# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_presets()
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel_2), 541, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbName_QLabel), 24, 9, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.pagesWidget_lbHeader_QLabel), 48, 5, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 60, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.pagesWidget_lbPower_QLabel), 53, 5, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.pagesWidget_lbPulseWidth_QLabel), 158, 41, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btCwMode_QToolButton))
    test.compare(str(waitForObjectExists(names.apollo_btCwMode_QToolButton).text), "CW")
    if str(waitForObjectExists(names.apollo_btCwMode_QToolButton).text) == "CW": 
        test.passes("Add Preset CW Screen verified")
    else: test.fail("Add Preset CW Screen verification failed")
    clickButton(waitForObject(names.apollo_btPulsedMode_QToolButton))
    test.compare(str(waitForObjectExists(names.apollo_btPulsedMode_QToolButton).text), "PULSED")
    if str(waitForObjectExists(names.apollo_btPulsedMode_QToolButton).text) == "PULSED": 
        test.passes("Add Preset PULSED Screen verified")
    else: test.fail("Add Preset PULSED Screen verification failed")
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel_2),
            waitForObject(names.apollo_lbName_QLabel), 24, 9,
            waitForObject(names.pagesWidget_lbHeader_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.pagesWidget_lbPower_QLabel),
            waitForObject(names.pagesWidget_lbPulseWidth_QLabel),
            waitForObject(names.apollo_btPulsedMode_QToolButton),
            waitForObject(names.apollo_btCwMode_QToolButton)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "CREATE A PRESET",
            "NAME",
            "ENERGY (J)",
            "FREQUENCY (Hz)",
            "POWER (W)",
            "PULSE WIDTH",
            "PULSED",
            "CW" 
        ],
    )

    mouseClick(waitForObject(names.apollo_edName_QLineEdit), 87, 20, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.apollo_edName_QLineEdit).placeholderText), "ADD NAME")
    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_edName_QLineEdit)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "ADD NAME"
        ],
    )
    clickButton(waitForObject(names.keyboardFrame_p_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    validate_localization(
        objects=[
            waitForObjectExists(names.keyboardFrame_Enter_KeyButtonEnter),
            waitForObjectExists(names.keyboardFrame_Cancel_KeyButtonCancel)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "Enter",
            "Cancel"
        ],
    )
    
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.apollo_btSave_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
    mouseClick(waitForObject(names.apollo_edName_QLineEdit), 87, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.keyboardFrame_p_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_btSave_QPushButton),
            waitForObjectExists(names.apollo_btCancel_QPushButton)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "SAVE",
            "CANCEL"
        ],
    )
    
    clickButton(waitForObject(names.apollo_btSave_QPushButton))
    mouseClick(waitForObject(names.warning_TextLabel_QLabel), 382, 48, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.warning_TextLabel_QLabel),
            waitForObjectExists(names.warning_OK_QPushButton)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            'The preset name "XXXX" already exists.',
            "OK"
        ],
    )
    
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "The preset name \"preset\" already exists.")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "The preset name \"preset\" already exists.": 
        test.passes("The preset name \"preset\" already exists. warning popup verified")
    else: test.fail("The preset name \"preset\" already exists. warning popup verification failed")
    clickButton(waitForObject(names.warning_OK_QPushButton))
    mouseClick(waitForObject(names.apollo_edName_QLineEdit), 156, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonSpace))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.apollo_btSave_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
    mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "preset 1"), 69, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.question_TextLabel_QLabel), 103, 26, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.question_TextLabel_QLabel),
            waitForObjectExists(names.question_OK_QPushButton),
            waitForObjectExists(names.question_CANCEL_QPushButton)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "DELETE PRESET",
            "OK",
            "CANCEL"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "DELETE PRESET<br>preset 1?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "DELETE PRESET<br>preset 1?": 
        test.passes("DELETE PRESET<br>preset 1? verified")
    else: test.fail("DELETE PRESET<br>preset 1? verification failed")
    clickButton(waitForObject(names.question_CANCEL_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
    clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
    mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "preset 1"), 44, 30, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
    mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "preset"), 81, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
