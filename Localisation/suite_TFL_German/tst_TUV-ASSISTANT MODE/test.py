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
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))

    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_BEHANDLUNGSART_WizardTitle),
            waitForObject(names.frWizardPlace_Lithotrypsie_WizardButton),
            waitForObject(names.frWizardPlace_Weichteilgewebe_WizardButton),
            waitForObject(names.frWizardPlace_BPH_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_Lithotrypsie_WizardButton))
    
    
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_BEREICH_WizardTitle),
            waitForObject(names.frWizardPlace_STEINGR_SSE_MM_WizardTitle),
            waitForObject(names.frWizardPlace_STEINDICHTE_HU_WizardTitle),
            waitForObject(names.frWizardPlace_Niere_WizardButton),
            waitForObject(names.frWizardPlace_Ureter_WizardButton),
            waitForObject(names.frWizardPlace_Harnblase_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_Niere_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_Title_QLabel), 271, 32, Qt.NoModifier, Qt.LeftButton)

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
    clickButton(waitForObject(names.frWizardPlace_Mittel_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Gro_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Unbekannt_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Weich_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mittel_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Hart_1000_WizardButton))

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Klein_6_WizardButton),
            waitForObject(names.frWizardPlace_Mittel_6_10_WizardButton),
            waitForObject(names.frWizardPlace_Gro_10_WizardButton),
            waitForObject(names.frWizardPlace_Unbekannt_WizardButton),
            waitForObject(names.frWizardPlace_Weich_500_WizardButton),
            waitForObject(names.frWizardPlace_Mittel_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_Hart_1000_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_Weichteilgewebe_WizardButton))
    
    validate_localization(
        objects=[

            waitForObject(names.frWizardPlace_PEDAL_LINKS_PEDAL_RECHTS_WizardTitle),
            waitForObject(names.frWizardPlace_Vaporisieren_H_mostase_WizardButton),
            waitForObject(names.frWizardPlace_Tumor_H_mostase_WizardButton),
            waitForObject(names.frWizardPlace_Inzision_H_mostase_WizardButton),
                   
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
    clickButton(waitForObject(names.frWizardPlace_Enukleation_Niedrige_Leistung_WizardButton))
    validate_localization(
        objects=[

            waitForObjectExists(names.frWizardPlace_WEITER_WizardApplyButton),
            waitForObject(names.frWizardPlace_Enukleation_H_mostase_WizardButton),
            waitForObject(names.frWizardPlace_Enukleation_Niedrige_Leistung_WizardButton),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )

    # clickButton(waitForObject(names.frWizardPlace_Enukleation_Niedrige_Leistung_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WEITER_WizardApplyButton))

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
            waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget),
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
    
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 15, 21, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
           
            waitForObjectExists(names.aivComboBoxPopup_Enukleation_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Niedrige_Leistung_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Dust_hoch_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Dust_niedrig_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Popcorn_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Fragment_hoch_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Fragment_niedrig_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Harnblasen_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Dust_QModelIndex_2),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostata_Enukleat_hoch_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostata_Enukleat_niedrig_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Gewebe_Vaporisation_gepulst_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Gewebe_Vaporisation_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Tumorablation_Exzision_QModelIndex),
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

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotrypsie_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Niere_WizardButton))
    
    test.compare(str(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).visible, True)
    test.log("Assistant Screen Verification")
    clickButton(waitForObject(names.frWizardPlace_WEITER_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 36, 23, Qt.NoModifier, Qt.LeftButton)  
     
    test.compare(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).windowIconText), "")
    test.log("Presets Color Verification in Assistant Treatment Screen")
    
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Dust_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Kidney Fragment",
            "Kidney Dust"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotrypsie_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Ureter_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WEITER_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 31, 22, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Ureter_Fragment_QModelIndex_2),
           waitForObjectExists(names.aivComboBoxPopup_Ureter_Dust_QModelIndex_2),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Ureter Fragment",
            "Ureter Dust"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotrypsie_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Harnblase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WEITER_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 27, 23, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
          waitForObjectExists(names.aivComboBoxPopup_Blasenfragmentierung_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Weichteilgewebe_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Vaporisieren_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WEITER_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 32, 32, Qt.NoModifier, Qt.LeftButton)
  
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Vaporisieren_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_H_mostase_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Vaporize",
            "Hemostasis"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Weichteilgewebe_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WEITER_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 25, 28, Qt.NoModifier, Qt.LeftButton)
   
    validate_localization(
        objects=[
            waitForObject(names.aivComboBoxPopup_Tumor_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Tumor"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Weichteilgewebe_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Inzision_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_WEITER_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 20, 27, Qt.NoModifier, Qt.LeftButton)
  
    validate_localization(
        objects=[
           waitForObject(names.aivComboBoxPopup_Inzision_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
