# encoding: UTF-8

from objectmaphelper import *

apollo_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Apollo"}
apollo_AlarmsListScreen_AlarmsListScreen = {"name": "AlarmsListScreen", "type": "AlarmsListScreen", "visible": 1, "window": apollo_MainWindow}
alarmsListScreen_frmPopup_AlarmNotificationPopup = {"container": apollo_AlarmsListScreen_AlarmsListScreen, "name": "frmPopup", "type": "AlarmNotificationPopup", "visible": 1}
frmPopup_pbAccept_QPushButton = {"container": alarmsListScreen_frmPopup_AlarmNotificationPopup, "name": "pbAccept", "type": "QPushButton", "visible": 1}
apollo_PasswordScreen_PasswordScreen = {"name": "PasswordScreen", "type": "PasswordScreen", "visible": 1, "window": apollo_MainWindow}
passwordScreen_wdKeypad_Keypad = {"container": apollo_PasswordScreen_PasswordScreen, "name": "wdKeypad", "type": "Keypad", "visible": 1}
wdKeypad_pushButton_0_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_0", "type": "QPushButton", "visible": 1}
apollo_ProfileSelectionScreen_ProfileSelectionScreen = {"name": "ProfileSelectionScreen", "type": "ProfileSelectionScreen", "visible": 1, "window": apollo_MainWindow}
apollo_sclProfiles_ProfilesScroll = {"name": "sclProfiles", "type": "ProfilesScroll", "visible": 1, "window": apollo_MainWindow}
sclProfiles_Default_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "Default", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_btSettings_QPushButton = {"name": "btSettings", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_centralWidget_QFrame = {"name": "centralWidget", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
centralWidget_frmComboBox_QFrame = {"container": apollo_centralWidget_QFrame, "name": "frmComboBox", "type": "QFrame", "visible": 1}
frmComboBox_cbLang_QComboBox = {"container": centralWidget_frmComboBox_QFrame, "name": "cbLang", "type": "QComboBox", "visible": 1}
apollo_btHome_QPushButton = {"name": "btHome", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_btExitProfile_QPushButton = {"name": "btExitProfile", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_Question_MessageBox = {"name": "Question", "type": "MessageBox", "visible": 1, "window": apollo_MainWindow}
question_QPushButton = {"container": apollo_Question_MessageBox, "text": "ДА", "type": "QPushButton", "unnamed": 1, "visible": 1}
apollo_lbTitle_QLabel = {"name": "lbTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
sclProfiles_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "По подразбиране", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_lbProfileTitle_QLabel = {"name": "lbProfileTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbProfileName_QLabel = {"name": "lbProfileName", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbLasingTimeTitle_QLabel = {"name": "lbLasingTimeTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbTotalEnergyTitle_QLabel = {"name": "lbTotalEnergyTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbFiberDiameterTitle_QLabel = {"name": "lbFiberDiameterTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbUsesLeftTitle_QLabel = {"name": "lbUsesLeftTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbExpirationTitle_QLabel = {"name": "lbExpirationTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_frToolbar_QFrame = {"name": "frToolbar", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
frToolbar_tbAddProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbAddProfile", "type": "QToolButton", "visible": 1}
apollo_keyboardFrame_QFrame = {"name": "keyboardFrame", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
keyboardFrame_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "т", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_e_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "e", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_KeyButton = {"container": apollo_keyboardFrame_QFrame, "text": "⌫", "type": "KeyButton", "unnamed": 1, "visible": 1}
keyboardFrame_123_KeyButtonNumSwitch = {"container": apollo_keyboardFrame_QFrame, "text": "&123\nЧисла", "type": "KeyButtonNumSwitch", "unnamed": 1, "visible": 1}
keyboardFrame_1_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 1, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_2_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 2, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_3_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 3, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_4_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 4, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_5_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 5, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_Enter_KeyButtonEnter = {"container": apollo_keyboardFrame_QFrame, "text": "Enter", "type": "KeyButtonEnter", "unnamed": 1, "visible": 1}
frToolbar_tbEditProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbEditProfile", "type": "QToolButton", "visible": 1}
sclProfiles_12345_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 12345, "type": "ProfileButton", "unnamed": 1, "visible": 1}
keyboardFrame_6_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 6, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_7_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 7, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_8_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 8, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_9_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 9, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
frToolbar_tbDeleteProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbDeleteProfile", "type": "QToolButton", "visible": 1}
sclProfiles_123456789_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 123456789, "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_MessageBoxBackground = {"type": "MessageBoxBackground", "unnamed": 1, "visible": 1, "window": apollo_MainWindow}
question_OK_QPushButton = {"container": apollo_Question_MessageBox, "text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1}
question_TextLabel_QLabel = {"container": apollo_Question_MessageBox, "name": "TextLabel", "type": "QLabel", "visible": 1}
question_QPushButton_2 = {"container": apollo_Question_MessageBox, "text": "ОТКАЗ", "type": "QPushButton", "unnamed": 1, "visible": 1}
apollo_btTreatmentLogs_QPushButton = {"name": "btTreatmentLogs", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_lbExpirationDate_QLabel = {"name": "lbExpirationDate", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbHeader_QLabel = {"name": "lbHeader", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_frmTable_QFrame = {"name": "frmTable", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
frmTable_frmHeader_QFrame = {"container": apollo_frmTable_QFrame, "name": "frmHeader", "type": "QFrame", "visible": 1}
frmHeader_lbDate_QLabel = {"container": frmTable_frmHeader_QFrame, "name": "lbDate", "type": "QLabel", "visible": 1}
frmHeader_lbTime_QLabel = {"container": frmTable_frmHeader_QFrame, "name": "lbTime", "type": "QLabel", "visible": 1}
frmHeader_lbLasingTime_QLabel = {"container": frmTable_frmHeader_QFrame, "name": "lbLasingTime", "type": "QLabel", "visible": 1}
frmHeader_lbTotal_QLabel = {"container": frmTable_frmHeader_QFrame, "name": "lbTotal", "type": "QLabel", "visible": 1}
frmHeader_lbFiber_QLabel = {"container": frmTable_frmHeader_QFrame, "name": "lbFiber", "type": "QLabel", "visible": 1}
apollo_btUtilities_QPushButton = {"name": "btUtilities", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_stackedWidget_QStackedWidget = {"name": "stackedWidget", "type": "QStackedWidget", "visible": 1, "window": apollo_MainWindow}
stackedWidget_systemInformationPage_QFrame = {"container": apollo_stackedWidget_QStackedWidget, "name": "systemInformationPage", "type": "QFrame", "visible": 1}
systemInformationPage_label_2_QLabel = {"container": stackedWidget_systemInformationPage_QFrame, "name": "label_2", "type": "QLabel", "visible": 1}
systemInformationPage_label_3_QLabel = {"container": stackedWidget_systemInformationPage_QFrame, "name": "label_3", "type": "QLabel", "visible": 1}
systemInformationPage_label_QLabel = {"container": stackedWidget_systemInformationPage_QFrame, "name": "label", "type": "QLabel", "visible": 1}
sclProfiles_scrollAreaWidgetContents_QWidget = {"container": apollo_sclProfiles_ProfilesScroll, "name": "scrollAreaWidgetContents", "type": "QWidget", "visible": 1}
apollo_lbModeHelp_QLabel = {"name": "lbModeHelp", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
sclProfiles_123_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 123, "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_frmHeader_QFrame = {"name": "frmHeader", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
frmHeader_rbErrorLogs_QRadioButton = {"container": apollo_frmHeader_QFrame, "name": "rbErrorLogs", "type": "QRadioButton", "visible": 1}
frmHeader_rbFiberInfo_QRadioButton = {"container": apollo_frmHeader_QFrame, "name": "rbFiberInfo", "type": "QRadioButton", "visible": 1}
stackedWidget_stackedWidget_QStackedWidget = {"container": apollo_stackedWidget_QStackedWidget, "name": "stackedWidget", "type": "QStackedWidget", "visible": 1}
stackedWidget_lbDiameterTitle_QLabel = {"container": stackedWidget_stackedWidget_QStackedWidget, "name": "lbDiameterTitle", "type": "QLabel", "visible": 1}
stackedWidget_lbMaximumPowerTitle_QLabel = {"container": stackedWidget_stackedWidget_QStackedWidget, "name": "lbMaximumPowerTitle", "type": "QLabel", "visible": 1}
stackedWidget_lbUsesReminingTitle_QLabel = {"container": stackedWidget_stackedWidget_QStackedWidget, "name": "lbUsesReminingTitle", "type": "QLabel", "visible": 1}
stackedWidget_lbSerialNumberTitle_QLabel = {"container": stackedWidget_stackedWidget_QStackedWidget, "name": "lbSerialNumberTitle", "type": "QLabel", "visible": 1}
stackedWidget_lbExpirationDateTitle_QLabel = {"container": stackedWidget_stackedWidget_QStackedWidget, "name": "lbExpirationDateTitle", "type": "QLabel", "visible": 1}
stackedWidget_errorLogsPage_QFrame = {"container": apollo_stackedWidget_QStackedWidget, "name": "errorLogsPage", "type": "QFrame", "visible": 1}
treatmentLogs_pbDownload_QPushButton = {"name": "pbDownload", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
errorLogsPage_pbDownload_QPushButton = {"container": stackedWidget_errorLogsPage_QFrame, "name": "pbDownload", "type": "QPushButton", "visible": 1}
errorLogsPage_tvErrorLog_QTreeView = {"container": stackedWidget_errorLogsPage_QFrame, "name": "tvErrorLog", "type": "QTreeView", "visible": 1}
tvErrorLog_QHeaderView = {"container": errorLogsPage_tvErrorLog_QTreeView, "orientation": 1, "type": "QHeaderView", "unnamed": 1, "visible": 1}
o_HeaderViewItem = {"container": tvErrorLog_QHeaderView, "text": "ЧАС/ДАТА", "type": "HeaderViewItem", "visible": True}
o_HeaderViewItem_2 = {"container": tvErrorLog_QHeaderView, "text": "РЕГИСТРИ ЗА ГРЕШКИ", "type": "HeaderViewItem", "visible": True}
o_HeaderViewItem_3 = {"container": tvErrorLog_QHeaderView, "text": "ОПИСАНИЕ НА ГРЕШКА", "type": "HeaderViewItem", "visible": True}
apollo_btPresets_QPushButton = {"name": "btPresets", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_lbScreenTitle_QLabel = {"name": "lbScreenTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_tvPresets_PresetsTable = {"name": "tvPresets", "type": "PresetsTable", "visible": 1, "window": apollo_MainWindow}
tvPresets_QHeaderView = {"container": apollo_tvPresets_PresetsTable, "orientation": 1, "type": "QHeaderView", "unnamed": 1, "visible": 1}
o_HeaderViewItem_4 = {"container": tvPresets_QHeaderView, "text": "ИМЕ НА ПРЕДВАРИТЕЛНА НАСТРОЙКА", "type": "HeaderViewItem", "visible": True}
o_HeaderViewItem_5 = {"container": tvPresets_QHeaderView, "text": "ЕНЕРГИЯ", "type": "HeaderViewItem", "visible": True}
o_HeaderViewItem_6 = {"container": tvPresets_QHeaderView, "text": "ЧЕСТОТА", "type": "HeaderViewItem", "visible": True}
o_HeaderViewItem_7 = {"container": tvPresets_QHeaderView, "text": "МОЩНОСТ", "type": "HeaderViewItem", "visible": True}
o_HeaderViewItem_8 = {"container": tvPresets_QHeaderView, "text": "ШИРИНА НА ИМПУЛСА", "type": "HeaderViewItem", "visible": True}
centralWidget_lbLang_QLabel = {"container": apollo_centralWidget_QFrame, "name": "lbLang", "type": "QLabel", "visible": 1}
centralWidget_lbVolume_QLabel = {"container": apollo_centralWidget_QFrame, "name": "lbVolume", "type": "QLabel", "visible": 1}
centralWidget_lbBrightness_QLabel = {"container": apollo_centralWidget_QFrame, "name": "lbBrightness", "type": "QLabel", "visible": 1}
apollo_centralWidget_QStackedWidget = {"name": "centralWidget", "type": "QStackedWidget", "visible": 1, "window": apollo_MainWindow}
centralWidget_lbHeader_QLabel = {"container": apollo_centralWidget_QStackedWidget, "name": "lbHeader", "occurrence": 2, "type": "QLabel", "visible": 1}
centralWidget_lbPower_QLabel = {"container": apollo_centralWidget_QStackedWidget, "name": "lbPower", "type": "QLabel", "visible": 1}
centralWidget_pbPulsedMode_QToolButton = {"container": apollo_centralWidget_QStackedWidget, "name": "pbPulsedMode", "type": "QToolButton", "visible": 1}
centralWidget_pbCwMode_QToolButton = {"container": apollo_centralWidget_QStackedWidget, "name": "pbCwMode", "type": "QToolButton", "visible": 1}
centralWidget_lbDualPulse_QLabel = {"container": apollo_centralWidget_QStackedWidget, "name": "lbDualPulse", "type": "QLabel", "visible": 1}
centralWidget_lbPulseWidth_QLabel = {"container": apollo_centralWidget_QStackedWidget, "name": "lbPulseWidth", "type": "QLabel", "visible": 1}
centralWidget_PulseModeWidget_PulseModeWidget = {"container": apollo_centralWidget_QStackedWidget, "name": "PulseModeWidget", "type": "PulseModeWidget", "visible": 1}
apollo_stateSwitch_StateSwitch = {"name": "stateSwitch", "type": "StateSwitch", "visible": 1, "window": apollo_MainWindow}
stateSwitch_lbStandby_QLabel = {"container": apollo_stateSwitch_StateSwitch, "name": "lbStandby", "type": "QLabel", "visible": 1}
stateSwitch_lbReady_QLabel = {"container": apollo_stateSwitch_StateSwitch, "name": "lbReady", "type": "QLabel", "visible": 1}
centralWidget_pbCwMode_QToolButton_2 = {"container": apollo_centralWidget_QStackedWidget, "name": "pbCwMode", "occurrence": 2, "type": "QToolButton", "visible": 1}
question_QPushButton_3 = {"container": apollo_Question_MessageBox, "text": "НЕ", "type": "QPushButton", "unnamed": 1, "visible": 1}
frToolbar_tbAddPreset_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbAddPreset", "type": "QToolButton", "visible": 1}
apollo_lbScreenTitle_QLabel_2 = {"name": "lbScreenTitle", "occurrence": 2, "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_lbName_QLabel = {"name": "lbName", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_pagesWidget_QStackedWidget = {"name": "pagesWidget", "type": "QStackedWidget", "visible": 1, "window": apollo_MainWindow}
pagesWidget_lbHeader_QLabel = {"container": apollo_pagesWidget_QStackedWidget, "name": "lbHeader", "occurrence": 2, "type": "QLabel", "visible": 1}
pagesWidget_lbPower_QLabel = {"container": apollo_pagesWidget_QStackedWidget, "name": "lbPower", "type": "QLabel", "visible": 1}
pagesWidget_lbPulseWidth_QLabel = {"container": apollo_pagesWidget_QStackedWidget, "name": "lbPulseWidth", "type": "QLabel", "visible": 1}
apollo_btPulsedMode_QToolButton = {"name": "btPulsedMode", "type": "QToolButton", "visible": 1, "window": apollo_MainWindow}
apollo_btCwMode_QToolButton = {"name": "btCwMode", "type": "QToolButton", "visible": 1, "window": apollo_MainWindow}
apollo_edName_QLineEdit = {"name": "edName", "type": "QLineEdit", "visible": 1, "window": apollo_MainWindow}
keyboardFrame_KeyButtonLetter_2 = {"container": apollo_keyboardFrame_QFrame, "text": "а", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
keyboardFrame_KeyButtonLetter_3 = {"container": apollo_keyboardFrame_QFrame, "text": "с", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
apollo_btSave_QPushButton = {"name": "btSave", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
keyboardFrame_KeyButtonLetter_4 = {"container": apollo_keyboardFrame_QFrame, "text": "ь", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
apollo_btCancel_QPushButton = {"name": "btCancel", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
frToolbar_tbEditPreset_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbEditPreset", "type": "QToolButton", "visible": 1}
frToolbar_tbDeletePreset_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbDeletePreset", "type": "QToolButton", "visible": 1}
apollo_wdNavigationBar_QWidget = {"name": "wdNavigationBar", "occurrence": 2, "type": "QWidget", "visible": 1, "window": apollo_MainWindow}
apollo_btClearName_QToolButton = {"name": "btClearName", "type": "QToolButton", "visible": 1, "window": apollo_MainWindow}
apollo_centralWidget_QWidget = {"name": "centralWidget", "occurrence": 2, "type": "QWidget", "visible": 1, "window": apollo_MainWindow}
keyboardFrame_KeyButtonLetter_5 = {"container": apollo_keyboardFrame_QFrame, "text": "ъ", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
sclProfiles_12_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 12, "type": "ProfileButton", "unnamed": 1, "visible": 1}
centralWidget_comboBox_ComboBox = {"container": apollo_centralWidget_QStackedWidget, "name": "comboBox", "type": "ComboBox", "visible": 1}
comboBox_lbValue_AutoReducibleFontSizeLabel = {"container": centralWidget_comboBox_ComboBox, "name": "lbValue", "type": "AutoReducibleFontSizeLabel", "visible": 1}
apollo_aivComboBoxPopup_QTreeView = {"name": "aivComboBoxPopup", "type": "QTreeView", "visible": 1, "window": apollo_MainWindow}
comboBox_lbLogo_QLabel = {"container": centralWidget_comboBox_ComboBox, "name": "lbLogo", "type": "QLabel", "visible": 1}
apollo_frmComboBoxHeader_ComboBoxTwin = {"name": "frmComboBoxHeader", "type": "ComboBoxTwin", "visible": 1, "window": apollo_MainWindow}
frmComboBoxHeader_lbValue_AutoReducibleFontSizeLabel = {"container": apollo_frmComboBoxHeader_ComboBoxTwin, "name": "lbValue", "type": "AutoReducibleFontSizeLabel", "visible": 1}
comboBox_lbPixmap_QLabel = {"container": centralWidget_comboBox_ComboBox, "name": "lbPixmap", "type": "QLabel", "visible": 1}
frmComboBoxHeader_lbPixmap_QLabel = {"container": apollo_frmComboBoxHeader_ComboBoxTwin, "name": "lbPixmap", "type": "QLabel", "visible": 1}
centralWidget_frmSettings_QFrame = {"container": apollo_centralWidget_QStackedWidget, "name": "frmSettings", "type": "QFrame", "visible": 1}
sclProfiles_uu_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "uu", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_editFrame_QFrame = {"name": "editFrame", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
editFrame_tbClear_QToolButton = {"container": apollo_editFrame_QFrame, "name": "tbClear", "type": "QToolButton", "visible": 1}
keyboardFrame_t_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "t", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
apollo_Warning_MessageBox = {"name": "Warning", "type": "MessageBox", "visible": 1, "window": apollo_MainWindow}
warning_OK_QPushButton = {"container": apollo_Warning_MessageBox, "text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1}
keyboardFrame_Cancel_KeyButtonCancel = {"container": apollo_keyboardFrame_QFrame, "text": "Cancel", "type": "KeyButtonCancel", "unnamed": 1, "visible": 1}
wdKeypad_pushButton_8_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_8", "type": "QPushButton", "visible": 1}
sclProfiles_uut_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "uut", "type": "ProfileButton", "unnamed": 1, "visible": 1}
keyboardFrame_i_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "i", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
sclProfiles_i_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "i", "type": "ProfileButton", "unnamed": 1, "visible": 1}
centralWidget_pbReduce_QPushButton = {"container": apollo_centralWidget_QStackedWidget, "name": "pbReduce", "type": "QPushButton", "visible": 1}
keyboardFrame_keyboardWidget_KeyboardWidget = {"container": apollo_keyboardFrame_QFrame, "name": "keyboardWidget", "type": "KeyboardWidget", "visible": 1}
question_S_QPushButton = {"container": apollo_Question_MessageBox, "text": "SÍ", "type": "QPushButton", "unnamed": 1, "visible": 1}
sclProfiles_1_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 1, "type": "ProfileButton", "unnamed": 1, "visible": 1}
warning_TextLabel_QLabel = {"container": apollo_Warning_MessageBox, "name": "TextLabel", "type": "QLabel", "visible": 1}
keyboardFrame_0_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": 0, "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
sclProfiles_90_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 90, "type": "ProfileButton", "unnamed": 1, "visible": 1}
sclProfiles_909_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 909, "type": "ProfileButton", "unnamed": 1, "visible": 1}
sclProfiles_10_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 10, "type": "ProfileButton", "unnamed": 1, "visible": 1}
sclProfiles_107_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": 107, "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_tbAssistant_QToolButton = {"name": "tbAssistant", "type": "QToolButton", "visible": 1, "window": apollo_MainWindow}
apollo_frWizardPlace_WizardWidget = {"name": "frWizardPlace", "type": "WizardWidget", "visible": 1, "window": apollo_MainWindow}
frWizardPlace_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Литотрипсия", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_2 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Бъбрек", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_6_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Малък\n(<6)", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_500_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Мек\n(<500)", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_HU_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "ПЛЪТНОСТ НА КАМЪКА (HU)", "type": "WizardTitle", "unnamed": 1, "visible": 1}
frWizardPlace_MM_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "РАЗМЕР НА КАМЪКА (MM)", "type": "WizardTitle", "unnamed": 1, "visible": 1}
frWizardPlace_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "МЕСТОПОЛОЖЕНИЕ", "type": "WizardTitle", "unnamed": 1, "visible": 1}
frWizardPlace_WizardTitle_2 = {"container": apollo_frWizardPlace_WizardWidget, "text": "ТИП ТЕРАПИЯ", "type": "WizardTitle", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_3 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Меки тъкани", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_4 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Тумор|Хемостаза", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_BPH_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "BPH", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_5 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Енуклеация|Хемостаза", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_6 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Пикочен мехур", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_7 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Неизвестно", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_8 = {"container": apollo_frWizardPlace_WizardWidget, "occurrence": 2, "text": "Неизвестно", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Title_QLabel = {"container": apollo_frWizardPlace_WizardWidget, "name": "Title", "type": "QLabel", "visible": 1}
frWizardPlace_WizardApplyButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "ПРОДЪЛЖАВАНЕ>>>", "type": "WizardApplyButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardTitle_3 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Среден\n(6-10)", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_6_10_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Среден\n(6-10)", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_500_1000_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Среден\n(500-1000)", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_10_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Голям\n(>10)", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_1000_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Твърд\n(>1000)", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_9 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Уретер", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_10 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Вапориране|Хемостаза", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_11 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Разрез|Хемостаза", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardButton_12 = {"container": apollo_frWizardPlace_WizardWidget, "text": "Енуклеация|Ниска мощност", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_WizardTitle_4 = {"container": apollo_frWizardPlace_WizardWidget, "text": "ЛЯВ ПЕДАЛ|ДЕСЕН ПЕДАЛ", "type": "WizardTitle", "unnamed": 1, "visible": 1}
keyboardFrame_KeyButtonShift = {"aboveWidget": keyboardFrame_KeyButtonLetter_3, "container": apollo_keyboardFrame_QFrame, "type": "KeyButtonShift", "unnamed": 1, "visible": 1}
keyboardFrame_KeyButtonLetter_6 = {"container": apollo_keyboardFrame_QFrame, "text": "Х", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}
aivComboBoxPopup_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Енуклеация", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_2 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Ниска мощност", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_3 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Песъчинки в бъбрека (високо)", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_4 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Песъчинки в бъбрека (ниско)", "type": "QModelIndex"}
aivComboBoxPopup_Popcorn_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Техника Popcorn в бъбрека", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_5 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Фрагментиране в бъбрека (високо)", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_6 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Фрагментиране в бъбрека (ниско)", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_7 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Уретер (фрагментиране)", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_8 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Песъчинки, уретер", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_9 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Фрагментиране в пикочния мехур", "type": "QModelIndex"}
aivComboBoxPopup_QScrollBar = {"container": apollo_aivComboBoxPopup_QTreeView, "type": "QScrollBar", "unnamed": 1, "visible": 1}
aivComboBoxPopup_QModelIndex_10 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "КОАГУЛАЦИЯ", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_11 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Енуклеация в простатата (високо)", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_12 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Енуклеация в простатата (ниско)", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_13 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Вапориране за тъкан (с импулс)", "type": "QModelIndex"}
aivComboBoxPopup_CW_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Вапориране за тъкан (CW)", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_14 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Аблация/ексцизия на тумор ", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_15 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Фрагментиране в бъбрека", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_16 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Песъчинки в бъбрека", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_17 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Уретер фрагментиране", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_18 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Фрагментация на пикочния мехур", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_19 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Вапориране", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_20 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Хемостаза", "type": "QModelIndex"}
aivComboBoxPopup_QModelIndex_21 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Тумор", "type": "QModelIndex"}
frWizardPlace_tbHome_QToolButton = {"container": apollo_frWizardPlace_WizardWidget, "name": "tbHome", "type": "QToolButton", "visible": 1}
centralWidget_wdLeftPedal_PedalSettingsWidget = {"container": apollo_centralWidget_QStackedWidget, "name": "wdLeftPedal", "type": "PedalSettingsWidget", "visible": 1}
centralWidget_pbSaveSettings_QPushButton = {"container": apollo_centralWidget_QStackedWidget, "name": "pbSaveSettings", "type": "QPushButton", "visible": 1}
tvPresets_QModelIndex = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Песъчинки в бъбрека (високо)", "type": "QModelIndex"}
tvPresets_QModelIndex_2 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Песъчинки в бъбрека (ниско)", "type": "QModelIndex"}
tvPresets_Popcorn_QModelIndex = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Техника Popcorn в бъбрека", "type": "QModelIndex"}
tvPresets_QModelIndex_3 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Фрагментиране в бъбрека (високо)", "type": "QModelIndex"}
tvPresets_QModelIndex_4 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Фрагментиране в бъбрека (ниско)", "type": "QModelIndex"}
tvPresets_QModelIndex_5 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Уретер (фрагментиране)", "type": "QModelIndex"}
tvPresets_QModelIndex_6 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Песъчинки, уретер", "type": "QModelIndex"}
tvPresets_QModelIndex_7 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Фрагментиране в пикочния мехур", "type": "QModelIndex"}
tvPresets_QModelIndex_8 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "КОАГУЛАЦИЯ", "type": "QModelIndex"}
tvPresets_QModelIndex_9 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Енуклеация в простатата (високо)", "type": "QModelIndex"}
tvPresets_QModelIndex_10 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Енуклеация в простатата (ниско)", "type": "QModelIndex"}
tvPresets_QModelIndex_11 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Вапориране за тъкан (с импулс)", "type": "QModelIndex"}
tvPresets_CW_QModelIndex = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Вапориране за тъкан (CW)", "type": "QModelIndex"}
tvPresets_QModelIndex_12 = {"column": 0, "container": apollo_tvPresets_PresetsTable, "text": "Аблация/ексцизия на тумор ", "type": "QModelIndex"}


# Additional object definitions from names.py (missing in Bulgarian file)
frmPopup_lbTitle_QLabel = {"container": alarmsListScreen_frmPopup_AlarmNotificationPopup, "name": "lbTitle", "type": "QLabel", "visible": 1}

centralWidget_lbHeader_QLabel_2 = {"container": apollo_centralWidget_QStackedWidget, "name": "lbHeader", "type": "QLabel", "visible": 1}

centralWidget_btDualPulse_ButtonWithClickSound = {"container": apollo_centralWidget_QStackedWidget, "name": "btDualPulse", "type": "ButtonWithClickSound", "visible": 1}

centralWidget_PulseModeWidget_PulseModeWidget_2 = {"container": apollo_centralWidget_QStackedWidget, "name": "PulseModeWidget", "occurrence": 2, "type": "PulseModeWidget", "visible": 1}

apollo_frmComboBoxShadow_QFrame = {"name": "frmComboBoxShadow", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}

pRESET_NAME_HeaderViewItem = {"container": tvPresets_QHeaderView, "text": "PRESET NAME", "type": "HeaderViewItem", "visible": True}

eNERGY_HeaderViewItem = {"container": tvPresets_QHeaderView, "text": "ENERGY", "type": "HeaderViewItem", "visible": True}

fREQUENCY_HeaderViewItem = {"container": tvPresets_QHeaderView, "text": "FREQUENCY", "type": "HeaderViewItem", "visible": True}

pOWER_HeaderViewItem = {"container": tvPresets_QHeaderView, "text": "POWER", "type": "HeaderViewItem", "visible": True}

pULSE_WIDTH_HeaderViewItem = {"container": tvPresets_QHeaderView, "text": "PULSE WIDTH", "type": "HeaderViewItem", "visible": True}

pagesWidget_PulseModeWidget_PulseModeWidget = {"container": apollo_pagesWidget_QStackedWidget, "name": "PulseModeWidget", "type": "PulseModeWidget", "visible": 1}

pagesWidget_lbHeader_QLabel_2 = {"container": apollo_pagesWidget_QStackedWidget, "name": "lbHeader", "type": "QLabel", "visible": 1}

centralWidget_lbHeader_QLabel_3 = {"container": apollo_centralWidget_QFrame, "name": "lbHeader", "type": "QLabel", "visible": 1}

frmHeader_lbHeader_QLabel = {"container": apollo_frmHeader_QFrame, "name": "lbHeader", "type": "QLabel", "visible": 1}

dATE_TIME_HeaderViewItem = {"container": tvErrorLog_QHeaderView, "text": "DATE TIME", "type": "HeaderViewItem", "visible": True}

eRROR_CODE_HeaderViewItem = {"container": tvErrorLog_QHeaderView, "text": "ERROR CODE", "type": "HeaderViewItem", "visible": True}

eRROR_DESCRIPTION_HeaderViewItem = {"container": tvErrorLog_QHeaderView, "text": "ERROR DESCRIPTION", "type": "HeaderViewItem", "visible": True}

stackedWidget_lbTitle_QLabel = {"container": stackedWidget_stackedWidget_QStackedWidget, "name": "lbTitle", "type": "QLabel", "visible": 1}

question_YES_QPushButton = {"container": apollo_Question_MessageBox, "text": "YES", "type": "QPushButton", "unnamed": 1, "visible": 1}

wdKeypad_pushButton_5_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_5", "type": "QPushButton", "visible": 1}

passwordScreen_mInvalidPassNotif_QLabel = {"container": apollo_PasswordScreen_PasswordScreen, "name": "mInvalidPassNotif", "type": "QLabel", "visible": 1}

passwordScreen_pbBackspace_QPushButton = {"container": apollo_PasswordScreen_PasswordScreen, "name": "pbBackspace", "type": "QPushButton", "visible": 1}

keyboardFrame_h_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "h", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

keyboardFrame_u_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "u", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

keyboardFrame_v_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "v", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

keyboardFrame_r_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "r", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

keyboardFrame_a_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "a", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

keyboardFrame_x_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "x", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

keyboardFrame_123_KeyButtonSpace = {"aboveWidget": keyboardFrame_x_KeyButtonLetter, "container": apollo_keyboardFrame_QFrame, "leftWidget": keyboardFrame_123_KeyButtonNumSwitch, "type": "KeyButtonSpace", "unnamed": 1, "visible": 1}

sclProfiles_thuvera_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "thuvera", "type": "ProfileButton", "unnamed": 1, "visible": 1}

sclProfiles_thuvera_1_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "thuvera 1", "type": "ProfileButton", "unnamed": 1, "visible": 1}

question_CANCEL_QPushButton = {"container": apollo_Question_MessageBox, "text": "CANCEL", "type": "QPushButton", "unnamed": 1, "visible": 1}

keyboardFrame_p_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "p", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

keyboardFrame_s_KeyButtonLetter = {"container": apollo_keyboardFrame_QFrame, "text": "s", "type": "KeyButtonLetter", "unnamed": 1, "visible": 1}

aivComboBoxPopup_Kidney_Dust_High_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Kidney Dust (High)", "type": "QModelIndex"}

aivComboBoxPopup_Kidney_Dust_Low_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Kidney Dust (Low)", "type": "QModelIndex"}

aivComboBoxPopup_Kidney_Popcorn_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Kidney Popcorn", "type": "QModelIndex"}

aivComboBoxPopup_Kidney_Fragment_High_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Kidney Fragment (High)", "type": "QModelIndex"}

aivComboBoxPopup_Kidney_Fragment_Low_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Kidney Fragment (Low)", "type": "QModelIndex"}

aivComboBoxPopup_Ureter_Fragment_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Ureter (Fragment)", "type": "QModelIndex"}

aivComboBoxPopup_Ureter_Dust_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Ureter Dust", "type": "QModelIndex"}

aivComboBoxPopup_Bladder_Fragment_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Bladder Fragment", "type": "QModelIndex"}

aivComboBoxPopup_COAG_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "COAG", "type": "QModelIndex"}

aivComboBoxPopup_Prostate_Enucleate_High_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Prostate Enucleate (High)", "type": "QModelIndex"}

aivComboBoxPopup_Prostate_Enucleate_Low_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Prostate Enucleate (Low)", "type": "QModelIndex"}

aivComboBoxPopup_Tissue_Vaporize_Pulsed_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Tissue Vaporize (Pulsed)", "type": "QModelIndex"}

aivComboBoxPopup_Tissue_Vaporize_CW_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Tissue Vaporize (CW)", "type": "QModelIndex"}

aivComboBoxPopup_Tumor_Ablation_Excision_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Tumor Ablation/Excision", "type": "QModelIndex"}

apollo_wdLogo_QWidget = {"name": "wdLogo", "type": "QWidget", "visible": 1, "window": apollo_MainWindow}

question_NO_QPushButton = {"container": apollo_Question_MessageBox, "text": "NO", "type": "QPushButton", "unnamed": 1, "visible": 1}

sclProfiles_thuveraa_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "thuveraa", "type": "ProfileButton", "unnamed": 1, "visible": 1}

frWizardPlace_TREATMENT_TYPE_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "TREATMENT TYPE", "type": "WizardTitle", "unnamed": 1, "visible": 1}

frWizardPlace_Lithotripsy_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Lithotripsy", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Soft_Tissue_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Soft Tissue", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_LOCATION_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "LOCATION", "type": "WizardTitle", "unnamed": 1, "visible": 1}

frWizardPlace_STONE_SIZE_MM_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "STONE SIZE (MM)", "type": "WizardTitle", "unnamed": 1, "visible": 1}

frWizardPlace_STONE_DENSITY_HU_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "STONE DENSITY (HU)", "type": "WizardTitle", "unnamed": 1, "visible": 1}

frWizardPlace_Kidney_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Kidney", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Small_6_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Small\n(<6)", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Medium_6_10_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Medium\n(6-10)", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Large_10_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Large\n(>10)", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Unknown_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Unknown", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Soft_500_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Soft\n(<500)", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Medium_500_1000_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Medium\n(500-1000)", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Hard_1000_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Hard\n(>1000)", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Ureter_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Ureter", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Bladder_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Bladder", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_LEFT_PEDAL_RIGHT_PEDAL_WizardTitle = {"container": apollo_frWizardPlace_WizardWidget, "text": "LEFT PEDAL|RIGHT PEDAL", "type": "WizardTitle", "unnamed": 1, "visible": 1}

frWizardPlace_Vaporize_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Vaporize|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Tumor_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Tumor|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Incision_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Incision|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Enucleation_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Enucleation|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_Enucleation_Low_Power_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Enucleation|Low Power", "type": "WizardButton", "unnamed": 1, "visible": 1}

frWizardPlace_ADVANCE_WizardApplyButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "ADVANCE>>>", "type": "WizardApplyButton", "unnamed": 1, "visible": 1}

sclProfiles_thuveraaa_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "thuveraaa", "type": "ProfileButton", "unnamed": 1, "visible": 1}

aivComboBoxPopup_Low_Power_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Low Power", "type": "QModelIndex"}

aivComboBoxPopup_Enucleation_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Enucleation", "type": "QModelIndex"}

aivComboBoxPopup_Kidney_Fragment_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Kidney Fragment", "type": "QModelIndex"}

aivComboBoxPopup_Kidney_Dust_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Kidney Dust", "type": "QModelIndex"}

aivComboBoxPopup_Ureter_Fragment_QModelIndex_2 = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Ureter Fragment", "type": "QModelIndex"}

aivComboBoxPopup_Bladder_Fragmentation_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Bladder Fragmentation", "type": "QModelIndex"}

aivComboBoxPopup_Vaporize_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Vaporize", "type": "QModelIndex"}

aivComboBoxPopup_Hemostasis_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Hemostasis", "type": "QModelIndex"}

aivComboBoxPopup_Tumor_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Tumor", "type": "QModelIndex"}

aivComboBoxPopup_Incision_QModelIndex = {"column": 0, "container": apollo_aivComboBoxPopup_QTreeView, "text": "Incision", "type": "QModelIndex"}

centralWidget_pbReduce_QPushButton_2 = {"container": apollo_centralWidget_QStackedWidget, "name": "pbReduce", "occurrence": 2, "type": "QPushButton", "visible": 1}

apollo_TextLabel_QLabel = {"name": "TextLabel", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}

apollo_YES_QPushButton = {"text": "YES", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": apollo_MainWindow}

apollo_NO_QPushButton = {"text": "NO", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": apollo_MainWindow}

apollo_pbDownload_QPushButton = {"name": "pbDownload", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}

apollo_wdTotalEnergy_QWidget = {"name": "wdTotalEnergy", "type": "QWidget", "visible": 1, "window": apollo_MainWindow}
question_ANO_QPushButton = {"container": apollo_Question_MessageBox, "text": "ANO", "type": "QPushButton", "unnamed": 1, "visible": 1}
question_NE_QPushButton = {"container": apollo_Question_MessageBox, "text": "NE", "type": "QPushButton", "unnamed": 1, "visible": 1}
apollo_lbApolloLogo_QLabel = {"name": "lbApolloLogo", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
