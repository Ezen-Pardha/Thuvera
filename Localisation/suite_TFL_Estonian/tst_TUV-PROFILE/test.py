# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 451, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Eesti (Estonia)"), 120, 36, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btHome_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObjectExists(names.question_JAH_QPushButton),
            waitForObjectExists(names.question_EI_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Confirm Exit?",
            "NO",
            "YES"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Kas kinnitada sulgemine?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Kas kinnitada sulgemine?": 
        test.passes("Kas kinnitada sulgemine? popup is verified")
    else: test.fail("Kas kinnitada sulgemine? popup verification failed")
    clickButton(waitForObject(names.question_JAH_QPushButton))
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
 
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Profiili nime miinimumpikkus on 1 märk ")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Profiili nime miinimumpikkus on 1 märk ": 
        test.passes("Profiili nime miinimumpikkus on 1 märk warning popup is verified")
    else: test.fail("Profiili nime miinimumpikkus on 1 märk warning popup verification failed")
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
            waitForObjectExists(names.apollo_TextLabel_QLabel),
            waitForObjectExists(names.warning_OK_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "The profile name \"XXXX\" already exists.",
            "OK"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Profiili nimi \"thuvera\"<br>on juba olemas.")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Profiili nimi \"thuvera\"<br>on juba olemas.": 
        test.passes("Profiili nimi \"thuvera\"<br>on juba olemas. warning popup is verified")
    else: test.fail("Profiili nimi \"thuvera\"<br>on juba olemas. warning popup verification failed")
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
            waitForObjectExists(names.question_T_HISTA_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "DELETE PROFILE?",
            "OK",
            "CANCEL"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "KAS KUSTUTADA PROFIIL?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "KAS KUSTUTADA PROFIIL?": 
        test.passes("KAS KUSTUTADA PROFIIL? popup is verified")
    else: test.fail("KAS KUSTUTADA PROFIIL? popup verification failed")
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_thuveraaa_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    validate_assistant_label()
    validate_localization(
        objects=[
            waitForObjectExists(names.sclProfiles_Vaikimisi_ProfileButton),
        ],
        screen_name="PROFILE",
        expected_strings=[
            "Default",
        ],
    )
    test.compare(str(waitForObjectExists(names.sclProfiles_Vaikimisi_ProfileButton).text), "Vaikimisi")
    if str(waitForObjectExists(names.sclProfiles_Vaikimisi_ProfileButton).text) == "Vaikimisi": 
        test.passes("Profile Screen verified")
    else: test.fail("Profile Screen verification failed")

        

    
