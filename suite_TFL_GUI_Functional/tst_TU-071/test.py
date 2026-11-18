from common import *
import names


def main():
    test.log("This TC contains TU-071 to TU-219")
    test.log("Verification for TU-071")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_kidney_lithotripsy()

    clickButton(waitForObject(names.frWizardPlace_Small_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 347, 32, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("TU-072-left")
    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame), 641, 91, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel_2), 83, 45, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("TU-072-Right")
    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame), 552, 628, Qt.NoModifier, Qt.LeftButton)
    for i in range(3):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(2):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(11):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(12):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_3))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(4):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_2))

    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(16):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_4))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(4):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_4))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(4):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_3))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    
    navigate_to_ureter_lithotripsy()

    clickButton(waitForObject(names.frWizardPlace_Medium_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 14, 30, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("lithotripsy_ureter_left")
    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame), 673, 102, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbLogo_QLabel), 40, 46, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("lithotripsy_ureter_right")
    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame), 673, 111, Qt.NoModifier, Qt.LeftButton)
    for i in range(4):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(13):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(3):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(5):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_3))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(2):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_4))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(6):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_2))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(8):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_4))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    
    navigate_to_bph_enucleation_hemostasis()

    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 34, 25, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("bph_left")
    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame), 939, 109, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbLogo_QLabel), 56, 12, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("bph_right")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 28, 23, Qt.NoModifier, Qt.LeftButton)
    for i in range(6):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    for i in range(8):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(11):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(2):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_3))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))

    clickButton(waitForObject(names.centralWidget_btDualPulse_ButtonWithClickSound))
    clickButton(waitForObject(names.centralWidget_btShortPulse_ButtonWithClickSound))
    clickButton(waitForObject(names.centralWidget_btLongPulse_ButtonWithClickSound))
    clickButton(waitForObject(names.centralWidget_btMiddlePulse_ButtonWithClickSound))
    for i in range(5):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_4))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(6):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_2))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(19):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_3))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    
    for i in range(9):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_4))
    test.imagePresent("Exit_mode")
    
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    
    
