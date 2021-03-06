# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heinsight_applications_gui_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 571)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.title_widget = QtWidgets.QWidget(self.centralwidget)
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.title_widget.setObjectName("title_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.title_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Heinsight_title = QtWidgets.QLabel(self.title_widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Heinsight_title.setFont(font)
        self.Heinsight_title.setText("HeinSight - Liquid level")
        self.Heinsight_title.setOpenExternalLinks(False)
        self.Heinsight_title.setObjectName("Heinsight_title")
        self.verticalLayout_3.addWidget(self.Heinsight_title)
        self.subtitle1 = QtWidgets.QLabel(self.title_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.subtitle1.setFont(font)
        self.subtitle1.setObjectName("subtitle1")
        self.verticalLayout_3.addWidget(self.subtitle1)
        self.horizontalLayout_7.addWidget(self.title_widget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.SetupTab = QtWidgets.QWidget()
        self.SetupTab.setObjectName("SetupTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.SetupTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.SetupTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 455))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.General_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.General_groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.General_groupBox.setObjectName("General_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.General_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.directory_to_save_experiment_to_LineEdit = QtWidgets.QLineEdit(self.General_groupBox)
        self.directory_to_save_experiment_to_LineEdit.setMaximumSize(QtCore.QSize(16777215, 75))
        self.directory_to_save_experiment_to_LineEdit.setObjectName("directory_to_save_experiment_to_LineEdit")
        self.gridLayout.addWidget(self.directory_to_save_experiment_to_LineEdit, 0, 1, 1, 1)
        self.ExpName_entry = QtWidgets.QLineEdit(self.General_groupBox)
        self.ExpName_entry.setObjectName("ExpName_entry")
        self.gridLayout.addWidget(self.ExpName_entry, 1, 1, 1, 1)
        self.directory_to_save_experiment_to_label = QtWidgets.QLabel(self.General_groupBox)
        self.directory_to_save_experiment_to_label.setWordWrap(False)
        self.directory_to_save_experiment_to_label.setObjectName("directory_to_save_experiment_to_label")
        self.gridLayout.addWidget(self.directory_to_save_experiment_to_label, 0, 0, 1, 1)
        self.directory_to_save_experiment_to_browse_button = QtWidgets.QPushButton(self.General_groupBox)
        self.directory_to_save_experiment_to_browse_button.setObjectName("directory_to_save_experiment_to_browse_button")
        self.gridLayout.addWidget(self.directory_to_save_experiment_to_browse_button, 0, 2, 1, 1)
        self.ExpName_label = QtWidgets.QLabel(self.General_groupBox)
        self.ExpName_label.setObjectName("ExpName_label")
        self.gridLayout.addWidget(self.ExpName_label, 1, 0, 1, 1)
        self.ExpType_label_2 = QtWidgets.QLabel(self.General_groupBox)
        self.ExpType_label_2.setObjectName("ExpType_label_2")
        self.gridLayout.addWidget(self.ExpType_label_2, 2, 0, 1, 1)
        self.experiment_type_comboBox = QtWidgets.QComboBox(self.General_groupBox)
        self.experiment_type_comboBox.setObjectName("experiment_type_comboBox")
        self.experiment_type_comboBox.addItem("")
        self.experiment_type_comboBox.addItem("")
        self.experiment_type_comboBox.addItem("")
        self.experiment_type_comboBox.addItem("")
        self.gridLayout.addWidget(self.experiment_type_comboBox, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.General_groupBox)
        self.Peripherals_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.Peripherals_groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Peripherals_groupBox.setObjectName("Peripherals_groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Peripherals_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pump_two_port_lineEdit = QtWidgets.QLineEdit(self.Peripherals_groupBox)
        self.pump_two_port_lineEdit.setReadOnly(False)
        self.pump_two_port_lineEdit.setObjectName("pump_two_port_lineEdit")
        self.gridLayout_6.addWidget(self.pump_two_port_lineEdit, 2, 1, 1, 1)
        self.CamPort_Label = QtWidgets.QLabel(self.Peripherals_groupBox)
        self.CamPort_Label.setObjectName("CamPort_Label")
        self.gridLayout_6.addWidget(self.CamPort_Label, 0, 0, 1, 1)
        self.slack_integration_json_browse_button = QtWidgets.QPushButton(self.Peripherals_groupBox)
        self.slack_integration_json_browse_button.setObjectName("slack_integration_json_browse_button")
        self.gridLayout_6.addWidget(self.slack_integration_json_browse_button, 5, 2, 1, 1)
        self.CamPort_SpinBox = QtWidgets.QSpinBox(self.Peripherals_groupBox)
        self.CamPort_SpinBox.setProperty("value", 0)
        self.CamPort_SpinBox.setObjectName("CamPort_SpinBox")
        self.gridLayout_6.addWidget(self.CamPort_SpinBox, 0, 1, 1, 1)
        self.pump_one_port_label = QtWidgets.QLabel(self.Peripherals_groupBox)
        self.pump_one_port_label.setWordWrap(False)
        self.pump_one_port_label.setObjectName("pump_one_port_label")
        self.gridLayout_6.addWidget(self.pump_one_port_label, 1, 0, 1, 1)
        self.pump_one_port_lineEdit = QtWidgets.QLineEdit(self.Peripherals_groupBox)
        self.pump_one_port_lineEdit.setText("")
        self.pump_one_port_lineEdit.setObjectName("pump_one_port_lineEdit")
        self.gridLayout_6.addWidget(self.pump_one_port_lineEdit, 1, 1, 1, 1)
        self.pump_two_port_label = QtWidgets.QLabel(self.Peripherals_groupBox)
        self.pump_two_port_label.setWordWrap(False)
        self.pump_two_port_label.setObjectName("pump_two_port_label")
        self.gridLayout_6.addWidget(self.pump_two_port_label, 2, 0, 1, 1)
        self.slack_integration_json_lineEdit = QtWidgets.QLineEdit(self.Peripherals_groupBox)
        self.slack_integration_json_lineEdit.setObjectName("slack_integration_json_lineEdit")
        self.gridLayout_6.addWidget(self.slack_integration_json_lineEdit, 5, 1, 1, 1)
        self.slack_integration_json_label = QtWidgets.QLabel(self.Peripherals_groupBox)
        self.slack_integration_json_label.setObjectName("slack_integration_json_label")
        self.gridLayout_6.addWidget(self.slack_integration_json_label, 5, 0, 1, 1)
        self.pump_rate_SpinBox = QtWidgets.QDoubleSpinBox(self.Peripherals_groupBox)
        self.pump_rate_SpinBox.setMaximum(800.0)
        self.pump_rate_SpinBox.setProperty("value", 5.0)
        self.pump_rate_SpinBox.setObjectName("pump_rate_SpinBox")
        self.gridLayout_6.addWidget(self.pump_rate_SpinBox, 3, 1, 1, 1)
        self.pump_rate_Label = QtWidgets.QLabel(self.Peripherals_groupBox)
        self.pump_rate_Label.setObjectName("pump_rate_Label")
        self.gridLayout_6.addWidget(self.pump_rate_Label, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.Peripherals_groupBox)
        self.system_specifics_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.system_specifics_groupBox.setObjectName("system_specifics_groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.system_specifics_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.try_tracker_max_number_of_tries_label_spinBox = QtWidgets.QSpinBox(self.system_specifics_groupBox)
        self.try_tracker_max_number_of_tries_label_spinBox.setSingleStep(1)
        self.try_tracker_max_number_of_tries_label_spinBox.setProperty("value", 5)
        self.try_tracker_max_number_of_tries_label_spinBox.setObjectName("try_tracker_max_number_of_tries_label_spinBox")
        self.gridLayout_7.addWidget(self.try_tracker_max_number_of_tries_label_spinBox, 3, 1, 1, 1)
        self.self_correction_pump_rate_spinBox = QtWidgets.QDoubleSpinBox(self.system_specifics_groupBox)
        self.self_correction_pump_rate_spinBox.setMaximum(800.0)
        self.self_correction_pump_rate_spinBox.setProperty("value", 5.0)
        self.self_correction_pump_rate_spinBox.setObjectName("self_correction_pump_rate_spinBox")
        self.gridLayout_7.addWidget(self.self_correction_pump_rate_spinBox, 2, 1, 1, 1)
        self.self_correction_pump_rate_label = QtWidgets.QLabel(self.system_specifics_groupBox)
        self.self_correction_pump_rate_label.setWordWrap(False)
        self.self_correction_pump_rate_label.setObjectName("self_correction_pump_rate_label")
        self.gridLayout_7.addWidget(self.self_correction_pump_rate_label, 2, 0, 1, 1)
        self.time_to_self_correct_label = QtWidgets.QLabel(self.system_specifics_groupBox)
        self.time_to_self_correct_label.setWordWrap(True)
        self.time_to_self_correct_label.setObjectName("time_to_self_correct_label")
        self.gridLayout_7.addWidget(self.time_to_self_correct_label, 0, 0, 1, 1)
        self.number_of_monitor_liquid_level_replicate_measurements_spinBox = QtWidgets.QSpinBox(self.system_specifics_groupBox)
        self.number_of_monitor_liquid_level_replicate_measurements_spinBox.setSingleStep(2)
        self.number_of_monitor_liquid_level_replicate_measurements_spinBox.setProperty("value", 5)
        self.number_of_monitor_liquid_level_replicate_measurements_spinBox.setObjectName("number_of_monitor_liquid_level_replicate_measurements_spinBox")
        self.gridLayout_7.addWidget(self.number_of_monitor_liquid_level_replicate_measurements_spinBox, 4, 1, 1, 1)
        self.advance_time_label = QtWidgets.QLabel(self.system_specifics_groupBox)
        self.advance_time_label.setWordWrap(True)
        self.advance_time_label.setObjectName("advance_time_label")
        self.gridLayout_7.addWidget(self.advance_time_label, 5, 0, 1, 1)
        self.number_of_monitor_liquid_level_replicate_measurements_label = QtWidgets.QLabel(self.system_specifics_groupBox)
        self.number_of_monitor_liquid_level_replicate_measurements_label.setWordWrap(True)
        self.number_of_monitor_liquid_level_replicate_measurements_label.setObjectName("number_of_monitor_liquid_level_replicate_measurements_label")
        self.gridLayout_7.addWidget(self.number_of_monitor_liquid_level_replicate_measurements_label, 4, 0, 1, 1)
        self.advance_time_spinBox = QtWidgets.QSpinBox(self.system_specifics_groupBox)
        self.advance_time_spinBox.setMaximum(200)
        self.advance_time_spinBox.setProperty("value", 5)
        self.advance_time_spinBox.setObjectName("advance_time_spinBox")
        self.gridLayout_7.addWidget(self.advance_time_spinBox, 5, 1, 1, 1)
        self.try_tracker_max_number_of_tries_label = QtWidgets.QLabel(self.system_specifics_groupBox)
        self.try_tracker_max_number_of_tries_label.setWordWrap(True)
        self.try_tracker_max_number_of_tries_label.setObjectName("try_tracker_max_number_of_tries_label")
        self.gridLayout_7.addWidget(self.try_tracker_max_number_of_tries_label, 3, 0, 1, 1)
        self.time_to_self_correct_spinBox = QtWidgets.QSpinBox(self.system_specifics_groupBox)
        self.time_to_self_correct_spinBox.setEnabled(True)
        self.time_to_self_correct_spinBox.setMaximum(200)
        self.time_to_self_correct_spinBox.setProperty("value", 10)
        self.time_to_self_correct_spinBox.setObjectName("time_to_self_correct_spinBox")
        self.gridLayout_7.addWidget(self.time_to_self_correct_spinBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.system_specifics_groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.SetupTab, "")
        self.Run = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setKerning(False)
        self.Run.setFont(font)
        self.Run.setObjectName("Run")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Run)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Run)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 479, 311))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.initialize_experiment_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        self.initialize_experiment_button.setObjectName("initialize_experiment_button")
        self.verticalLayout_2.addWidget(self.initialize_experiment_button)
        self.webcam_stream_pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        self.webcam_stream_pushButton.setObjectName("webcam_stream_pushButton")
        self.verticalLayout_2.addWidget(self.webcam_stream_pushButton)
        self.pump_control_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_8)
        self.pump_control_groupBox.setObjectName("pump_control_groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pump_control_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.pump_control_groupBox)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.pump_direction_label = QtWidgets.QLabel(self.pump_control_groupBox)
        self.pump_direction_label.setObjectName("pump_direction_label")
        self.gridLayout_4.addWidget(self.pump_direction_label, 0, 0, 1, 1)
        self.dispense_radioButton = QtWidgets.QRadioButton(self.pump_control_groupBox)
        self.dispense_radioButton.setChecked(True)
        self.dispense_radioButton.setObjectName("dispense_radioButton")
        self.gridLayout_4.addWidget(self.dispense_radioButton, 0, 1, 1, 1)
        self.withdraw_radioButton = QtWidgets.QRadioButton(self.pump_control_groupBox)
        self.withdraw_radioButton.setObjectName("withdraw_radioButton")
        self.gridLayout_4.addWidget(self.withdraw_radioButton, 0, 2, 1, 1)
        self.pump_time_spinBox = QtWidgets.QSpinBox(self.pump_control_groupBox)
        self.pump_time_spinBox.setMaximum(200)
        self.pump_time_spinBox.setProperty("value", 5)
        self.pump_time_spinBox.setObjectName("pump_time_spinBox")
        self.gridLayout_4.addWidget(self.pump_time_spinBox, 1, 1, 1, 2)
        self.pump_pushButton = QtWidgets.QPushButton(self.pump_control_groupBox)
        self.pump_pushButton.setObjectName("pump_pushButton")
        self.gridLayout_4.addWidget(self.pump_pushButton, 2, 0, 1, 3)
        self.verticalLayout_2.addWidget(self.pump_control_groupBox)
        self.start_experiment_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        self.start_experiment_Button.setObjectName("start_experiment_Button")
        self.verticalLayout_2.addWidget(self.start_experiment_Button)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.Run, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuAbout.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HeinSight liquid level"))
        self.subtitle1.setText(_translate("MainWindow", "Automated liquid level control for chemistry"))
        self.General_groupBox.setTitle(_translate("MainWindow", "General"))
        self.directory_to_save_experiment_to_label.setText(_translate("MainWindow", "Experiment directory"))
        self.directory_to_save_experiment_to_browse_button.setText(_translate("MainWindow", "Browse..."))
        self.ExpName_label.setText(_translate("MainWindow", "Experiment name"))
        self.ExpType_label_2.setText(_translate("MainWindow", "Experiment type"))
        self.experiment_type_comboBox.setItemText(0, _translate("MainWindow", "Single pump CPC"))
        self.experiment_type_comboBox.setItemText(1, _translate("MainWindow", "Dual pump CPC"))
        self.experiment_type_comboBox.setItemText(2, _translate("MainWindow", "Continuous distillation"))
        self.experiment_type_comboBox.setItemText(3, _translate("MainWindow", "Filtration"))
        self.Peripherals_groupBox.setTitle(_translate("MainWindow", "Peripherals"))
        self.CamPort_Label.setText(_translate("MainWindow", "Camera port"))
        self.slack_integration_json_browse_button.setText(_translate("MainWindow", "Browse..."))
        self.pump_one_port_label.setText(_translate("MainWindow", "Pump 1 port"))
        self.pump_two_port_label.setText(_translate("MainWindow", "Pump 2 port"))
        self.slack_integration_json_label.setText(_translate("MainWindow", "Slack integration JSON"))
        self.pump_rate_Label.setText(_translate("MainWindow", "Pump rate (mL/min)"))
        self.system_specifics_groupBox.setTitle(_translate("MainWindow", "System Specifics"))
        self.self_correction_pump_rate_label.setText(_translate("MainWindow", "Liquid level correction pump rate (mL/min)"))
        self.time_to_self_correct_label.setText(_translate("MainWindow", "Liquid level correction time (sec)"))
        self.advance_time_label.setText(_translate("MainWindow", "System advance time (sec)"))
        self.number_of_monitor_liquid_level_replicate_measurements_label.setText(_translate("MainWindow", "No. of replicate measurements"))
        self.try_tracker_max_number_of_tries_label.setText(_translate("MainWindow", "Try tracker max. no. of times"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SetupTab), _translate("MainWindow", "Set-Up"))
        self.initialize_experiment_button.setText(_translate("MainWindow", "Initialize"))
        self.webcam_stream_pushButton.setText(_translate("MainWindow", "Webcam stream"))
        self.pump_control_groupBox.setTitle(_translate("MainWindow", "Pump control"))
        self.label.setText(_translate("MainWindow", "Pump time:"))
        self.pump_direction_label.setText(_translate("MainWindow", "Pump direction:"))
        self.dispense_radioButton.setText(_translate("MainWindow", "Dispense"))
        self.withdraw_radioButton.setText(_translate("MainWindow", "Withdraw"))
        self.pump_pushButton.setText(_translate("MainWindow", "Pump"))
        self.start_experiment_Button.setText(_translate("MainWindow", "Start experiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Run), _translate("MainWindow", "Run"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
