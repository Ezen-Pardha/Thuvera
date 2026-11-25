
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
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Български (Bulgaria)"), 130, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 630, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_WizardTitle_2), 153, 14, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_WizardTitle_2),
            waitForObject(names.frWizardPlace_WizardButton),
            waitForObject(names.frWizardPlace_WizardButton_3),
            waitForObject(names.frWizardPlace_BPH_WizardButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "ASSISTANT",
            "TREATMENT TYPE",
            "Lithotripsy",
            "Soft Tissue",
            "BPH"
        ],
    )
    clickButton(waitForObject(names.frWizardPlace_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_3))
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_WizardTitle),
            waitForObject(names.frWizardPlace_MM_WizardTitle),
            waitForObject(names.frWizardPlace_HU_WizardTitle),
            waitForObject(names.frWizardPlace_WizardButton_2),
            waitForObject(names.frWizardPlace_WizardButton_9),
            waitForObject(names.frWizardPlace_WizardButton_6)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "LOCATION",
            "STONE SIZE (MM)",
            "STONE DENSITY (HU)",
            "Kidney",
            "Ureter",
            "Bladder"
        ],
    )
    mouseClick(waitForObject(names.frWizardPlace_WizardTitle), 92, 16, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_MM_WizardTitle), 103, 17, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_HU_WizardTitle), 88, 13, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_WizardButton_2))
    mouseClick(waitForObject(names.frWizardPlace_Title_QLabel), 213, 33, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Title_QLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "RECOMMENDED FIBER"
        ],
    )
    
    clickButton(waitForObject(names.frWizardPlace_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardTitle_3))
    clickButton(waitForObject(names.frWizardPlace_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_7))
    clickButton(waitForObject(names.frWizardPlace_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_9))


    clickButton(waitForObject(names.frWizardPlace_WizardButton_6))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_6_WizardButton),
            waitForObject(names.frWizardPlace_WizardTitle_3),
            waitForObject(names.frWizardPlace_10_WizardButton),
            waitForObject(names.frWizardPlace_WizardButton_7),
            waitForObjectExists(names.frWizardPlace_500_WizardButton),
            # waitForObject(names.frWizardPlace_500_WizardButton),
            waitForObject(names.frWizardPlace_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_1000_WizardButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Small",
            "Medium",
            "Large",
            "Unknown",
            "Soft",
            "Medium",
            "Hard"
        ],
    )
    clickButton(waitForObject(names.frWizardPlace_WizardButton_3))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_10))
    mouseClick(waitForObject(names.frWizardPlace_WizardTitle_4), 126, 14, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_WizardTitle_4), 375, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_WizardButton_4))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_11))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_10))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_WizardButton_10),
            waitForObject(names.frWizardPlace_WizardTitle_4),
            waitForObject(names.frWizardPlace_WizardTitle_4),
            waitForObject(names.frWizardPlace_WizardButton_4),
            waitForObject(names.frWizardPlace_WizardButton_11),
            waitForObject(names.frWizardPlace_WizardButton_10)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "LEFT PEDAL",
            "RIGHT PEDAL",
            "Vaporize",
            "Tumor",
            "Incision",
            "Hemostasis"
        ],
    )
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_5))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_12))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_WizardButton_5),
            waitForObjectExists(names.frWizardPlace_WizardApplyButton),
            waitForObject(names.frWizardPlace_WizardButton_12)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )

    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_lbHeader_QLabel), 36, 1, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 77, 4, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPower_QLabel), 57, 8, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPulseWidth_QLabel), 47, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbPulsedMode_QToolButton))
    clickButton(waitForObject(names.centralWidget_pbCwMode_QToolButton))
    mouseClick(waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget), 416, 461, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 114, 36, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 205, 50, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.centralWidget_lbHeader_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbPower_QLabel),
            waitForObject(names.centralWidget_lbPulseWidth_QLabel),
            waitForObject(names.centralWidget_pbPulsedMode_QToolButton),
            waitForObject(names.centralWidget_pbCwMode_QToolButton),
            waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget),
            waitForObject(names.stateSwitch_lbReady_QLabel),
            waitForObject(names.stateSwitch_lbStandby_QLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "ENERGY (J)",
            "FREQUENCY (Hz)",
            "POWER (W)",
            "PULSE WIDTH",
            "PULSED",
            "CW",
            "AIMING BEAM",
            "READY",
            "STANDBY"
        ],
    )
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 114, 19, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Енуклеация"), 104, 31, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 26, 24, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_2),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_3),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_4),
            waitForObjectExists(names.aivComboBoxPopup_Popcorn_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_5),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_6),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_7),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_8),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_9),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_10),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_11),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_12),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_13),
            waitForObjectExists(names.aivComboBoxPopup_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_14)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "Kidney Dust (High)",
            "Kidney Dust (Low)",
            "Kidney Popcorn",
            "Kidney Fragment (High)",
            "Kidney Fragment (Low)",
            "Ureter (Fragment)",
            "Ureter Dust",
            "Bladder Fragment",
            "COAG",
            "Prostate Enucleate (High)",
            "Prostate Enucleate (Low)",
            "Tissue Vaporize (Pulsed)",
            "Tissue Vaporize (CW)",
            "Tumor Ablation/Excision"
        ],
    )
    mouseClick(waitForObject(names.apollo_frmComboBoxHeader_ComboBoxTwin), 289, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_2))
    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 29, 11, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_15),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_16)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Kidney Fragment",
            "Kidney Dust"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 10, 29, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_9))
    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 7, 23, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_QModelIndex_17),
           waitForObjectExists(names.aivComboBoxPopup_QModelIndex_8)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Ureter Fragment",
            "Ureter Dust"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 33, 29, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_6))
    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 38, 34, Qt.NoModifier, Qt.LeftButton)
   
    validate_localization(
        objects=[
          waitForObjectExists(names.aivComboBoxPopup_QModelIndex_18)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 20, 18, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_3))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_10))
    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 27, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_19),
            waitForObjectExists(names.aivComboBoxPopup_QModelIndex_20)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Vaporize",
            "Hemostasis"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 24, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))

    mouseClick(waitForObject(names.question_TextLabel_QLabel), 158, 13, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_3))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_4))
    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 37, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Тумор"), 49, 31, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_3))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_4))
    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 36, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Тумор"), 34, 39, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Tumor",
        ],
    )
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))

    clickButton(waitForObject(names.frWizardPlace_WizardButton_3))
    clickButton(waitForObject(names.frWizardPlace_WizardButton_11))
    clickButton(waitForObject(names.frWizardPlace_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 31, 27, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Разрез"), 51, 32, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
           waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_QPushButton))
    
