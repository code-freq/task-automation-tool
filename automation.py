from PyQt6 import QtCore, QtGui, QtWidgets
from main import *

class Ui_MainWindow(object):
    # Default setup functon of pyqt6-designer
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 661)
        MainWindow.setMinimumSize(QtCore.QSize(894, 661))
        MainWindow.setMaximumSize(QtCore.QSize(894, 661))
        MainWindow.setIconSize(QtCore.QSize(24, 24))

        MainWindow.setWindowIcon(QtGui.QIcon('assets/code-freq.png'))

        # self variables
        self.invalid_des_name = False
        self.invalid_pre_name = False
        self.invalid_ext_name = False
        self.invalid_ext_name_2 = False
        self.invalid_suf_name = False

        self.format_valid = False
        self.format_clicked = False
        self.selections_list = []
        self.path = ""
        self.des_name = ""
        self.des_ext = ""
        self.filter_ = ""
        self.start = None
        self.seq = False

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 80, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_folder_label = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.select_folder_label.setReadOnly(True)
        self.select_folder_label.setObjectName("select_folder_label")
        self.horizontalLayout.addWidget(self.select_folder_label)
        self.select_folder_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.select_folder_button.setObjectName("select_folder_button")
        self.select_folder_button.setStyleSheet('QPushButton {background-color: #943e8a; color: white}')
        self.select_folder_button.clicked.connect(self.select_folder_func)
        self.horizontalLayout.addWidget(self.select_folder_button)  # Connect to self.select_folder

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(350, 140, 180, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_automation_type = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_2)
        self.select_automation_type.setMouseTracking(False)
        self.select_automation_type.setObjectName("select_automation_type")
        self.select_automation_type.addItem("")
        self.select_automation_type.addItem("")
        self.select_automation_type.currentIndexChanged.connect(self.seq_comb)
        self.horizontalLayout_2.addWidget(self.select_automation_type)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(230, 440, 421, 132))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.would_you_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.would_you_layout.setContentsMargins(0, 0, 0, 0)
        self.would_you_layout.setObjectName("would_you_layout")
        self.would_you_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.would_you_label.setObjectName("would_you_label")
        self.would_you_layout.addWidget(self.would_you_label)
        self.rename_all_radio = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_3)
        self.rename_all_radio.setObjectName("rename_all_radio")
        self.rename_all_radio.clicked.connect(self.all_radio)

        self.would_you_layout.addWidget(self.rename_all_radio)
        self.rename_specific_radio = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_3)
        self.rename_specific_radio.setObjectName("rename_specific_radio")
        self.rename_specific_radio.clicked.connect(self.specific_radio)

        self.would_you_layout.addWidget(self.rename_specific_radio)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.enter_startwith_label = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.enter_startwith_label.setObjectName("enter_startwith_label")
        self.horizontalLayout_6.addWidget(self.enter_startwith_label)
        self.would_you_layout.addLayout(self.horizontalLayout_6)

        self.submit_button = QtWidgets.QPushButton()
        self.submit_button.setStyleSheet('QPushButton {background-color: green; color: white}')
        self.submit_button.setObjectName("submit_button")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.submit_button.setFont(font)
        self.submit_button.clicked.connect(self.main_submit)
        self.would_you_layout.addWidget(self.submit_button)


        self.result_message_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_message_label.setWordWrap(True)
        self.result_message_label.adjustSize()
        self.result_message_label.setGeometry(QtCore.QRect(160, 590, 561, 41))
        self.result_message_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_message_label.setObjectName("result_message_label")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.result_message_label.setFont(font)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 801, 41))
        self.label.setStyleSheet("color: #a8adf7")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(450, 230, 391, 191))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.combinational_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.combinational_layout.setContentsMargins(0, 0, 0, 0)
        self.combinational_layout.setSpacing(1)
        self.combinational_layout.setObjectName("combinational_layout")

        self.addprefix_checkBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_4)
        self.addprefix_checkBox.setObjectName("addprefix_checkBox")
        self.addprefix_checkBox.stateChanged.connect(self.prefix_checkbox)


        self.combinational_layout.addWidget(self.addprefix_checkBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Add_prefix_label = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.Add_prefix_label.setObjectName("Add_prefix_label")
        self.horizontalLayout_5.addWidget(self.Add_prefix_label)
        self.combinational_layout.addLayout(self.horizontalLayout_5)

        self.addsuffix_checkBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_4)
        self.addsuffix_checkBox.setObjectName("addsuffix_checkBox")
        self.addsuffix_checkBox.stateChanged.connect(self.suffix_checkbox)

        self.combinational_layout.addWidget(self.addsuffix_checkBox)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.add_suffix_label = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.add_suffix_label.setObjectName("add_suffix_label")
        self.horizontalLayout_7.addWidget(self.add_suffix_label)
        self.combinational_layout.addLayout(self.horizontalLayout_7)

        self.change_ext_checkBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_4)
        self.change_ext_checkBox.setObjectName("change_ext_checkBox")
        self.change_ext_checkBox.stateChanged.connect(self.ext_checkbox)

        self.combinational_layout.addWidget(self.change_ext_checkBox)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.add_suffix_label_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.add_suffix_label_2.setText("")
        self.add_suffix_label_2.setObjectName("add_suffix_label_2")
        self.horizontalLayout_8.addWidget(self.add_suffix_label_2)
        self.combinational_layout.addLayout(self.horizontalLayout_8)

        self.submit_comb_button = QtWidgets.QPushButton()
        self.submit_comb_button.setStyleSheet('QPushButton {background-color: #4a6741; color: white}')
        self.submit_comb_button.setObjectName("submit_comb_button")
        self.submit_comb_button.clicked.connect(self.comb_submit_clicked)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.submit_comb_button.setFont(font)
        self.combinational_layout.addWidget(self.submit_comb_button)

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 180, 371, 247))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.sequential_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.sequential_layout.setContentsMargins(0, 0, 0, 0)
        self.sequential_layout.setSpacing(6)
        self.sequential_layout.setObjectName("sequential_layout")
        self.please_select_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.please_select_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.please_select_label.setFont(font)
        self.please_select_label.setAutoFillBackground(False)
        self.please_select_label.setObjectName("please_select_label")
        self.sequential_layout.addWidget(self.please_select_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.select_format_1 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.select_format_1.setObjectName("select_format_1")
        self.select_format_1.addItem("")
        self.select_format_1.addItem("")
        self.select_format_1.addItem("")
        self.select_format_1.addItem("")
        self.select_format_1.addItem("")
        self.select_format_1.addItem("")
        self.horizontalLayout_3.addWidget(self.select_format_1)
        self.select_format_2 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.select_format_2.setObjectName("select_format_2")
        self.select_format_2.addItem("")
        self.select_format_2.addItem("")
        self.select_format_2.addItem("")
        self.select_format_2.addItem("")
        self.select_format_2.addItem("")
        self.select_format_2.addItem("")
        self.horizontalLayout_3.addWidget(self.select_format_2)
        self.select_format_3 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.select_format_3.setObjectName("select_format_3")
        self.select_format_3.addItem("")
        self.select_format_3.addItem("")
        self.select_format_3.addItem("")
        self.select_format_3.addItem("")
        self.select_format_3.addItem("")
        self.select_format_3.addItem("")
        self.horizontalLayout_3.addWidget(self.select_format_3)
        self.select_format_4 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.select_format_4.setObjectName("select_format_4")
        self.select_format_4.addItem("")
        self.select_format_4.addItem("")
        self.select_format_4.addItem("")
        self.select_format_4.addItem("")
        self.select_format_4.addItem("")
        self.select_format_4.addItem("")
        self.horizontalLayout_3.addWidget(self.select_format_4)
        self.select_format_5 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.select_format_5.setObjectName("select_format_5")
        self.select_format_5.addItem("")
        self.select_format_5.addItem("")
        self.select_format_5.addItem("")
        self.select_format_5.addItem("")
        self.select_format_5.addItem("")
        self.select_format_5.addItem("")
        self.horizontalLayout_3.addWidget(self.select_format_5)
        self.sequential_layout.addLayout(self.horizontalLayout_3)
        self.select_format_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.select_format_button.setObjectName("select_format_button")
        self.select_format_button.setStyleSheet('QPushButton {background-color: #943e8a; color: white}')

        self.select_format_button.clicked.connect(self.apply_format)

        self.sequential_layout.addWidget(self.select_format_button)
        self.warning_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.warning_label.setObjectName("warning_label")
        self.sequential_layout.addWidget(self.warning_label)
        self.change_name_ext_checkbox_layout = QtWidgets.QVBoxLayout()
        self.change_name_ext_checkbox_layout.setObjectName("change_name_ext_checkbox_layout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.change_name_checkbox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.change_name_checkbox.setObjectName("change_name_checkbox")
        self.change_name_checkbox.stateChanged.connect(self.seq_name_checkbox)

        self.horizontalLayout_4.addWidget(self.change_name_checkbox)

        self.change_ext__checkbox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.change_ext__checkbox.setObjectName("change_ext__checkbox")
        self.change_ext__checkbox.stateChanged.connect(self.seq_ext_checkbox)

        self.horizontalLayout_4.addWidget(self.change_ext__checkbox)
        self.change_name_ext_checkbox_layout.addLayout(self.horizontalLayout_4)
        self.sequential_layout.addLayout(self.change_name_ext_checkbox_layout)
        self.desired_filename_layout = QtWidgets.QHBoxLayout()
        self.desired_filename_layout.setObjectName("desired_filename_layout")
        self.type_name_label = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.type_name_label.setObjectName("type_name_label")
        self.desired_filename_layout.addWidget(self.type_name_label)

        self.sequential_layout.addLayout(self.desired_filename_layout)
        self.desired_ext_layout = QtWidgets.QHBoxLayout()
        self.desired_ext_layout.setObjectName("desired_ext_layout")
        self.type_ext_label = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.type_ext_label.setObjectName("type_ext_label")
        self.desired_ext_layout.addWidget(self.type_ext_label)

        self.sequential_layout.addLayout(self.desired_ext_layout)
        self.starting_number_layout = QtWidgets.QHBoxLayout()
        self.starting_number_layout.setObjectName("starting_number_layout")
        self.enter_starting_number_label = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.enter_starting_number_label.setObjectName("enter_starting_number_label")
        self.starting_number_layout.addWidget(self.enter_starting_number_label)

        self.sequential_layout.addLayout(self.starting_number_layout)

        self.submit_seq_button = QtWidgets.QPushButton()
        self.submit_seq_button.setStyleSheet('QPushButton {background-color: #4a6741; color: white}')
        self.submit_seq_button.setObjectName("submit_seq_button")
        self.submit_seq_button.clicked.connect(self.seq_submit_clicked)

        font = QtGui.QFont()
        font.setPointSize(13)
        self.submit_seq_button.setFont(font)
        self.sequential_layout.addWidget(self.submit_seq_button)

        # Initial hide/show situations
        set_layout_or_widget_visible(self.sequential_layout, False)
        set_layout_or_widget_visible(self.would_you_layout, False)
        set_layout_or_widget_visible(self.horizontalLayout_5, False)
        set_layout_or_widget_visible(self.horizontalLayout_7, False)
        set_layout_or_widget_visible(self.horizontalLayout_8, False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Default function of pyqt6 designer
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task Automation Tool - by ~code-freq~"))
        self.submit_button.setText(_translate("MainWindow", "Start Automation"))
        self.select_folder_label.setPlaceholderText(_translate("MainWindow", "Please select a folder"))
        self.select_folder_button.setText(_translate("MainWindow", "Select"))
        self.select_automation_type.setPlaceholderText(_translate("MainWindow", "Select automation type"))
        self.select_automation_type.setItemText(0, _translate("MainWindow", "Combinational Automation"))
        self.select_automation_type.setItemText(1, _translate("MainWindow", "Sequential Automation"))
        self.submit_comb_button.setText(_translate("MainWindow", "Submit"))
        self.submit_seq_button.setText(_translate("MainWindow", "Submit"))
        self.would_you_label.setText(_translate("MainWindow", "Would you like to rename all files or only those starting with a specific text?"))
        self.rename_all_radio.setText(_translate("MainWindow", "Rename all files"))
        self.rename_specific_radio.setText(_translate("MainWindow", "Rename only files starting with specific text"))
        self.enter_startwith_label.setPlaceholderText(_translate("MainWindow", "Enter the text that the files should start with"))
        self.result_message_label.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "WELCOME TO TASK AUTOMATION TOOL"))
        self.addprefix_checkBox.setText(_translate("MainWindow", "Add Prefix"))
        self.Add_prefix_label.setPlaceholderText(_translate("MainWindow", "Desired Prefix"))
        self.addsuffix_checkBox.setText(_translate("MainWindow", "Add Suffix"))
        self.add_suffix_label.setPlaceholderText(_translate("MainWindow", "Desired Suffix"))
        self.change_ext_checkBox.setText(_translate("MainWindow", "Change Extension"))
        self.add_suffix_label_2.setPlaceholderText(_translate("MainWindow", "Desired Extension (e.g. txt, png)"))
        self.please_select_label.setText(_translate("MainWindow", "Please select the format of your desired file name:"))
        self.select_format_1.setItemText(0, _translate("MainWindow", "None"))
        self.select_format_1.setItemText(1, _translate("MainWindow", "Name"))
        self.select_format_1.setItemText(2, _translate("MainWindow", "Number"))
        self.select_format_1.setItemText(3, _translate("MainWindow", "Date"))
        self.select_format_1.setItemText(4, _translate("MainWindow", "Time"))
        self.select_format_1.setItemText(5, _translate("MainWindow", "Year"))
        self.select_format_2.setItemText(0, _translate("MainWindow", "None"))
        self.select_format_2.setItemText(1, _translate("MainWindow", "Name"))
        self.select_format_2.setItemText(2, _translate("MainWindow", "Number"))
        self.select_format_2.setItemText(3, _translate("MainWindow", "Date"))
        self.select_format_2.setItemText(4, _translate("MainWindow", "Time"))
        self.select_format_2.setItemText(5, _translate("MainWindow", "Year"))
        self.select_format_3.setItemText(0, _translate("MainWindow", "None"))
        self.select_format_3.setItemText(1, _translate("MainWindow", "Name"))
        self.select_format_3.setItemText(2, _translate("MainWindow", "Number"))
        self.select_format_3.setItemText(3, _translate("MainWindow", "Date"))
        self.select_format_3.setItemText(4, _translate("MainWindow", "Time"))
        self.select_format_3.setItemText(5, _translate("MainWindow", "Year"))
        self.select_format_4.setItemText(0, _translate("MainWindow", "None"))
        self.select_format_4.setItemText(1, _translate("MainWindow", "Name"))
        self.select_format_4.setItemText(2, _translate("MainWindow", "Number"))
        self.select_format_4.setItemText(3, _translate("MainWindow", "Date"))
        self.select_format_4.setItemText(4, _translate("MainWindow", "Time"))
        self.select_format_4.setItemText(5, _translate("MainWindow", "Year"))
        self.select_format_5.setItemText(0, _translate("MainWindow", "None"))
        self.select_format_5.setItemText(1, _translate("MainWindow", "Name"))
        self.select_format_5.setItemText(2, _translate("MainWindow", "Number"))
        self.select_format_5.setItemText(3, _translate("MainWindow", "Date"))
        self.select_format_5.setItemText(4, _translate("MainWindow", "Time"))
        self.select_format_5.setItemText(5, _translate("MainWindow", "Year"))
        self.select_format_button.setText(_translate("MainWindow", "Select Format"))
        self.warning_label.setText(_translate("MainWindow", ""))
        self.change_name_checkbox.setText(_translate("MainWindow", "Change Name"))
        self.change_ext__checkbox.setText(_translate("MainWindow", "Change Extension"))
        self.type_name_label.setPlaceholderText(_translate("MainWindow", "Desired File Name"))
        self.type_ext_label.setPlaceholderText(_translate("MainWindow", "Desired Extension (e.g. txt, png)"))
        self.enter_starting_number_label.setPlaceholderText(_translate("MainWindow", "Enter the starting number for file numbering"))

    # Manage automation type
    def seq_comb(self, index):
        # reset combinational
        if index == 0:
            set_layout_or_widget_visible(self.combinational_layout, True)
            set_layout_or_widget_visible(self.sequential_layout, False)
            set_layout_or_widget_visible(self.would_you_layout, False)
            set_layout_or_widget_visible(self.horizontalLayout_5, False)
            set_layout_or_widget_visible(self.horizontalLayout_7, False)
            set_layout_or_widget_visible(self.horizontalLayout_8, False)
            self.enter_startwith_label.setText("")
            self.add_suffix_label.setText("")
            self.Add_prefix_label.setText("")
            self.add_suffix_label_2.setText("")
            self.addprefix_checkBox.setChecked(False)
            self.addsuffix_checkBox.setChecked(False)
            self.change_ext_checkBox.setChecked(False)

        # reset sequential
        elif index == 1:
            self.select_format_1.setCurrentIndex(0)
            self.select_format_2.setCurrentIndex(0)
            self.select_format_3.setCurrentIndex(0)
            self.select_format_4.setCurrentIndex(0)
            self.select_format_5.setCurrentIndex(0)

            self.format_clicked = False
            set_layout_or_widget_visible(self.combinational_layout, False)
            set_layout_or_widget_visible(self.would_you_layout, False)
            set_layout_or_widget_visible(self.sequential_layout, True)
            set_layout_or_widget_visible(self.desired_filename_layout, False)
            set_layout_or_widget_visible(self.desired_ext_layout, False)
            set_layout_or_widget_visible(self.warning_label, False)
            self.type_name_label.setText("")
            self.enter_startwith_label.setText("")
            self.type_ext_label.setText("")
            self.enter_starting_number_label.setText("")
            self.change_name_checkbox.setChecked(False)
            self.change_ext__checkbox.setChecked(False)
            self.start = None
            self.format_valid = False
            self.seq = False
            self.selections_list = []

    # Hide / Show add prefix in the combinational automation
    def prefix_checkbox(self):
        if self.addprefix_checkBox.isChecked():
            set_layout_or_widget_visible(self.horizontalLayout_5, True)
        else:
            set_layout_or_widget_visible(self.horizontalLayout_5, False)

    # Hide / Show add suffix in the combinational automation
    def suffix_checkbox(self):
        if self.addsuffix_checkBox.isChecked():
            set_layout_or_widget_visible(self.horizontalLayout_7, True)
        else:
            set_layout_or_widget_visible(self.horizontalLayout_7, False)

    # Hide / Show add ext in the combinational automation
    def ext_checkbox(self):
        if self.change_ext_checkBox.isChecked():
            set_layout_or_widget_visible(self.horizontalLayout_8, True)
        else:
            set_layout_or_widget_visible(self.horizontalLayout_8, False)

    # Hide / Show add name in the sequential automation
    def seq_name_checkbox(self):
        if self.change_name_checkbox.isChecked():
            set_layout_or_widget_visible(self.desired_filename_layout, True)
            self.des_name = self.type_name_label.text()
        else:
            self.des_name = ""
            set_layout_or_widget_visible(self.desired_filename_layout, False)

    # Hide / Show add ext in the sequential automation
    def seq_ext_checkbox(self):
        if self.change_ext__checkbox.isChecked():
            set_layout_or_widget_visible(self.desired_ext_layout, True)
            self.des_ext = self.type_ext_label.text()
        else:
            self.des_ext = ""
            set_layout_or_widget_visible(self.desired_ext_layout, False)

    # Process format button
    def apply_format(self):
        # Get combobox choices
        sel1 = self.select_format_1.currentText()
        sel2 = self.select_format_2.currentText()
        sel3 = self.select_format_3.currentText()
        sel4 = self.select_format_4.currentText()
        sel5 = self.select_format_5.currentText()
        self.format_clicked = True

        # Check if number selected or not as a format
        self.selections_list = [sel1,sel2,sel3,sel4,sel5]
        if not "Number" in self.selections_list:
            self.warning_label.setText("Number is required for sequential numbering...")
            self.warning_label.setStyleSheet("color: #f53b3b")
            set_layout_or_widget_visible(self.warning_label, True)
            self.format_valid = False
        else:
            # Drop None values
            [self.selections_list.pop(i) for i in range(len(self.selections_list)-1, -1, -1) if self.selections_list[i] == "None"]
            format_text = "_".join(self.selections_list)
            self.warning_label.setText(format_text)
            self.warning_label.setStyleSheet("color: #bebf15")
            set_layout_or_widget_visible(self.warning_label, True)
            self.format_valid = True

    # Select folder
    def select_folder_func(self):
        self.path = select_folder()
        self.select_folder_label.setPlaceholderText(self.path)
        if self.path != "":
            self.result_message_label.setVisible(False)

    # Sequential Submit Button Clicked
    def seq_submit_clicked(self):
        # Check checkboxes
        if self.change_name_checkbox.isChecked():
            des_name_text = self.type_name_label.text()
            invalid_chars = ["#", "%", "&", "{", "}", "\\","<",">","*","?","/","$","!","'","\"",":","@","+",
                             "`", "|", "="]
            self.invalid_des_name = False
            for i in des_name_text:
                if i in invalid_chars:
                    self.invalid_des_name = True
            if self.invalid_des_name:
                self.result_message_label.setText("Invalid character for a file name..")
                self.result_message_label.setStyleSheet("color: red")
                self.result_message_label.setVisible(True)
            else:
                self.des_name = des_name_text
                self.result_message_label.setVisible(False)

        else:
            self.des_name = ""

        if self.change_ext__checkbox.isChecked():
            des_ext_text = self.type_ext_label.text()
            invalid_chars = ["#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "$", "!", "'", "\"", ":", "@", "+",
                             "`", "|", "="]
            self.invalid_ext_name = False
            for i in des_ext_text:
                if i in invalid_chars:
                    self.invalid_ext_name = True
            if self.invalid_ext_name:
                self.result_message_label.setText("Invalid character for an extension name..")
                self.result_message_label.setStyleSheet("color: red")
                self.result_message_label.setVisible(True)
            else:
                self.des_name = des_ext_text
                self.result_message_label.setVisible(False)

        # Check starting number input
        try:
            int_inp = int(self.enter_starting_number_label.text().strip())
            if 1 > int_inp:
                self.result_message_label.setText("You must enter a number bigger than 0..")
                self.result_message_label.setStyleSheet("color: #fa7828")
                self.result_message_label.setVisible(True)
                set_layout_or_widget_visible(self.would_you_layout, False)
            else:
                self.result_message_label.setVisible(False)
                self.start = int_inp

                # If everything is right
                if self.format_valid and not (self.invalid_des_name or self.invalid_ext_name):
                    set_layout_or_widget_visible(self.would_you_layout, True)
                    self.rename_all_radio.setChecked(True)
                    self.rename_specific_radio.setChecked(False)
                    set_layout_or_widget_visible(self.enter_startwith_label, False)
                    self.seq = True

                # if format button not clicked
                elif not self.format_clicked:
                    self.result_message_label.setText("Please select format..")
                    self.result_message_label.setStyleSheet("color: orange")
                    self.result_message_label.setVisible(True)

                else:
                    set_layout_or_widget_visible(self.would_you_layout, False)
                    self.result_message_label.setVisible(True)

        except (ValueError, AttributeError):
            self.result_message_label.setText("Invalid starting number..")
            self.result_message_label.setStyleSheet("color: #f53b3b")
            self.result_message_label.setVisible(True)
            set_layout_or_widget_visible(self.would_you_layout, False)

    # Combinational Submit Button Clicked
    def comb_submit_clicked(self):
        # Check checkboxes
        if self.addprefix_checkBox.isChecked():
            prefix_text = self.Add_prefix_label.text()
            invalid_chars = ["#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "$", "!", "'", "\"", ":", "@", "+",
                             "`", "|", "="]
            self.invalid_pre_name = False
            for i in prefix_text:
                if i in invalid_chars:
                    self.invalid_pre_name = True
            if self.invalid_pre_name:
                self.result_message_label.setText("Invalid character for a file name..")
                self.result_message_label.setStyleSheet("color: red")
                set_layout_or_widget_visible(self.would_you_layout, False)
                self.result_message_label.setVisible(True)
            else:
                self.des_name = prefix_text
                self.result_message_label.setVisible(False)

        else:
            self.des_name = ""

        if self.addsuffix_checkBox.isChecked():
            suffix_text = self.add_suffix_label.text()
            invalid_chars = ["#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "$", "!", "'", "\"", ":", "@", "+",
                             "`", "|", "="]
            self.invalid_suf_name = False
            for i in suffix_text:
                if i in invalid_chars:
                    self.invalid_suf_name = True
            if self.invalid_suf_name:
                self.result_message_label.setText("Invalid character for a file name..")
                self.result_message_label.setStyleSheet("color: red")
                self.result_message_label.setVisible(True)
            else:
                self.des_ext = suffix_text
                self.result_message_label.setVisible(False)

        if self.change_ext_checkBox.isChecked():
            ext_text = self.add_suffix_label_2.text()
            invalid_chars = ["#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "$", "!", "'", "\"", ":", "@", "+",
                             "`", "|", "="]
            self.invalid_ext_name_2 = False
            for i in ext_text:
                if i in invalid_chars:
                    self.invalid_ext_name_2 = True
            if self.invalid_suf_name:
                self.result_message_label.setText("Invalid character for an extension name..")
                self.result_message_label.setStyleSheet("color: red")
                self.result_message_label.setVisible(True)
            else:
                self.selections_list = ext_text
                self.result_message_label.setVisible(False)

        if not (self.invalid_suf_name or self.invalid_pre_name or self.invalid_ext_name_2):
            set_layout_or_widget_visible(self.would_you_layout, True)
            self.rename_all_radio.setChecked(True)
            self.rename_specific_radio.setChecked(False)
            set_layout_or_widget_visible(self.enter_startwith_label, False)
            self.seq = False
        else:
            self.result_message_label.setVisible(True)


    # Final submit button
    def main_submit(self):
        # Check radio buttons
        if self.rename_all_radio.isChecked():
            self.filter_ = ""
        else:
            self.filter_ = self.enter_startwith_label.text()

        # Check path
        if self.path != "":
            # Do automation process
            out_text, color = rename_files(self.path, self.des_name, self.des_ext, self.selections_list, self.filter_,
                                           self.start, self.seq)
            self.result_message_label.setText(out_text)
            self.result_message_label.setStyleSheet(f"color: {color}")
            self.result_message_label.setVisible(True)
            # Open folder
            os.startfile(self.path)

        else:
            self.result_message_label.setText("Please select a folder..")
            self.result_message_label.setStyleSheet(f"color: red")
            self.result_message_label.setVisible(True)


    # When all files radio button clicked
    def all_radio(self):
        set_layout_or_widget_visible(self.enter_startwith_label, False)

    # When specific files radio button clicked
    def specific_radio(self):
        set_layout_or_widget_visible(self.enter_startwith_label, True)


# Hide / Show Layout or Widget
def set_layout_or_widget_visible(item, visible):
    if isinstance(item,QtWidgets.QLayout):
        # If item is a layout, hide or show all widgets inside it
        for i in range(item.count()):
            sub_item = item.itemAt(i)
            if sub_item is not None:
                widget = sub_item.widget()
                if widget is not None:
                    widget.setVisible(visible)
                else:
                    sub_layout = sub_item.layout()
                    if sub_layout is not None:
                        set_layout_or_widget_visible(sub_layout, visible)
    elif isinstance(item, QtWidgets.QWidget):
        # If item is a widget, hide or show it
        item.setVisible(visible)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
