# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MultiWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultiWidget(object):
    def setupUi(self, MultiWidget):
        MultiWidget.setObjectName("MultiWidget")
        MultiWidget.resize(516, 402)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MultiWidget.sizePolicy().hasHeightForWidth())
        MultiWidget.setSizePolicy(sizePolicy)
        MultiWidget.setMinimumSize(QtCore.QSize(516, 402))
        MultiWidget.setMaximumSize(QtCore.QSize(516, 402))
        self.centralwidget = QtWidgets.QWidget(MultiWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.tab_widgets1 = QtWidgets.QWidget()
        self.tab_widgets1.setObjectName("tab_widgets1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_widgets1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_widgets1)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_tree = QtWidgets.QWidget()
        self.tab_tree.setObjectName("tab_tree")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_tree)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tree = QtWidgets.QTreeWidget(self.tab_tree)
        self.tree.setObjectName("tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout_3.addWidget(self.tree)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_tree, "")
        self.tab_calendar = QtWidgets.QWidget()
        self.tab_calendar.setObjectName("tab_calendar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_calendar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.date = QtWidgets.QDateEdit(self.tab_calendar)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setTimeSpec(QtCore.Qt.LocalTime)
        self.date.setObjectName("date")
        self.verticalLayout_4.addWidget(self.date)
        self.calendar = QtWidgets.QCalendarWidget(self.tab_calendar)
        self.calendar.setObjectName("calendar")
        self.verticalLayout_4.addWidget(self.calendar)
        self.tabWidget_2.addTab(self.tab_calendar, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabs.addTab(self.tab_widgets1, "")
        self.tab_widgets2 = QtWidgets.QWidget()
        self.tab_widgets2.setObjectName("tab_widgets2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_widgets2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.choose_option = QtWidgets.QGroupBox(self.tab_widgets2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_option.sizePolicy().hasHeightForWidth())
        self.choose_option.setSizePolicy(sizePolicy)
        self.choose_option.setMinimumSize(QtCore.QSize(160, 150))
        self.choose_option.setMaximumSize(QtCore.QSize(160, 150))
        self.choose_option.setObjectName("choose_option")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.choose_option)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radio_start = QtWidgets.QRadioButton(self.choose_option)
        self.radio_start.setChecked(True)
        self.radio_start.setObjectName("radio_start")
        self.verticalLayout_5.addWidget(self.radio_start)
        self.radio_stop = QtWidgets.QRadioButton(self.choose_option)
        self.radio_stop.setObjectName("radio_stop")
        self.verticalLayout_5.addWidget(self.radio_stop)
        self.radio_reset = QtWidgets.QRadioButton(self.choose_option)
        self.radio_reset.setObjectName("radio_reset")
        self.verticalLayout_5.addWidget(self.radio_reset)
        self.horizontalLayout_2.addWidget(self.choose_option)
        self.move_dial = QtWidgets.QGroupBox(self.tab_widgets2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.move_dial.sizePolicy().hasHeightForWidth())
        self.move_dial.setSizePolicy(sizePolicy)
        self.move_dial.setMinimumSize(QtCore.QSize(300, 150))
        self.move_dial.setMaximumSize(QtCore.QSize(150, 16777215))
        self.move_dial.setObjectName("move_dial")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.move_dial)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dial = QtWidgets.QDial(self.move_dial)
        self.dial.setObjectName("dial")
        self.horizontalLayout.addWidget(self.dial)
        self.lcd_num = QtWidgets.QLCDNumber(self.move_dial)
        self.lcd_num.setStyleSheet("color: rgb(0, 0, 255);\n"
"")
        self.lcd_num.setDigitCount(2)
        self.lcd_num.setObjectName("lcd_num")
        self.horizontalLayout.addWidget(self.lcd_num)
        self.horizontalLayout_2.addWidget(self.move_dial)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.font_box = QtWidgets.QFontComboBox(self.tab_widgets2)
        self.font_box.setObjectName("font_box")
        self.verticalLayout_7.addWidget(self.font_box)
        self.font_label = QtWidgets.QLabel(self.tab_widgets2)
        self.font_label.setStyleSheet("font: 12pt \"Arial\";")
        self.font_label.setText("")
        self.font_label.setObjectName("font_label")
        self.verticalLayout_7.addWidget(self.font_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progress_bar = QtWidgets.QProgressBar(self.tab_widgets2)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout_3.addWidget(self.progress_bar)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tabs.addTab(self.tab_widgets2, "")
        self.tab_dragdrop = QtWidgets.QWidget()
        self.tab_dragdrop.setObjectName("tab_dragdrop")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_dragdrop)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_edit = QtWidgets.QLineEdit(self.tab_dragdrop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit.sizePolicy().hasHeightForWidth())
        self.line_edit.setSizePolicy(sizePolicy)
        self.line_edit.setText("")
        self.line_edit.setDragEnabled(True)
        self.line_edit.setObjectName("line_edit")
        self.horizontalLayout_5.addWidget(self.line_edit)
        self.combo_box = QtWidgets.QComboBox(self.tab_dragdrop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_box.sizePolicy().hasHeightForWidth())
        self.combo_box.setSizePolicy(sizePolicy)
        self.combo_box.setAcceptDrops(True)
        self.combo_box.setEditable(True)
        self.combo_box.setCurrentText("")
        self.combo_box.setObjectName("combo_box")
        self.horizontalLayout_5.addWidget(self.combo_box)
        self.push_btn = QtWidgets.QPushButton(self.tab_dragdrop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_btn.sizePolicy().hasHeightForWidth())
        self.push_btn.setSizePolicy(sizePolicy)
        self.push_btn.setAcceptDrops(True)
        self.push_btn.setObjectName("push_btn")
        self.horizontalLayout_5.addWidget(self.push_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.list_1 = QtWidgets.QListWidget(self.tab_dragdrop)
        self.list_1.setDragEnabled(True)
        self.list_1.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.list_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_1.setObjectName("list_1")
        item = QtWidgets.QListWidgetItem()
        self.list_1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_1.addItem(item)
        self.horizontalLayout_6.addWidget(self.list_1)
        self.list_2 = QtWidgets.QListWidget(self.tab_dragdrop)
        self.list_2.setDragEnabled(True)
        self.list_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.list_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_2.setObjectName("list_2")
        self.horizontalLayout_6.addWidget(self.list_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.tabs.addTab(self.tab_dragdrop, "")
        self.tab_open_gl = QtWidgets.QWidget()
        self.tab_open_gl.setObjectName("tab_open_gl")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_open_gl)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_gl = QtWidgets.QFrame(self.tab_open_gl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_gl.sizePolicy().hasHeightForWidth())
        self.frame_gl.setSizePolicy(sizePolicy)
        self.frame_gl.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_gl.setMaximumSize(QtCore.QSize(300, 300))
        self.frame_gl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gl.setObjectName("frame_gl")
        self.gridLayout.addWidget(self.frame_gl, 0, 0, 1, 1)
        self.tabs.addTab(self.tab_open_gl, "")
        self.verticalLayout_2.addWidget(self.tabs)
        MultiWidget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MultiWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName("menubar")
        MultiWidget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MultiWidget)
        self.statusbar.setObjectName("statusbar")
        MultiWidget.setStatusBar(self.statusbar)

        self.retranslateUi(MultiWidget)
        self.tabs.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.dial.valueChanged['int'].connect(self.lcd_num.display)
        self.font_box.activated['QString'].connect(self.font_label.setText)
        QtCore.QMetaObject.connectSlotsByName(MultiWidget)

    def retranslateUi(self, MultiWidget):
        _translate = QtCore.QCoreApplication.translate
        MultiWidget.setWindowTitle(_translate("MultiWidget", "Multi-Widget"))
        self.tree.headerItem().setText(0, _translate("MultiWidget", "Header 1"))
        self.tree.headerItem().setText(1, _translate("MultiWidget", "New Column"))
        __sortingEnabled = self.tree.isSortingEnabled()
        self.tree.setSortingEnabled(False)
        self.tree.topLevelItem(0).setText(0, _translate("MultiWidget", "Item 1"))
        self.tree.topLevelItem(0).child(0).setText(0, _translate("MultiWidget", "Subitem 1"))
        self.tree.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_tree), _translate("MultiWidget", "Tree"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_calendar), _translate("MultiWidget", "Calendar"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_widgets1), _translate("MultiWidget", "Widgets 1"))
        self.choose_option.setTitle(_translate("MultiWidget", "Choose Option"))
        self.radio_start.setStatusTip(_translate("MultiWidget", "Start the Progress Bar"))
        self.radio_start.setText(_translate("MultiWidget", "Start"))
        self.radio_stop.setStatusTip(_translate("MultiWidget", "Stop the Progress Bar"))
        self.radio_stop.setText(_translate("MultiWidget", "Stop"))
        self.radio_reset.setStatusTip(_translate("MultiWidget", "Reset the Progress Bar"))
        self.radio_reset.setText(_translate("MultiWidget", "Reset"))
        self.move_dial.setTitle(_translate("MultiWidget", "Move the Dial"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_widgets2), _translate("MultiWidget", "Widgets 2"))
        self.push_btn.setText(_translate("MultiWidget", "PushButton"))
        __sortingEnabled = self.list_1.isSortingEnabled()
        self.list_1.setSortingEnabled(False)
        item = self.list_1.item(0)
        item.setText(_translate("MultiWidget", "Item 1"))
        item = self.list_1.item(1)
        item.setText(_translate("MultiWidget", "Item 2"))
        item = self.list_1.item(2)
        item.setText(_translate("MultiWidget", "Item 3"))
        item = self.list_1.item(3)
        item.setText(_translate("MultiWidget", "Item 4"))
        self.list_1.setSortingEnabled(__sortingEnabled)
        self.tabs.setTabText(self.tabs.indexOf(self.tab_dragdrop), _translate("MultiWidget", "Drag && Drop"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_open_gl), _translate("MultiWidget", "Open GL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MultiWidget = QtWidgets.QMainWindow()
    ui = Ui_MultiWidget()
    ui.setupUi(MultiWidget)
    MultiWidget.show()
    sys.exit(app.exec_())
