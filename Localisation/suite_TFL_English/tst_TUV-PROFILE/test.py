# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton, 32878))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObjectExists(names.question_YES_QPushButton),
            waitForObjectExists(names.question_NO_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Confirm Exit?",
            "NO",
            "YES"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Confirm Exit?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Confirm Exit?": 
        test.passes("Confirm Exit? popup is verified")
    else: test.fail("Confirm Exit? popup verification failed")
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    validate_localization(
        objects=[
            waitForObjectExists(names.warning_TextLabel_QLabel),
            waitForObjectExists(names.warning_OK_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "The minimum profile name length is 1 character",
            "OK"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "The minimum profile name length is 1 character")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "The minimum profile name length is 1 character": 
        test.passes("The minimum profile name length is 1 character warning popup is verified")
    else: test.fail("The minimum profile name length is 1 character warning popup verification failed")
    clickButton(waitForObject(names.warning_OK_QPushButton))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_h_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_u_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_v_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonLetter))
    validate_localization(
        objects=[
            waitForObjectExists(names.keyboardFrame_Enter_KeyButtonEnter),
            waitForObjectExists(names.keyboardFrame_Cancel_KeyButtonCancel)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Enter",
            "Cancel"
        ],
    )
    
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_h_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_u_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_v_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonLetter))
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

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "The profile name \"thuvera\"<br>already exists.")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "The profile name \"thuvera\"<br>already exists.": 
        test.passes("The profile name \"thuvera\"<br>already exists. warning popup is verified")
    else: test.fail("The profile name \"thuvera\"<br>already exists. warning popup verification failed")
    clickButton(waitForObject(names.warning_OK_QPushButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonLetter))
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

    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_lbModeHelp_QLabel)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Select Profile to Delete"
        ],
    )

    clickButton(waitForObject(names.sclProfiles_thuvera_ProfileButton))
    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObjectExists(names.question_OK_QPushButton),
            waitForObjectExists(names.question_CANCEL_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "DELETE PROFILE?",
            "OK",
            "CANCEL"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "DELETE PROFILE?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "DELETE PROFILE?": 
        test.passes("DELETE PROFILE? popup is verified")
    else: test.fail("DELETE PROFILE? popup verification failed")
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_thuveraaa_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    validate_assistant_label()
    validate_localization(
        objects=[
            waitForObjectExists(names.sclProfiles_Default_ProfileButton),
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Default",
        ],
    )
    test.compare(str(waitForObjectExists(names.sclProfiles_Default_ProfileButton).text), "Default")
    if str(waitForObjectExists(names.sclProfiles_Default_ProfileButton).text) == "Default":
        test.passes("Profile Screen verified")
    else: test.fail("Profile Screen verification failed")
   
        

    
