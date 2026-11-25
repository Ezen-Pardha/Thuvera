# -*- coding: utf-8 -*-
 
import names
from squish import *
from common import *
 
def main():
 
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 184, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Български (Bulgaria)"), 130, 25, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    test.imagePresent("exitProfile")
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 202, 18, Qt.NoModifier, Qt.LeftButton)
    
    
    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_TextLabel_QLabel),
            waitForObjectExists(names.question_QPushButton),
            waitForObjectExists(names.question_QPushButton_3)
           
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Confirm Exit?",
            "NO",
            "YES"
        ],
    )

    clickButton(waitForObject(names.question_QPushButton))
    test.vp("profileScreen")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))

    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    test.imagePresent("minimumCharacterPopup")

    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_TextLabel_QLabel),
            waitForObjectExists(names.warning_OK_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "The minimum profile name length is 1 character",
            "OK"
        ],
    )
    clickButton(waitForObject(names.warning_OK_QPushButton))

    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    
    validate_localization(
        objects=[
            waitForObject(names.keyboardFrame_Enter_KeyButtonEnter),
            waitForObject(names.keyboardFrame_Cancel_KeyButtonCancel)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Enter",
            "Cancel"
        ],
    )

    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.frToolbar_tbEditProfile_QToolButton))
    test.compare(str(waitForObjectExists(names.apollo_lbModeHelp_QLabel).text), "Изберете профил за преименуване")
    
    validate_localization(
        objects=[

            waitForObjectExists(names.apollo_lbModeHelp_QLabel)

        ],
        screen_name="PROFILE",
        expected_strings=[
            "Select Profile to Rename"
        ],
    )
    clickButton(waitForObject(names.sclProfiles_123_ProfileButton))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch)) 
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    test.compare(str(waitForObjectExists(names.apollo_lbModeHelp_QLabel).text), "Изберете профил за изтриване")
    clickButton(waitForObject(names.sclProfiles_12345_ProfileButton))
    test.imagePresent("deleteProfile")
    
    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObjectExists(names.question_OK_QPushButton),
            waitForObjectExists(names.question_QPushButton_2),
        ],
        screen_name="PROFILE",
        expected_strings=[
            "DELETE PROFILE?",
            "OK",
            "CANCEL"
        ],
    )
 
    clickButton(waitForObject(names.question_QPushButton_2))
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    test.imagePresent("profileExistsPopup")

    validate_localization(
        objects=[
            waitForObjectExists(names.warning_TextLabel_QLabel),
            waitForObjectExists(names.warning_OK_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "The profile name \"XXXX\" already exists.",
            "OK"
        ],
    )
    
    clickButton(waitForObject(names.warning_OK_QPushButton))
    clickButton(waitForObject(names.keyboardFrame_Cancel_KeyButtonCancel))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_12345_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
