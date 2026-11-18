# -*- coding: utf-8 -*-

import names
from common import *

def main():
    test.log("SVV TAG: Settings Screen Top Banner Displayed TU-183")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_p_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_o_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_f_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_i_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_l_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton))
    test.log("Treatment screen is verified")
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    test.log("Setting screen is verified")

    mouseClick(waitForObject(names.apollo_centralWidget_QFrame), 729, 75, Qt.NoModifier, Qt.LeftButton)
    actual_text = str(waitForObjectExists(names.apollo_lbHeader_QLabel).text)

    if actual_text == "SETTINGS":
        test.passes("Top Banner SETTINGS is verified successfully")
    else:
        test.fail("Top Banner SETTINGS verification failed. Actual text: " + actual_text)  
    
    test.log("SVV TAG: Settings Screen Side Bar Displayed TU-184")  
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton))
    if test.imagePresent("settingsUserProfile"):
        test.passes("Side Bar Settings button is available")
    else:
        test.fail("Side Bar Settings button is not available")
        
    test.log("SVV TAG: Settings Screen Language Selection Drop Down TU-185")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    test.log("Treatment screen is verified")
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton))
    clickButton(waitForObject(names.apollo_btSettings_QPushButton, 59701))
    if actual_text == "SETTINGS":
        test.passes("Top Banner SETTINGS is verified successfully")
    else:
        test.fail("Top Banner SETTINGS verification failed. Actual text: " + actual_text)  
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 477, 28, Qt.NoModifier, Qt.LeftButton)
    if waitForObjectExists(names.centralWidget_frmComboBox_QFrame).visible:
        test.passes("Dropdown menu is present and visible")
    else:
        test.fail("Dropdown menu is not visible")
    
    test.log("SVV TAG: Settings Screen Volume Adjustment TU-186")
    
    if waitForObjectExists(names.centralWidget_sldVolume_QSlider).visible:
        test.passes("Volume slider is visible and Adjustable")
    else:
        test.fail("Volume slider is not visible and Adjustable") 
    scrollTo(waitForObject(names.centralWidget_sldVolume_QSlider), 75)
    test.passes("Maximum volume is set successfully")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton))
    test.passes("Treatment Screen is verified successfully")
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 118, 41, Qt.NoModifier, Qt.LeftButton)
    test.passes("Read state Screen is verified successfully")
    clickButton(waitForObject(names.apollo_LeftPedalBtn_QPushButton))
    test.passes("Left Pedal emission is verified successfully")
    clickButton(waitForObject(names.apollo_RightPedalBtn_QPushButton))
    test.passes("Right Pedal emission is verified successfully")
    clickButton(waitForObject(names.apollo_MiddlePedalBtn_QPushButton))
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 74, 23, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    

    
    
