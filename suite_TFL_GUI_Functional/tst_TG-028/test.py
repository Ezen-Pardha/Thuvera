
# -*- coding: utf-8 -*-

import names
from common import *

def main():
    test.log("SVV TAG: Maximum User Presets Per Profile - TG-029")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton, 1147693))
    enterpin()
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "Test1")
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
    mouseClick(waitForObject(names.apollo_edName_QLineEdit), 173, 25, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "p")
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "<Backspace>")
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "Preset1")
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.apollo_btSave_QPushButton))  
    if waitForObjectExists(names.tvPresets_Preset1_QModelIndex):
        actualText = waitForObject(names.tvPresets_Preset1_QModelIndex).displayText

        if actualText == "Preset1":
            test.passes("Preset1 created successfully")
        else:
            test.fail("Preset creation failed. Expected: Preset1, Actual: " + str(actualText))
    else:
        test.fail("Preset1 is not present in the preset list")
        
    for i in range(2, 21):

        """Click Add Preset"""
        clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
        snooze(1)

        """Select preset name field"""
        mouseClick(waitForObject(names.apollo_edName_QLineEdit),
                   161, 17, Qt.NoModifier, Qt.LeftButton)
    
        """Enter Preset"""
        clickButton(waitForObject(names.keyboardFrame_p_KeyButtonLetter))
        clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
        clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
        clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
        clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
        clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    
        """Switch to numeric keyboard"""
        clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    
        """Enter preset number"""
        for digit in str(i):
            digitButton = getattr(names, "keyboardFrame_" + digit + "_KeyButtonLetter")
            clickButton(waitForObject(digitButton))
    
        """Press Enter"""
        clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
        snooze(1)
    
        """Save preset"""
        clickButton(waitForObject(names.apollo_btSave_QPushButton))
        snooze(2)
    
        test.passes("Preset" + str(i) + " created successfully")
    test.passes("20 presets are created successfully")
    
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
    expectedText = "The maximum number (20) of users presets has been reached"
    
    if waitForObjectExists(names.warning_TextLabel_QLabel):
        actualText = str(waitForObject(names.warning_TextLabel_QLabel).text)
    
        if actualText == expectedText:
            test.passes("Maximum limit of 20 user presets reached warning displayed successfully")
        else:
            test.fail("Warning text mismatch. Expected: " + expectedText + " | Actual: " + actualText)
    else:
        test.fail("Maximum user presets warning message was not displayed")
    mouseClick(waitForObject(names.apollo_Warning_MessageBox), 1015, 197, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.warning_OK_QPushButton))

    clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
    mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "_1"), 90, 34, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_Question_MessageBox), 131, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.question_OK_QPushButton))
    test.passes("Preset is Deleted Successfully")
    
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
    mouseClick(waitForObject(names.apollo_edName_QLineEdit), 196, 24, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.keyboardFrame_p_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_0_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.apollo_btSave_QPushButton))
    test.passes("Preset Saved Successfully")
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
    expectedText = "The maximum number (20) of users presets has been reached"
    
    if waitForObjectExists(names.warning_TextLabel_QLabel):
        actualText = str(waitForObject(names.warning_TextLabel_QLabel).text)
    
        if actualText == expectedText:
            test.passes("Maximum limit of 20 user presets reached warning displayed successfully")
        else:
            test.fail("Warning text mismatch. Expected: " + expectedText + " | Actual: " + actualText)
    else:
        test.fail("Maximum user presets warning message was not displayed")
    mouseClick(waitForObject(names.apollo_Warning_MessageBox), 1015, 197, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.warning_OK_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    
    
        

