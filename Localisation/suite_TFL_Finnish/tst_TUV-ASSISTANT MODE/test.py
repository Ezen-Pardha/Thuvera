# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 404, 43, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "suomi (Finland)"), 128, 33, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))

    validate_localization(
        objects=[

            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_HOIDON_TYYPPI_WizardTitle),
            waitForObject(names.frWizardPlace_litotripsia_WizardButton),
            waitForObject(names.frWizardPlace_pehmyt_kudos_WizardButton),
            waitForObject(names.frWizardPlace_Hyv_nlaatuinen_eturauhasen_liikakasvu_BPH_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_litotripsia_WizardButton))
    

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_SIJAINTI_WizardTitle),
            waitForObject(names.frWizardPlace_KIVEN_KOKO_mm_WizardTitle),
            waitForObject(names.frWizardPlace_KIVEN_TIHEYS_HU_WizardTitle),
            waitForObject(names.frWizardPlace_munuainen_WizardButton),
            waitForObject(names.frWizardPlace_virtsaputki_WizardButton),
            waitForObject(names.frWizardPlace_virtsarakko_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_munuainen_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_Title_QLabel), 256, 28, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Title_QLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "RECOMMENDED FIBER"
        ],
    )
    
    clickButton(waitForObject(names.frWizardPlace_pieni_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_keskikokoinen_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_suuri_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_tuntematon_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_pehme_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_keskikokoinen_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_kova_1000_WizardButton))

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_pieni_6_WizardButton),
            waitForObject(names.frWizardPlace_keskikokoinen_6_10_WizardButton),
            waitForObject(names.frWizardPlace_suuri_10_WizardButton),
            waitForObject(names.frWizardPlace_tuntematon_WizardButton),
            waitForObject(names.frWizardPlace_pehme_500_WizardButton),
            waitForObject(names.frWizardPlace_keskikokoinen_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_kova_1000_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_pehmyt_kudos_WizardButton))

    validate_localization(
        objects=[

            waitForObject(names.frWizardPlace_VASEMMANPUOLEINEN_POLJIN_OIKEANPUOLEINEN_POLJIN_WizardTitle),
            waitForObject(names.frWizardPlace_h_yrysty_hemostaasi_WizardButton),
            waitForObject(names.frWizardPlace_tuumori_hemostaasi_WizardButton),
            waitForObject(names.frWizardPlace_viilto_hemostaasi_WizardButton),
                   
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

    clickButton(waitForObject(names.frWizardPlace_Hyv_nlaatuinen_eturauhasen_liikakasvu_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_enukleaatio_hemostaasi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_enukleaatio_pieni_teho_WizardButton))

    validate_localization(
        objects=[
            waitForObjectExists(names.frWizardPlace_ENNAKKO_WizardApplyButton),
            waitForObject(names.frWizardPlace_enukleaatio_hemostaasi_WizardButton),
            waitForObject(names.frWizardPlace_enukleaatio_pieni_teho_WizardButton),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )

    clickButton(waitForObject(names.frWizardPlace_ENNAKKO_WizardApplyButton))

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
    
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 35, 29, Qt.NoModifier, Qt.LeftButton)
  
    validate_localization(
        objects=[
           
            waitForObjectExists(names.aivComboBoxPopup_enukleaatio_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_pieni_teho_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Munuaiskivihiukkaset_paljon_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Munuaiskivihiukkaset_v_h_n_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Munuaispopcorn_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Munuaiskivipalat_paljon_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Munuaiskivipalat_v_h_n_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Eturauhasen_enukleaatio_suuri_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Eturauhasen_enukleaatio_pieni_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kudoken_h_yrystys_pulssinen_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kudoksen_h_yrystys_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Tuumorin_ablaatio_poistaminen_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Hiukkaset_virtsaputkessa_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Pala_virtsarakossa_QModelIndex),
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

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 23, 19, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_munuainen_WizardButton))
    
    test.compare(str(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).visible, True)
    test.log("Assistant Screen Verification")
    
    clickButton(waitForObject(names.frWizardPlace_ENNAKKO_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 27, Qt.NoModifier, Qt.LeftButton)

    test.compare(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).windowIconText), "")
    test.log("Presets Color Verification in Assistant Screen")
   
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Munuaiskivipalat_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Munuaiskivihiukkaset_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Kidney Fragment",
            "Kidney Dust"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 18, 23, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_virtsaputki_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ENNAKKO_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 24, 18, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Virtsaputki_pala_QModelIndex_2),
           waitForObjectExists(names.aivComboBoxPopup_Hiukkaset_virtsaputkessa_QModelIndex),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Ureter Fragment",
            "Ureter Dust"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 26, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_virtsarakko_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ENNAKKO_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 16, 28, Qt.NoModifier, Qt.LeftButton)
   
    validate_localization(
        objects=[
          waitForObjectExists(names.aivComboBoxPopup_Virtsarakon_pirstoutuminen_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 24, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_pehmyt_kudos_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_h_yrysty_hemostaasi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ENNAKKO_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 26, 34, Qt.NoModifier, Qt.LeftButton)
   
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_h_yrysty_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_hemostaasi_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Vaporize",
            "Hemostasis"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 24, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_pehmyt_kudos_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_tuumori_hemostaasi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ENNAKKO_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 28, 28, Qt.NoModifier, Qt.LeftButton)
   
    validate_localization(
        objects=[
            waitForObject(names.aivComboBoxPopup_tuumori_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Tumor"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 24, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))

    clickButton(waitForObject(names.frWizardPlace_pehmyt_kudos_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_viilto_hemostaasi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ENNAKKO_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 18, 26, Qt.NoModifier, Qt.LeftButton)
  
    validate_localization(
        objects=[
           waitForObject(names.aivComboBoxPopup_viilto_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 24, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_KYLL_QPushButton))
