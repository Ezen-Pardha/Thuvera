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
    
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbAddPreset_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel_2), 541, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbName_QLabel), 24, 9, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.pagesWidget_lbHeader_QLabel), 48, 5, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 60, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.pagesWidget_lbPower_QLabel), 53, 5, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.pagesWidget_lbPulseWidth_QLabel), 158, 41, Qt.NoModifier, Qt.LeftButton)

    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel_2).text), "VYTVOŘIT PŘEDVOLBU")
    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_centralWidget_QWidget).windowIconText), "")
    test.log("Presets - Pulsed Mode Screen Property Verification")
    clickButton(waitForObject(names.apollo_btCwMode_QToolButton))

    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel_2).text), "VYTVOŘIT PŘEDVOLBU")
    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_centralWidget_QWidget).windowIconText), "")
    test.log("Presets - CW Mode Screen Property Verification")
    clickButton(waitForObject(names.apollo_btPulsedMode_QToolButton))
     
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
    waitForObjectExists(names.apollo_edName_QLineEdit).placeholderText, "ADD NAME",
    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_edName_QLineEdit)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "ADD NAME"
        ],
    )

    clickButton(waitForObject(names.keyboardFrame_123_sla_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    
    validate_localization(
        objects=[
            waitForObject(names.keyboardFrame_Enter_KeyButtonEnter),
            waitForObject(names.apollo_btCancel_QPushButton)
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
    mouseClick(waitForObject(names.apollo_edName_QLineEdit), 287, 15, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.keyboardFrame_123_sla_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    validate_localization(
        objects=[

            waitForObject(names.apollo_btSave_QPushButton),
            waitForObject(names.apollo_btCancel_QPushButton)
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "SAVE",
            "CANCEL"
        ],
    )
    
    clickButton(waitForObject(names.apollo_btSave_QPushButton))
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 544, 51, Qt.NoModifier, Qt.LeftButton)

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

    clickButton(waitForObject(names.warning_OK_QPushButton))
    clickButton(waitForObject(names.apollo_btCancel_QPushButton))
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 1067, 20, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 1067, 20, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 1067, 19, -120, 0, 2)

    clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
    mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "0\\.10000000149011612_1"), 54, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 355, 20, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObjectExists(names.apollo_TextLabel_QLabel),
            waitForObject(names.question_ZRU_IT_QPushButton),
            waitForObjectExists(names.question_OK_QPushButton)
            
        ],
        screen_name="ADD PRESET",
        expected_strings=[
            "DELETE PRESET",
            "OK",
            "CANCEL"
        ],
    )

    clickButton(waitForObject(names.question_OK_QPushButton))
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 671, 215, -120, 0, 2)
