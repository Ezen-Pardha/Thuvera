# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 471, 39, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Nederlands (The Netherlands)"), 177, 47, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 631, 13, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_TYPE_BEHANDELING_WizardTitle), 149, 21, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_TYPE_BEHANDELING_WizardTitle),
            waitForObject(names.frWizardPlace_Lithotripsie_WizardButton),
            waitForObject(names.frWizardPlace_Weke_delen_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_Lithotripsie_WizardButton))

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_LOCATIE_WizardTitle),
            waitForObject(names.frWizardPlace_STEENGROOTTE_MM_WizardTitle),
            waitForObject(names.frWizardPlace_STEENDICHTHEID_HU_WizardTitle),
            waitForObject(names.frWizardPlace_Nier_WizardButton),
            waitForObject(names.frWizardPlace_Ureter_WizardButton),
            waitForObject(names.frWizardPlace_Blaas_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_Nier_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_Title_QLabel), 298, 47, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Title_QLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "RECOMMENDED FIBER"
        ],
    )
    
    clickButton(waitForObject(names.frWizardPlace_Klein_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Medium_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Groot_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Onbekend_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Zacht_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Hard_1000_WizardButton))

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Klein_6_WizardButton),
            waitForObject(names.frWizardPlace_Medium_6_10_WizardButton),
            waitForObject(names.frWizardPlace_Groot_10_WizardButton),
            waitForObject(names.frWizardPlace_Onbekend_WizardButton),
            waitForObject(names.frWizardPlace_Zacht_500_WizardButton),
            waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_Hard_1000_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_Weke_delen_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_PEDAAL_LINKS_PEDAAL_RECHTS_WizardTitle), 143, 20, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_PEDAAL_LINKS_PEDAAL_RECHTS_WizardTitle), 360, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Verdampen_Hemostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incisie_Hemostase_WizardButton))

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_PEDAAL_LINKS_PEDAAL_RECHTS_WizardTitle),
            waitForObject(names.frWizardPlace_Verdampen_Hemostase_WizardButton),
            waitForObject(names.frWizardPlace_Tumor_Hemostase_WizardButton),
            waitForObject(names.frWizardPlace_Incisie_Hemostase_WizardButton),
            waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton),
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
    clickButton(waitForObject(names.frWizardPlace_Enucleatie_Hemostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enucleatie_Laag_vermogen_WizardButton))
       
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton),
            waitForObjectExists(names.frWizardPlace_Enucleatie_Hemostase_WizardButton),
            waitForObjectExists(names.frWizardPlace_Enucleatie_Laag_vermogen_WizardButton),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )

    clickButton(waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_lbHeader_QLabel), 48, 8, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 74, 6, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPower_QLabel), 72, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbDualPulse_QLabel), 33, 33, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPulseWidth_QLabel), 112, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbPulsedMode_QToolButton))
    clickButton(waitForObject(names.centralWidget_pbCwMode_QToolButton))
    mouseClick(waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget), 422, 457, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 152, 41, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 122, 36, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 179, 41, Qt.NoModifier, Qt.LeftButton)

    validate_aiming_beam_label()
    
    validate_localization(
        objects=[
            waitForObject(names.centralWidget_lbHeader_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbPower_QLabel),
            waitForObject(names.centralWidget_lbDualPulse_QLabel),
            waitForObject(names.centralWidget_lbPulseWidth_QLabel),
            waitForObject(names.centralWidget_pbPulsedMode_QToolButton),
            waitForObject(names.centralWidget_pbCwMode_QToolButton),
            waitForObject(names.stateSwitch_lbStandby_QLabel),
            waitForObject(names.stateSwitch_lbReady_QLabel),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "ENERGY (J)",
            "FREQUENCY (Hz)",
            "POWER (W)",
            "PULSE WIDTH",
            "PULSED",
            "CW",
            "READY",
            "STANDBY"
        ],
    )
    
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 34, 18, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Enucleatie_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Laag_vermogen_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Niergruis_hoog_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Niergruis_laag_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Niersteenfragmenten_met_popcornstructuur_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nierfragment_Hoog_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nierfragment_Laag_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Uretergruis_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Blaasfragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostaatenucleatie_hoog_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostaatenucleatie_laag_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Weefsel_verdampen_gepulseerd_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Weefsel_verdampen_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Tumorablatie_excisie_QModelIndex),
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

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 17, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsie_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Nier_WizardButton))

    test.compare(str(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).visible, True)
    test.log("Assistant Screen Verification")
    
    clickButton(waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 25, 34, Qt.NoModifier, Qt.LeftButton)

    test.compare(str(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).visible, True)
    test.log("Presets Color Verification in Assistant Treatment Screen")
    
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Nierfragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Niergruis_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Kidney Fragment",
            "Kidney Dust"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 8, 31, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsie_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Ureter_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 28, 25, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Ureter_Fragment_QModelIndex_2),
           waitForObjectExists(names.aivComboBoxPopup_Uretergruis_QModelIndex),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Ureter Fragment",
            "Ureter Dust"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 33, 29, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))

    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsie_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Blaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 32, 32, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
          waitForObjectExists(names.aivComboBoxPopup_Blaasfragmentatie_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 30, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Weke_delen_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Verdampen_Hemostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 19, 25, Qt.NoModifier, Qt.LeftButton)
   
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Verdampen_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Hemostase_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Vaporize",
            "Hemostasis"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 27, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Weke_delen_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 28, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObject(names.aivComboBoxPopup_Tumor_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Tumor",
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 23, 31, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Weke_delen_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incisie_Hemostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_OPVOEREN_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 33, 24, Qt.NoModifier, Qt.LeftButton)    
    
    validate_localization(
        objects=[
           waitForObject(names.aivComboBoxPopup_Incisie_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 31, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    
    test.compare(waitForObjectExists(names.apollo_ProfileSelectionScreen_ProfileSelectionScreen).visible, True)
    test.log("Screen Verification")

    
