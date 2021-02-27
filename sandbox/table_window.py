# ==============================================================================
# Name: table_window.py
# Author: Bloom, Matthew 
# Date: 02/24/2020
# Revision: 1.0.0
#
# ==============================================================================
# Description
# ------------------------------------------------------------------------------
# N/A
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

# 3rd-Party
from PyQt5 import QtCore, QtGui, QtWidgets

# Local
from ui.TableWindow import Ui_TableWindow
       
# ==============================================================================
# FUNCTIONS
# ==============================================================================

def btn1_clicked():
    ui.btn1.setText("Button 1 was clicked!")

#-------------------------------------------------------------------------------

def btn2_clicked():
    ui.btn2.setText("Button 2 was clicked!")

#-------------------------------------------------------------------------------

def set_table_items():
    row = 0
    ui.table.setItem(row, 0, QtWidgets.QTableWidgetItem("item1"))
    ui.table.setItem(1, 1, QtWidgets.QTableWidgetItem("item2"))
    ui.table.setItem(2, 2, QtWidgets.QTableWidgetItem("item3"))

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    table_window = QtWidgets.QMainWindow()
    ui = Ui_TableWindow()
    ui.setupUi(table_window)
    
    set_table_items()
    ui.btn1.clicked.connect(btn1_clicked)
    ui.btn2.clicked.connect(btn2_clicked)

    table_window.show()

    sys.exit(app.exec_())
