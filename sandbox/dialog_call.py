# ==============================================================================
# Name: dialog_call.py
# Author: Bloom, Matthew 
# Date: 02/24/2020
# Revision: 1.0.0
#
# ==============================================================================
# Description
# ------------------------------------------------------------------------------
# Sandbox controller.
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

# Local
from ui.Dialog import Ui_Dialog
from ui.MainWindow import Ui_MainWindow

# ==============================================================================
# CLASSES
# ==============================================================================

class MainWindow(QMainWindow, Ui_MainWindow):

    # ==========================================================================
    # INIT
    # ==========================================================================

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.btn_call_dialog.clicked.connect(self._event_call_dialog)

    # ==========================================================================
    # EVENTS
    # ==========================================================================

    def _event_call_dialog(self):
        dialog = QDialog()
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)
        dialog.show()
        resp = dialog.exec_()

        if resp == dialog.Accepted:
            self.lbl_call_dialog.setText("OK button was clicked")
        else:
            self.lbl_call_dialog.setText("Cancel button was clicked")

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def main():
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == '__main__':
    main()
