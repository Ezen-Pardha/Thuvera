# encoding: UTF-8

from objectmaphelper import *


# Added missing definitions from local names.py
apollo_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Apollo"}
apollo_AlarmsListScreen_AlarmsListScreen = {"name": "AlarmsListScreen", "type": "AlarmsListScreen", "visible": 1, "window": apollo_MainWindow}
alarmsListScreen_frmPopup_AlarmNotificationPopup = {"container": apollo_AlarmsListScreen_AlarmsListScreen, "name": "frmPopup", "type": "AlarmNotificationPopup", "visible": 1}
frmPopup_pbAccept_QPushButton = {"container": alarmsListScreen_frmPopup_AlarmNotificationPopup, "name": "pbAccept", "type": "QPushButton", "visible": 1}
apollo_PasswordScreen_PasswordScreen = {"name": "PasswordScreen", "type": "PasswordScreen", "visible": 1, "window": apollo_MainWindow}
passwordScreen_wdKeypad_Keypad = {"container": apollo_PasswordScreen_PasswordScreen, "name": "wdKeypad", "type": "Keypad", "visible": 1}
wdKeypad_pushButton_0_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_0", "type": "QPushButton", "visible": 1}
wdKeypad_pushButton_8_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_8", "type": "QPushButton", "visible": 1}
passwordScreen_pbBackspace_QPushButton = {"container": apollo_PasswordScreen_PasswordScreen, "name": "pbBackspace", "type": "QPushButton", "visible": 1}
apollo_sclProfiles_ProfilesScroll = {"name": "sclProfiles", "type": "ProfilesScroll", "visible": 1, "window": apollo_MainWindow}
sclProfiles_Default_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "Default", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_btHome_QPushButton = {"name": "btHome", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_tbAssistant_QToolButton = {"name": "tbAssistant", "type": "QToolButton", "visible": 1, "window": apollo_MainWindow}
apollo_frWizardPlace_WizardWidget = {"name": "frWizardPlace", "type": "WizardWidget", "visible": 1, "window": apollo_MainWindow}
frWizardPlace_Lithotripsy_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Lithotripsy", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Kidney_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Kidney", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Ureter_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Ureter", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Bladder_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Bladder", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_ADVANCE_WizardApplyButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "ADVANCE>>>", "type": "WizardApplyButton", "unnamed": 1, "visible": 1}
frWizardPlace_Soft_Tissue_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Soft Tissue", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Vaporize_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Vaporize|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Tumor_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Tumor|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Incision_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Incision|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_BPH_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "BPH", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Enucleation_Hemostasis_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Enucleation|Hemostasis", "type": "WizardButton", "unnamed": 1, "visible": 1}
frWizardPlace_Enucleation_Low_Power_WizardButton = {"container": apollo_frWizardPlace_WizardWidget, "text": "Enucleation|Low Power", "type": "WizardButton", "unnamed": 1, "visible": 1}
apollo_btExitProfile_QPushButton = {"name": "btExitProfile", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_Question_MessageBox = {"name": "Question", "type": "MessageBox", "visible": 1, "window": apollo_MainWindow}
question_YES_QPushButton = {"container": apollo_Question_MessageBox, "text": "YES", "type": "QPushButton", "unnamed": 1, "visible": 1}
apollo_btPresets_QPushButton = {"name": "btPresets", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_btTreatmentLogs_QPushButton = {"name": "btTreatmentLogs", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_btSettings_QPushButton = {"name": "btSettings", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_btUtilities_QPushButton = {"name": "btUtilities", "type": "QPushButton", "visible": 1, "window": apollo_MainWindow}
apollo_frToolbar_QFrame = {"name": "frToolbar", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
frToolbar_tbAddProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbAddProfile", "type": "QToolButton", "visible": 1}
apollo_keyboardFrame_QFrame = {"name": "keyboardFrame", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
keyboardFrame_Cancel_KeyButtonCancel = {"container": apollo_keyboardFrame_QFrame, "text": "Cancel", "type": "KeyButtonCancel", "unnamed": 1, "visible": 1}
sclProfiles_thuvera_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "thuvera", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_lbHeader_QLabel = {"name": "lbHeader", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
frToolbar_tbEditProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbEditProfile", "type": "QToolButton", "visible": 1}
sclProfiles_profile_1_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "profile 1", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_lbModeHelp_QLabel = {"name": "lbModeHelp", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_editFrame_QFrame = {"name": "editFrame", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
editFrame_tbClear_QToolButton = {"container": apollo_editFrame_QFrame, "name": "tbClear", "type": "QToolButton", "visible": 1}
editFrame_edEditText_QLineEdit = {"container": apollo_editFrame_QFrame, "name": "edEditText", "type": "QLineEdit", "visible": 1}
keyboardFrame_Enter_KeyButtonEnter = {"container": apollo_keyboardFrame_QFrame, "text": "Enter", "type": "KeyButtonEnter", "unnamed": 1, "visible": 1}
sclProfiles_profile1_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "profile1", "type": "ProfileButton", "unnamed": 1, "visible": 1}
apollo_Warning_MessageBox = {"name": "Warning", "type": "MessageBox", "visible": 1, "window": apollo_MainWindow}
warning_TextLabel_QLabel = {"container": apollo_Warning_MessageBox, "name": "TextLabel", "type": "QLabel", "visible": 1}
warning_OK_QPushButton = {"container": apollo_Warning_MessageBox, "text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1}
