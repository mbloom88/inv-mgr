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
# Revision on https://github.com/mbloom88/TBD
# 
# ==============================================================================

# ==============================================================================
# IMPORTS
# ==============================================================================

# Standard
import sqlite3
import sys
from os import path

# 3rd-Party
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.uic import loadUiType

# Local

# ==============================================================================
# LOADERS
# ==============================================================================

ui_dir = path.dirname('ui/')
form1, base1 = loadUiType(path.join(ui_dir, "main_win.ui"))

# ==============================================================================
# CLASSES
# ==============================================================================

class MainWin(base1, form1):

    # ==========================================================================
    # CLASSES
    # ==========================================================================

    def __init__(self, parent=None):
        super(base1, self).__init__(parent)
        self.setupUi(self)
        
        self._connect_buttons()

    # ==========================================================================
    # PROTECTED METHODS
    # ==========================================================================

    def _connect_buttons(self):
        self.btn_refresh.clicked.connect(self._get_db)

    #---------------------------------------------------------------------------

    def _get_db(self):
        """
        Connects to Sqlite3 database and fills out GUI table with data.
        """
        db = ''
        try:
            db = sqlite3.connect("db/parts.db")
        except Error as e:
            print(e)

        cursor = db.cursor()

        cmd = '''SELECT * from parts_table'''
        result = cursor.execute(cmd)

        self.table_inv.setRowCount(0)

        for row_num, row_data in enumerate(result):
            self.table_inv.insertRow(row_num)
            
            for col_num, cell_data in enumerate(row_data):
                new_item = QTableWidgetItem(str(cell_data))
                self.table_inv.setItem(row_num, col_num, new_item)

        db.commit()
        db.close()
 
# ==============================================================================
# FUNCTIONS
# ==============================================================================

def main():
    # Create application
    app = QApplication(sys.argv)
    
    # Create windows and show
    main_win = MainWin()
    main_win.show()

    # Execute the application and provide a clean exit on exceptions
    sys.exit(app.exec_())

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == '__main__':
    main()
