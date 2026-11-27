# -*- coding: utf-8 -*-
import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 480, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "čeština (Czech Republic)"), 181, 43, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    
    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_TextLabel_QLabel),
            waitForObjectExists(names.question_ANO_QPushButton),
            waitForObjectExists(names.question_NE_QPushButton)

        ],
        screen_name="PROFILE",
        expected_strings=[
            "Confirm Exit?",
            "NO",
            "YES"
        ],
    )

    clickButton(waitForObject(names.question_ANO_QPushButton))
    test.compare(str(waitForObjectExists(names.sclProfiles_V_choz_ProfileButton).text), "Výchozí")
    test.compare(str(waitForObjectExists(names.sclProfiles_V_choz_ProfileButton).windowIconText), "")
    test.compare(waitForObjectExists(names.sclProfiles_V_choz_ProfileButton).visible, True)
    test.log("Profile screen Verification")
    
    validate_assistant_label()
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

    validate_localization(
        objects=[

            waitForObject(names.apollo_TextLabel_QLabel),
            waitForObjectExists(names.warning_OK_QPushButton)
        ],
        screen_name="PROFILE",
        expected_strings=[
            "The minimum profile name length is 1 character",
            "OK"
        ],
    )
    clickButton(waitForObject(names.warning_OK_QPushButton))

    clickButton(waitForObject(names.keyboardFrame_123_sla_KeyButtonNumSwitch))
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
    clickButton(waitForObject(names.keyboardFrame_123_sla_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_12345_ProfileButton))

    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObjectExists(names.question_OK_QPushButton),
            waitForObjectExists(names.question_ZRU_IT_QPushButton),
        ],
        screen_name="PROFILE",
        expected_strings=[
            "DELETE PROFILE?",
            "OK",
            "CANCEL"
        ],
    )
 
    clickButton(waitForObject(names.question_ZRU_IT_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_123_sla_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
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
    
    clickButton(waitForObject(names.warning_OK_QPushButton))
    clickButton(waitForObject(names.keyboardFrame_Cancel_KeyButtonCancel))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_12345_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
