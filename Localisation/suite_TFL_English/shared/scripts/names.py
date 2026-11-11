# encoding: UTF-8

from objectmaphelper import *

apollo_AlarmsListScreen_AlarmsListScreen = {"name": "AlarmsListScreen", "type": "AlarmsListScreen", "visible": 1, "window": apollo_MainWindow}
alarmsListScreen_frmPopup_AlarmNotificationPopup = {"container": apollo_AlarmsListScreen_AlarmsListScreen, "name": "frmPopup", "type": "AlarmNotificationPopup", "visible": 1}
frmPopup_pbAccept_QPushButton = {"container": alarmsListScreen_frmPopup_AlarmNotificationPopup, "name": "pbAccept", "type": "QPushButton", "visible": 1}
apollo_PasswordScreen_PasswordScreen = {"name": "PasswordScreen", "type": "PasswordScreen", "visible": 1, "window": apollo_MainWindow}
passwordScreen_wdKeypad_Keypad = {"container": apollo_PasswordScreen_PasswordScreen, "name": "wdKeypad", "type": "Keypad", "visible": 1}
wdKeypad_pushButton_0_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_0", "type": "QPushButton", "visible": 1}
apollo_sclProfiles_ProfilesScroll = {"name": "sclProfiles", "type": "ProfilesScroll", "visible": 1, "window": apollo_MainWindow}
sclProfiles_Default_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "Default", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_centralWidget_QStackedWidget = {"name": "centralWidget", "type": "QStackedWidget", "visible": 1, "window": apollo_MainWindow}
centralWidget_comboBox_ComboBox = {"container": apollo_centralWidget_QStackedWidget, "name": "comboBox", "type": "ComboBox", "visible": 1}
comboBox_lbValue_AutoReducibleFontSizeLabel = {"container": centralWidget_comboBox_ComboBox, "name": "lbValue", "type": "AutoReducibleFontSizeLabel", "visible": 1}
apollo_frmComboBoxHeader_ComboBoxTwin = {"name": "frmComboBoxHeader", "type": "ComboBoxTwin", "visible": 1, "window": apollo_MainWindow}
frmComboBoxHeader_lbValue_AutoReducibleFontSizeLabel = {"container": apollo_frmComboBoxHeader_ComboBoxTwin, "name": "lbValue", "type": "AutoReducibleFontSizeLabel", "visible": 1}
apollo_btSettings_QPushButton = {"name": "btSettings", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_centralWidget_QFrame = {"name": "centralWidget", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
centralWidget_frmComboBox_QFrame = {"container": apollo_centralWidget_QFrame, "name": "frmComboBox", "type": "QFrame", "visible": 1}
frmComboBox_cbLang_QComboBox = {"container": centralWidget_frmComboBox_QFrame, "name": "cbLang", "type": "QComboBox", "visible": 1}
frmPopup_lbTitle_QLabel = {"container": alarmsListScreen_frmPopup_AlarmNotificationPopup, "name": "lbTitle", "type": "QLabel", "visible": 1}
wdKeypad_pushButton_8_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_8", "type": "QPushButton", "visible": 1}
apollo_lbProfileTitle_QLabel = {"name": "lbProfileTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbProfileName_QLabel = {"name": "lbProfileName", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbLasingTimeTitle_QLabel = {"name": "lbLasingTimeTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbTotalEnergyTitle_QLabel = {"name": "lbTotalEnergyTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbFiberDiameterTitle_QLabel = {"name": "lbFiberDiameterTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbUsesLeftTitle_QLabel = {"name": "lbUsesLeftTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbExpirationTitle_QLabel = {"name": "lbExpirationTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_stateSwitch_StateSwitch = {"name": "stateSwitch", "type": "StateSwitch", "visible": 1, "window": apollo_MainWindow}
stateSwitch_lbStandby_QLabel = {"container": apollo_stateSwitch_StateSwitch, "name": "lbStandby", "type": "QLabel", "visible": 1}
apollo_btHome_QPushButton = {"name": "btHome", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
centralWidget_PulseModeWidget_PulseModeWidget = {"container": apollo_centralWidget_QStackedWidget, "name": "PulseModeWidget", "type": "PulseModeWidget", "visible": 1}
