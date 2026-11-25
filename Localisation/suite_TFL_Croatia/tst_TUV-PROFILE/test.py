# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 91, 42, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObject(names.question_DA_QPushButton),
            waitForObjectExists(names.question_NE_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Confirm Exit?",
            "NO",
            "YES"
        ],
    )
    
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Želite li potvrditi izlaz?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Želite li potvrditi izlaz?": 
        test.passes("Želite li potvrditi izlaz? popup is verified")
    else: test.fail("Želite li potvrditi izlaz? popup verification failed")
    clickButton(waitForObject(names.question_DA_QPushButton))
    test.vp("Verifying Profile Screen")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    validate_localization(
        objects=[
            waitForObjectExists(names.warning_TextLabel_QLabel),
            waitForObjectExists(names.warning_U_REDU_QPushButton_2)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "The minimum profile name length is 1 character",
            "OK"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Minimalna duljina naziva profila je 1 znak ")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Minimalna duljina naziva profila je 1 znak ": 
        test.passes("Minimalna duljina naziva profila je 1 znak  warning popup is verified")
    else: test.fail("Minimalna duljina naziva profila je 1 znak  warning popup verification failed")
    clickButton(waitForObject(names.warning_U_REDU_QPushButton_2))
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
            waitForObjectExists(names.warning_U_REDU_QPushButton_2)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "The profile name \"XXXX\" already exists.",
            "OK"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Naziv profila \"thuvera\"<br>već postoji.")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Naziv profila \"thuvera\"<br>već postoji.": 
        test.passes("Naziv profila \"thuvera\"<br>već postoji. warning popup is verified")
    else: test.fail("Naziv profila \"thuvera\"<br>već postoji. warning popup verification failed")
    clickButton(waitForObject(names.warning_U_REDU_QPushButton_2))
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
            waitForObjectExists(names.question_U_REDU_QPushButton),
            waitForObjectExists(names.question_ODUSTANI_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "DELETE PROFILE?",
            "OK",
            "CANCEL"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "ŽELITE LI IZBRISATI PROFIL?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "ŽELITE LI IZBRISATI PROFIL?": 
        test.passes("ŽELITE LI IZBRISATI PROFIL? popup is verified")
    else: test.fail("ŽELITE LI IZBRISATI PROFIL? popup verification failed")
    clickButton(waitForObject(names.question_U_REDU_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_thuveraaa_ProfileButton))
    clickButton(waitForObject(names.question_U_REDU_QPushButton))
    validate_localization(
        objects=[
            waitForObjectExists(names.sclProfiles_Zadano_ProfileButton),
            waitForObjectExists(names.apollo_tbAssistant_QToolButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Default",
            "ASSISTANT"
        ],
    )

    

        

    
