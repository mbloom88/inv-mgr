# ==============================================================================
# Name: inv_mgr.py
# Author: Bloom, Matthew 
# Date: 02/24/2020
# Revision: 1.0.0
#
# ==============================================================================
# Description
# ------------------------------------------------------------------------------
# Fastener inventory manager that can browse current inventory from a database,
# add to it, an modify entries.
#
# ==============================================================================
# History
# ------------------------------------------------------------------------------
# Revision on https://github.com/mbloom88/inv-mgr
# 
# ==============================================================================

# ==============================================================================
# IMPORTS
# ==============================================================================

# Standard
from functools import partial
import sqlite3
import sys

# 3rd-Party
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# Local
from ui.MainWindow import Ui_MainWindow
from ui import images_rc

# ==============================================================================
# CLASSES
# ==============================================================================

class MainWindow(QMainWindow, Ui_MainWindow): # BaseClass, UiClass
    
    # Navigation directions
    FIRST = 0
    PREV = 1
    NEXT = 2
    LAST = 3

    # ==========================================================================
    # CONSTRUCTORS
    # ==========================================================================

    def __init__(self, parent=None):
        app = QApplication(sys.argv)
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self._connect_buttons()
        self.table_inv_idx = 0
        self._event_navigate_db(self.FIRST)

        self.show()
        sys.exit(app.exec_())

    # ==========================================================================
    # PROTECTED METHODS
    # ==========================================================================

    def _connect_buttons(self):
        """
        Connects all buttons in the Inventory Manager.
        """
        self.btn_refresh.clicked.connect(self._event_refresh_db)
        self.btn_search.clicked.connect(self._event_search_db)
        self.btn_check.clicked.connect(self._event_check_db)
        self.btn_update.clicked.connect(self._event_update_db_item)
        self.btn_del.clicked.connect(self._event_delete_db_item)
        self.btn_add.clicked.connect(self._event_add_db_item)
        self.btn_first.clicked.connect(partial(self._event_navigate_db, 
            self.FIRST))
        self.btn_prev.clicked.connect(partial(self._event_navigate_db, 
            self.PREV))
        self.btn_next.clicked.connect(partial(self._event_navigate_db, 
            self.NEXT))
        self.btn_last.clicked.connect(partial(self._event_navigate_db, 
            self.LAST))

    #---------------------------------------------------------------------------

    def _connect_db(self):
        """
        Establishes a connection to the SQLite3 database.

        Returns:
            - db: SQLite3 database.

        """
        try:
            db = sqlite3.connect("db/parts.db")
        except Error as e:
            print(e)

        return db

    #---------------------------------------------------------------------------

    def _update_table(self, result, table):
        """
        Updates the Inventory Details table with database information.

        Args:
            - result: database results from SQLite3 command.
            - table: the QTableWidget to modify.
        """
        table.setRowCount(0)

        for row_num, row_data in enumerate(result):
            table.insertRow(row_num)
            
            for col_num, cell_data in enumerate(row_data):
                new_item = QTableWidgetItem(str(cell_data))
                table.setItem(row_num, col_num, new_item)

    # ==========================================================================
    # EVENTS
    # ==========================================================================

    def _event_add_db_item(self):
        """
        Add a line item in the database.
        """
        db = self._connect_db()
        
        if not db:
            return

        cursor = db.cursor()
        row = (
            self.edit_ref.text(),
            self.edit_part_name.text(),
            self.edit_min_area.text(),
            self.edit_max_area.text(),
            self.edit_num_holes.value(),
            self.edit_min_dia.text(),
            self.edit_max_dia.text(),
            self.edit_count.value(),
        )
        cmd = '''INSERT INTO parts_table (ref, part_name, min_area, 
            max_area, num_holes, min_dia, max_dia, count) VALUES (?, ?, ?, ?, 
            ?, ?, ?, ?)'''
        cursor.execute(cmd, row)

        db.commit()
        db.close()

    #---------------------------------------------------------------------------

    def _event_check_db(self):
        """
        Checks the database for the top three references with the lowest 
        count.
        """
        db = self._connect_db()

        if not db:
            return

        cursor = db.cursor()
        cmd = '''SELECT ref, part_name, count from parts_table order by count 
            asc LIMIT 3'''
        result = cursor.execute(cmd)
        self._update_table(result, self.table_top_3)
    
    #---------------------------------------------------------------------------

    def _event_delete_db_item(self):
        """
        Delete a line item in the database.
        """
        db = self._connect_db()
        
        if not db:
            return

        cursor = db.cursor()
        del_id = self.edit_id.text()
        cmd = ''' DELETE FROM parts_table WHERE id=?'''
        cursor.execute(cmd, del_id)

        db.commit()
        db.close()

    #---------------------------------------------------------------------------

    def _event_navigate_db(self, direction):
        """
        Navigates the database based on the current Table Inventory index.

        Args:
            -direction: Direction to navigate.
        """
        db = self._connect_db()

        if not db:
            return

        cursor = db.cursor()
        cmd = '''SELECT * from parts_table'''
        result = cursor.execute(cmd)
        vals = result.fetchall()
        total_entries = len(vals)

        if direction == self.FIRST:
            self.table_inv_idx = 0
        elif direction == self.PREV:
            self.table_inv_idx -= 1
            if self.table_inv_idx < 0:
                self.table_inv_idx = total_entries - 1
        elif direction == self.NEXT:
            self.table_inv_idx += 1
            if self.table_inv_idx == total_entries:
                self.table_inv_idx = 0
        elif direction == self.LAST:
            self.table_inv_idx = total_entries - 1
        else:
            return

        val = vals[self.table_inv_idx]  

        self.edit_id.setText(str(val[0]))
        self.edit_ref.setText(str(val[1]))
        self.edit_part_name.setText(str(val[2]))
        self.edit_min_area.setText(str(val[3]))
        self.edit_max_area.setText(str(val[4]))
        self.edit_num_holes.setValue(val[5])
        self.edit_min_dia.setText(str(val[6]))
        self.edit_max_dia.setText(str(val[7]))
        self.edit_count.setValue(val[8])

        db.commit()
        db.close() 

    #---------------------------------------------------------------------------
    
    def _event_refresh_db(self):
        """
        Refreshes the Inventory Details table and the statistics shown in 
        Inventory Statistics.
        """
        db = self._connect_db()

        if not db:
            return

        cursor_1 = db.cursor()
        cmd_1 = '''SELECT * from parts_table'''
        result_1 = cursor_1.execute(cmd_1)
        self._update_table(result_1, self.table_inv)

        cursor_2 = db.cursor()
        cmd_2 = '''SELECT COUNT (DISTINCT ref) from parts_table'''
        result_2 = cursor_2.execute(cmd_2)
        self.num_ref.setText(str(result_2.fetchone()[0]))

        cursor_3 = db.cursor()
        cmd_3 = '''SELECT COUNT (DISTINCT part_name) from parts_table'''
        result_3 = cursor_3.execute(cmd_3)
        self.num_parts.setText(str(result_3.fetchone()[0]))

        cursor_4 = db.cursor()
        cmd_4 = '''SELECT MIN(num_holes), ref from parts_table'''
        temp_result_4 = cursor_4.execute(cmd_4)
        result_4 = temp_result_4.fetchone()
        self.min_num_holes.setText(str(result_4[0]))
        self.min_num_holes_ref.setText(str(result_4[1]))
        
        cursor_5 = db.cursor()
        cmd_5 = '''SELECT MAX(num_holes), ref from parts_table'''
        temp_result_5 = cursor_5.execute(cmd_5)
        result_5 = temp_result_5.fetchone()
        self.max_num_holes.setText(str(result_5[0])) 
        self.max_num_holes_ref.setText(str(result_5[1])) 

        db.commit()
        db.close()

    #---------------------------------------------------------------------------

    def _event_search_db(self):
        """
        Searches for line items with a specific count in the Inventory Details
        table.
        """
        db = self._connect_db()

        if not db:
            return

        cursor = db.cursor()
        num = self.count_num.value()
        cmd = '''SELECT * from parts_table WHERE count<=?'''
        result = cursor.execute(cmd, [num])
        self._update_table(result, self.table_inv)

        db.commit()
        db.close()

    #---------------------------------------------------------------------------

    def _event_update_db_item(self):
        """
        Update a line item in the database.
        """
        db = self._connect_db()
        
        if not db:
            return

        cursor = db.cursor()
        row = (
            self.edit_ref.text(),
            self.edit_part_name.text(),
            self.edit_min_area.text(),
            self.edit_max_area.text(),
            self.edit_num_holes.value(),
            self.edit_min_dia.text(),
            self.edit_max_dia.text(),
            self.edit_count.value(),
            self.edit_id.text(),
        )
        cmd = '''UPDATE parts_table SET ref=?, part_name=?, min_area=?, 
            max_area=?, num_holes=?, min_dia=?, max_dia=?, count=? WHERE id=?'''
        cursor.execute(cmd, row)

        db.commit()
        db.close()

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == '__main__':
    main_window = MainWindow()
