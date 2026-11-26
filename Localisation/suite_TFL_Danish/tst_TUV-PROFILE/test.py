# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Dansk (Denmark)"), 91, 42, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btHome_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObjectExists(names.question_NEJ_QPushButton),
            waitForObjectExists(names.question_JA_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Confirm Exit?",
            "NO",
            "YES"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Bekræft afslut?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Bekræft afslut?": 
        test.passes("Bekræft afslut? popup is verified")
    else: test.fail("Bekræft afslut? popup verification failed")
    clickButton(waitForObject(names.question_JA_QPushButton))
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

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Minimumslængden for profilnavne er 1 tegn ")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Minimumslængden for profilnavne er 1 tegn ": 
        test.passes("Minimumslængden for profilnavne er 1 tegn  warning popup is verified")
    else: test.fail("Minimumslængden for profilnavne er 1 tegn  warning popup verification failed")
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

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Profilnavnet \"thuvera\"<br>findes allerede.")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Profilnavnet \"thuvera\"<br>findes allerede.": 
        test.passes("Profilnavnet \"thuvera\"<br>findes allerede. warning popup is verified")
    else: test.fail("Profilnavnet \"thuvera\"<br>findes allerede. warning popup verification failed")
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
            waitForObjectExists(names.question_ANNULLER_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "DELETE PROFILE?",
            "OK",
            "CANCEL"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "SLET PROFIL?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "SLET PROFIL?": 
        test.passes("SLET PROFIL? popup is verified")
    else: test.fail("SLET PROFIL? popup verification failed")
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_thuveraaa_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    validate_assistant_label()
    validate_localization(
        objects=[
            waitForObjectExists(names.sclProfiles_Standard_ProfileButton),
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Default",
        ],
    )

    test.compare(str(waitForObjectExists(names.sclProfiles_Standard_ProfileButton).text), "Standard")
    if str(waitForObjectExists(names.sclProfiles_Standard_ProfileButton).text) == "Standard": 
        test.passes("Profile Screen verified")
    else: test.fail("Profile Screen verification failed")

        

    
