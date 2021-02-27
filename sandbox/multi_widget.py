# ==============================================================================
# Name: multi_widget.py
# Author: Bloom, Matthew 
# Date: 02/25/2020
# Revision: 1.0.0
#
# ==============================================================================
# Description
# ------------------------------------------------------------------------------
# Project file for course Python GUI Programming Recipes using PyQt5.
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
import sys
from time import sleep

# 3rd-Party
from PyQt5 import QtCore, QtGui, QtWidgets

# Local
from ui.MultiWidget import Ui_MultiWidget
from open_gl import PyQtOpenGL

# ==============================================================================
# CLASSES
# ==============================================================================

class ComboBox(QtWidgets.QComboBox):
    
    # ==========================================================================
    # CONSTRUCTORS
    # ==========================================================================

    def __init__(self, parent=None):
        super(ComboBox, self).__init__(parent)
        self.setAcceptDrops(True)

    # ==========================================================================
    # VIRTUAL METHODS
    # ==========================================================================

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    #---------------------------------------------------------------------------

    def dropEvent(self, event):
        self.addItem(event.mimeData().text())

#-------------------------------------------------------------------------------

class DragDropBtn(QtWidgets.QPushButton):

    # ==========================================================================
    # CONSTRUCTORS
    # ==========================================================================

    def __init__(self, text='', parent=None):
        super(DragDropBtn, self).__init__(text, parent)
        self.setAcceptDrops(True)

    # ==========================================================================
    # VIRTUAL METHODS
    # ==========================================================================

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    #---------------------------------------------------------------------------

    def dropEvent(self, event):
        self.setText(event.mimeData().text())

#-------------------------------------------------------------------------------

class MultiWidget():

    # ==========================================================================
    # CONSTRUCTORS
    # ==========================================================================

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        self.multi_widget = QtWidgets.QMainWindow()
        self.ui = Ui_MultiWidget()
        self.ui.setupUi(self.multi_widget)

        self._update_open_gl()
        self._update_combo_box()
        self._update_push_btn()
        self._update_tree()
        self._update_calendar()
        self._update_progress_bar()

        self.multi_widget.show()

        sys.exit(app.exec_())

    # ==========================================================================
    # PROTECTED METHODS
    # ==========================================================================

    def _print_tree(self):
        header_0 = self.ui.tree.headerItem().text(0)
        header_1 = self.ui.tree.headerItem().text(1)
        print(f"{header_0}\n{header_1}\n")
    
    #---------------------------------------------------------------------------

    def _start_progress_bar_counter(self, start_val):
        self.run_thread = RunThread(None, start_val)
        self.run_thread.start()
        self.run_thread.counter_updated.connect(self._event_set_progress_bar)

    #---------------------------------------------------------------------------

    def _update_calendar(self):
        self.ui.calendar.selectionChanged.connect(self._event_set_date)
    
    #---------------------------------------------------------------------------

    def _update_combo_box(self):
        self.ui.combo_box.hide()
        self.drag_drop_combo = ComboBox(self.multi_widget)
        # self.drag_drop_combo = ComboBox(self.multi_widget)
        self.drag_drop_combo.setMinimumSize(QtCore.QSize(153, 23))
        self.drag_drop_combo.setMaximumSize(QtCore.QSize(153, 23))
        self.ui.horizontalLayout_5.addWidget(self.drag_drop_combo)

    #---------------------------------------------------------------------------
    
    def _update_open_gl(self):
        self.open_gl = PyQtOpenGL(self.ui.frame_gl)
        self.open_gl.setMinimumSize(300, 300)
        self.open_gl.setMaximumSize(300, 300)

        self.open_gl.paint_0 = True # Draws a small, red square
        self.open_gl.paint_1 = True # Draws green lines
        self.open_gl.paint_2 = True # Draws black lines

    #---------------------------------------------------------------------------

    def _update_progress_bar(self):
        self.ui.radio_start.clicked.connect(self._event_start_progress_bar)
        self.ui.radio_stop.clicked.connect(self._event_stop_progress_bar)
        self.ui.radio_reset.clicked.connect(self._event_reset_progress_bar)
        self.progress_value = 0

    #---------------------------------------------------------------------------

    def _update_push_btn(self):
        self.ui.push_btn.hide()
        self.drag_drop_btn = DragDropBtn("DropButton", self.multi_widget)
        self.drag_drop_btn.setMinimumSize(QtCore.QSize(153, 23))
        self.drag_drop_btn.setMaximumSize(QtCore.QSize(153, 23))
        self.ui.horizontalLayout_5.addWidget(self.drag_drop_btn)

    #---------------------------------------------------------------------------

    def _update_tree(self):
        # self._print_tree()
        self.ui.tree.headerItem().setText(1, 'Header 2')
        # self._print_tree()

        # print(self.ui.tree.topLevelItem(0).text(0))
        # print(self.ui.tree.topLevelItem(0).child(0).text(0))

        self.ui.tree.topLevelItem(0).setText(1, "Item 2")
        # print(self.ui.tree.topLevelItem(0).text(1))

        self.ui.tree.topLevelItem(0).addChild(QtWidgets.QTreeWidgetItem())
        self.ui.tree.topLevelItem(0).child(0).setText(1, "Subitem 2")
        # print(self.ui.tree.topLevelItem(0).child(0).text(1))

    # ==========================================================================
    # EVENT METHODS
    # ==========================================================================
    
    def _event_reset_progress_bar(self):
        self._event_stop_progress_bar()
        self.progress_value = 0
        self.progress_stopped = False
        self.ui.progress_bar.reset()

    #---------------------------------------------------------------------------

    def _event_set_date(self):
        self.ui.date.setDate(self.ui.calendar.selectedDate())
    
    #---------------------------------------------------------------------------

    def _event_set_progress_bar(self, counter):
        if not self.progress_stopped:
            self.ui.progress_bar.setValue(counter)

    #---------------------------------------------------------------------------

    def _event_start_progress_bar(self):
        self.progress_stopped = False
        self.progress_value = self.ui.progress_bar.value()
        self._start_progress_bar_counter(self.progress_value)

    #---------------------------------------------------------------------------

    def _event_stop_progress_bar(self):
        self.progress_stopped = True

        try: 
            self.run_thread.stop()
        except:
            pass

#-------------------------------------------------------------------------------

class RunThread(QtCore.QThread):

    counter_updated = QtCore.pyqtSignal(int) # Define new signal

    # ==========================================================================
    # CONSTRUCTORS
    # ==========================================================================

    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True

    # ==========================================================================
    # VIRTUAL METHODS
    # ==========================================================================

    def run(self):
        while self.counter < 100 and self.is_running:
            sleep(0.1)
            self.counter += 1
            self.counter_updated.emit(self.counter) # Emit new signal with value

    #---------------------------------------------------------------------------

    def stop(self):
        self.is_running = False
        print('Stopping thread...')
        self.terminate()

# ==============================================================================
# FUNCTIONS
# ==============================================================================

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == '__main__':
    multi_widget = MultiWidget()
