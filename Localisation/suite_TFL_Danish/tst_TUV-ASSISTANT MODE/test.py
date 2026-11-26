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
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 635, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_BEHANDLINGSTYPE_WizardTitle), 165, 16, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_BEHANDLINGSTYPE_WizardTitle),
            waitForObject(names.frWizardPlace_Litotripsi_WizardButton),
            waitForObject(names.frWizardPlace_Bl_dt_v_v_WizardButton),
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
    
    clickButton(waitForObject(names.frWizardPlace_Litotripsi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bl_dt_v_v_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsi_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_PLACERING_WizardTitle),
            waitForObject(names.frWizardPlace_STENST_RRELSE_MM_WizardTitle),
            waitForObject(names.frWizardPlace_STENDENSITET_HU_WizardTitle),
            waitForObject(names.frWizardPlace_Nyre_WizardButton),
            waitForObject(names.frWizardPlace_Urinleder_WizardButton),
            waitForObject(names.frWizardPlace_Bl_re_WizardButton)
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
    
    mouseClick(waitForObject(names.frWizardPlace_PLACERING_WizardTitle), 133, 20, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_STENST_RRELSE_MM_WizardTitle), 198, 20, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_STENDENSITET_HU_WizardTitle), 115, 10, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Nyre_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_Title_QLabel), 238, 37, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Title_QLabel)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "RECOMMENDED FIBER"
        ],
    )
    
    clickButton(waitForObject(names.frWizardPlace_Lille_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Middel_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Stor_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Ukendt_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bl_d_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Middel_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_H_rd_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Urinleder_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bl_re_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Lille_6_WizardButton),
            waitForObject(names.frWizardPlace_Middel_6_10_WizardButton),
            waitForObject(names.frWizardPlace_Stor_10_WizardButton),
            waitForObject(names.frWizardPlace_Ukendt_WizardButton),
            waitForObject(names.frWizardPlace_Bl_d_500_WizardButton),
            waitForObject(names.frWizardPlace_Middel_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_H_rd_1000_WizardButton)
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

    test.compare(str(waitForObjectExists(names.frWizardPlace_PLACERING_WizardTitle).text), "PLACERING")
    if str(waitForObjectExists(names.frWizardPlace_PLACERING_WizardTitle).text) == "PLACERING": 
        test.passes("Assistant Lithotripsy Screen verified")
    else: test.fail("Assistant Lithotripsy Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_Bl_dt_v_v_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_VENSTRE_PEDAL_H_JRE_PEDAL_WizardTitle), 154, 16, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_VENSTRE_PEDAL_H_JRE_PEDAL_WizardTitle), 363, 15, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Fordamp_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incision_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Fordamp_H_mostase_WizardButton))  
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_VENSTRE_PEDAL_H_JRE_PEDAL_WizardTitle),
            waitForObject(names.frWizardPlace_VENSTRE_PEDAL_H_JRE_PEDAL_WizardTitle),
            waitForObject(names.frWizardPlace_Fordamp_H_mostase_WizardButton),
            waitForObject(names.frWizardPlace_Tumor_H_mostase_WizardButton),
            waitForObject(names.frWizardPlace_Incision_H_mostase_WizardButton),
            waitForObject(names.frWizardPlace_Fordamp_H_mostase_WizardButton)
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
    
    test.compare(str(waitForObjectExists(names.frWizardPlace_Fordamp_H_mostase_WizardButton).text), "Fordamp|H_mostase")
    if str(waitForObjectExists(names.frWizardPlace_Fordamp_H_mostase_WizardButton).text) == "Fordamp|H_mostase": 
        test.passes("Assistant Soft Tissue Screen verified")
    else: test.fail("Assistant Soft Tissue Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleation_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleation_Lav_effekt_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Enukleation_H_mostase_WizardButton),
            waitForObject(names.frWizardPlace_Enukleation_Lav_effekt_WizardButton),
            waitForObject(names.frWizardPlace_FREM_WizardApplyButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )

    test.compare(str(waitForObjectExists(names.frWizardPlace_Enukleation_Lav_effekt_WizardButton).text), "Enukleation|Lav effekt")
    if str(waitForObjectExists(names.frWizardPlace_Enukleation_Lav_effekt_WizardButton).text) == "Enukleation|Lav effekt": 
        test.passes("Assistant BPH Screen verified")
    else: test.fail("Assistant BPH Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_lbHeader_QLabel), 52, 8, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 24, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPower_QLabel), 39, 5, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPulseWidth_QLabel), 137, 37, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbPulsedMode_QToolButton))
    clickButton(waitForObject(names.centralWidget_pbCwMode_QToolButton))
    mouseClick(waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget), 457, 469, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 179, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 119, 28, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.centralWidget_lbHeader_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbPower_QLabel),
            waitForObject(names.centralWidget_lbPulseWidth_QLabel),
            waitForObject(names.centralWidget_pbPulsedMode_QToolButton),
            waitForObject(names.centralWidget_pbCwMode_QToolButton),
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
            "READY",
            "STANDBY"
        ],
    )
    
    validate_aiming_beam_label()
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 47, 25, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Enukleation"), 68, 35, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 26, 24, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Enukleation_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Lav_effekt_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nyregrus_h_jt_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nyregrus_lavt_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Sm_nyresten_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nyrestensfragment_h_jt_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nyrestensfragment_lavt_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Urinleder_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Urenledergrus_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bl_refragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostataenukleat_h_jt_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostataenukleat_lavt_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_V_vsfordampning_pulseret_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_V_vsfordampning_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ablation_excision_af_tumor_QModelIndex)
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
    
    test.vp("Verifying BPH Advanced")
    mouseClick(waitForObject(names.apollo_frmComboBoxHeader_ComboBoxTwin), 289, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Nyre_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 31, 23, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Nyrestensfragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nyregrus_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Kidney Fragment",
            "Kidney Dust"
        ],
    )
    
    test.vp("Verifying Lithotripsy Kidney Adv ")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 10, 29, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Urinleder_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 28, 32, Qt.NoModifier, Qt.LeftButton)      
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Urinleder_fragment_QModelIndex_2),
            waitForObjectExists(names.aivComboBoxPopup_Urenledergrus_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Ureter Fragment",
            "Ureter Dust"
        ],
    )

    test.vp("Verifying Lithotripsy Ureter Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 33, 29, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bl_re_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 396, 19, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Bl_refragmentering_QModelIndex) 
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )
    
    test.vp("Verifying Lithotripsy Bladder Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 20, 18, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Bl_dt_v_v_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Fordamp_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 30, 30, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Fordamp_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_H_mostase_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Vaporize",
            "Hemostasis"
        ],
    )

    test.vp("Verifying Soft Tissue Vaporize Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 35, 24, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Bl_dt_v_v_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 18, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Tumor_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Tumor"
        ],
    )
    
    test.vp("Verifying Soft Tissue Tumor Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 26, 11, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Bl_dt_v_v_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incision_H_mostase_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 28, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Incision_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )
    
    test.vp("Verifying Soft Tissue Incision Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 8, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsi_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Nyre_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_FREM_WizardApplyButton))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 219, 59, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Afslut assistenttilstand?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Afslut assistenttilstand?": 
        test.passes("Afslut assistenttilstand? popup verified")
    else: test.fail("Afslut assistenttilstand? popup verification failed")
    validate_localization(
        objects=[
           waitForObjectExists(names.apollo_TextLabel_QLabel),
           waitForObjectExists(names.apollo_JA_QPushButton),
           waitForObjectExists(names.apollo_NEJ_QPushButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Exit Assistant mode?",
            "YES",
            "NO"
        ],
    )
    
    clickButton(waitForObject(names.apollo_JA_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Bekræft afslut?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Bekræft afslut?": 
        test.passes("Bekræft afslut? popup is verified")
    else: test.fail("Bekræft afslut? popup verification failed")
    clickButton(waitForObject(names.apollo_JA_QPushButton))
    
