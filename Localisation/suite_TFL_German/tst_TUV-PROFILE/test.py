
# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 479, 33, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Deutsch (Germany)"), 169, 35, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 202, 18, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_TextLabel_QLabel),
            waitForObjectExists(names.question_NEIN_QPushButton),
            waitForObjectExists(names.question_JA_QPushButton),
            
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Confirm Exit?",
            "NO",
            "YES"
        ],
    )

    clickButton(waitForObject(names.question_JA_QPushButton))
    
    validate_assistant_label()
    
    test.compare(str(waitForObjectExists(names.sclProfiles_Standard_ProfileButton).text), "Standard")
    test.compare(str(waitForObjectExists(names.sclProfiles_Standard_ProfileButton).windowIconText), "")
    test.compare(waitForObjectExists(names.sclProfiles_Standard_ProfileButton).visible, True)
    test.log("Profile Screen Verification")

    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

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
    clickButton(waitForObject(names.keyboardFrame_123_Ziffern_KeyButtonNumSwitch))
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
    clickButton(waitForObject(names.keyboardFrame_123_Ziffern_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_12345_ProfileButton))

    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_TextLabel_QLabel),
            waitForObjectExists(names.question_ABBRECHEN_QPushButton),
            waitForObjectExists(names.question_OK_QPushButton),
        ],
        screen_name="PROFILE",
        expected_strings=[
            "DELETE PROFILE?",
            "OK",
            "CANCEL"
        ],
    )

    clickButton(waitForObject(names.question_ABBRECHEN_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_123_Ziffern_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

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
