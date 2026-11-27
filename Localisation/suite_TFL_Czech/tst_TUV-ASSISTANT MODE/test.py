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
    clickButton(waitForObject(names.question_ANO_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 630, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_TYP_ZPRACOV_N_WizardTitle), 152, 14, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[

        waitForObjectExists(names.apollo_lbScreenTitle_QLabel),
        waitForObjectExists(names.frWizardPlace_TYP_ZPRACOV_N_WizardTitle),
        waitForObjectExists(names.frWizardPlace_Litotrypse_WizardButton),
        waitForObjectExists(names.frWizardPlace_M_kk_tk_WizardButton),
        waitForObjectExists(names.frWizardPlace_Benign_hypertrofie_prostaty_WizardButton)

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

    clickButton(waitForObject(names.frWizardPlace_Litotrypse_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_UM_ST_N_WizardTitle), 112, 21, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_VELIKOST_KAMENE_MM_WizardTitle), 104, 16, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_HUSTOTA_KAMENE_HU_WizardTitle), 124, 15, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Ledviny_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mo_ovod_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mo_ov_m_ch_WizardButton))

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_UM_ST_N_WizardTitle),
            waitForObject(names.frWizardPlace_VELIKOST_KAMENE_MM_WizardTitle),
            waitForObject(names.frWizardPlace_HUSTOTA_KAMENE_HU_WizardTitle),
            waitForObject(names.frWizardPlace_Ledviny_WizardButton),
            waitForObject(names.frWizardPlace_Mo_ovod_WizardButton),
            waitForObject(names.frWizardPlace_Mo_ov_m_ch_WizardButton),
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

    mouseClick(waitForObject(names.frWizardPlace_Title_QLabel), 221, 35, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Title_QLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "RECOMMENDED FIBER"
        ],
    )
    
    clickButton(waitForObject(names.frWizardPlace_Mal_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_St_edn_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Velk_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Nezn_m_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_M_kk_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_St_edn_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tvrd_1000_WizardButton))
    
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Mal_6_WizardButton),
            waitForObject(names.frWizardPlace_St_edn_6_10_WizardButton),
            waitForObject(names.frWizardPlace_Velk_10_WizardButton),
            waitForObject(names.frWizardPlace_Nezn_m_WizardButton),
            waitForObject(names.frWizardPlace_M_kk_500_WizardButton),
            waitForObject(names.frWizardPlace_St_edn_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_Tvrd_1000_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_M_kk_tk_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_LEV_PED_L_PRAV_PED_L_WizardTitle), 144, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_LEV_PED_L_PRAV_PED_L_WizardTitle), 376, 14, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Odpa_ovat_Hemost_za_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_N_dor_Hemost_za_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incize_Hemost_za_WizardButton))

    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_LEV_PED_L_PRAV_PED_L_WizardTitle),
            waitForObject(names.frWizardPlace_Odpa_ovat_Hemost_za_WizardButton),
            waitForObject(names.frWizardPlace_N_dor_Hemost_za_WizardButton),
            waitForObject(names.frWizardPlace_Incize_Hemost_za_WizardButton),
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

    clickButton(waitForObject(names.frWizardPlace_Benign_hypertrofie_prostaty_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleace_Hemost_za_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleace_N_zk_v_kon_WizardButton))
    
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Enukleace_Hemost_za_WizardButton),
            waitForObject(names.frWizardPlace_Enukleace_N_zk_v_kon_WizardButton),
            waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
            
        ],
    )

    clickButton(waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_lbHeader_QLabel), 42, 7, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 64, 6, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPower_QLabel), 26, 9, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbPulsedMode_QToolButton))
    clickButton(waitForObject(names.centralWidget_pbCwMode_QToolButton))
    mouseClick(waitForObject(names.centralWidget_lbDualPulse_QLabel), 48, 33, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPulseWidth_QLabel), 101, 32, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 133, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 76, 43, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 121, 48, Qt.NoModifier, Qt.LeftButton)
    
    validate_aiming_beam_label()

    validate_localization(
        objects=[
            
            waitForObject(names.centralWidget_lbHeader_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbPower_QLabel),
            waitForObject(names.centralWidget_pbPulsedMode_QToolButton),
            waitForObject(names.centralWidget_pbCwMode_QToolButton),
            waitForObject(names.centralWidget_lbDualPulse_QLabel),
            waitForObject(names.centralWidget_lbPulseWidth_QLabel),
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

    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 34, 23, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[

            waitForObjectExists(names.aivComboBoxPopup_Enukleace_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_N_zk_v_kon_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ledvinov_prach_vysok_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ledvinov_prach_n_zk_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ledvinov_ste_ky_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ledvinov_fragment_vysok_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ledvinov_fragment_n_zk_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Mo_ovod_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prach_v_mo_ovodu_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Fragment_mo_ov_ho_m_ch_e_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Enukleace_prostaty_vysok_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Enukleace_prostaty_n_zk_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Odpa_ov_n_tk_n_pulzn_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Odpa_ov_n_tk_n_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ablace_excize_n_doru_QModelIndex),
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
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 36, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_ANO_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))

    clickButton(waitForObject(names.frWizardPlace_Litotrypse_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Ledviny_WizardButton))

    test.compare(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_WizardScreen_WizardScreen).windowIconText), "")
    test.log("Assistant Screen Verification")
    clickButton(waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 33, 30, Qt.NoModifier, Qt.LeftButton)

    test.compare(str(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_aivComboBoxPopup_QTreeView).visible, True)
    test.log("Presets Color Verification in Assistant Treatment Screen")
    
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Ledvinov_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ledvinov_prach_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Kidney Fragment",
            "Kidney Dust"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 23, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_ANO_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotrypse_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mo_ovod_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 30, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Mo_ovod_fragment_QModelIndex_2),
           waitForObjectExists(names.aivComboBoxPopup_Prach_v_mo_ovodu_QModelIndex),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Ureter Fragment",
            "Ureter Dust"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 32, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_ANO_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotrypse_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mo_ov_m_ch_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 26, 21, Qt.NoModifier, Qt.LeftButton)
    
   
    validate_localization(
        objects=[
          waitForObjectExists(names.aivComboBoxPopup_Fragmentace_mo_ov_ho_m_ch_e_QModelIndex),
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 33, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_ANO_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_M_kk_tk_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Odpa_ovat_Hemost_za_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 20, 22, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Odpa_ovat_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Hemost_za_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Vaporize",
            "Hemostasis"
        ],
    )
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 24, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_ANO_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_M_kk_tk_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_N_dor_Hemost_za_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 32, 30, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(
        objects=[
            waitForObject(names.aivComboBoxPopup_N_dor_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Tumor",
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 23, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_ANO_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_M_kk_tk_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incize_Hemost_za_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_POSTUPOVAT_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 29, 33, Qt.NoModifier, Qt.LeftButton)

    validate_localization(
        objects=[
           waitForObject(names.aivComboBoxPopup_Incize_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 23, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_ANO_QPushButton))
