# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 146, 54, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Eesti (Estonia)"), 98, 23, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 656, 19, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_RAVI_T_P_WizardTitle), 184, 18, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_RAVI_T_P_WizardTitle),
            waitForObject(names.frWizardPlace_Litotripsia_WizardButton),
            waitForObject(names.frWizardPlace_Pehme_kude_WizardButton),
            waitForObject(names.frWizardPlace_Eesn_rme_healoomuline_h_perplaasia_WizardButton)
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
    
    clickButton(waitForObject(names.frWizardPlace_Litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Pehme_kude_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Eesn_rme_healoomuline_h_perplaasia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsia_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_ASUKOHT_WizardTitle),
            waitForObject(names.frWizardPlace_KIVI_SUURUS_MM_WizardTitle),
            waitForObject(names.frWizardPlace_KIVI_TIHENDUS_HU_WizardTitle),
            waitForObject(names.frWizardPlace_Neer_WizardButton),
            waitForObject(names.frWizardPlace_Kusejuha_WizardButton),
            waitForObject(names.frWizardPlace_P_is_WizardButton)
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
    
    mouseClick(waitForObject(names.frWizardPlace_ASUKOHT_WizardTitle), 116, 14, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_KIVI_SUURUS_MM_WizardTitle), 162, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_KIVI_TIHENDUS_HU_WizardTitle), 100, 9, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Neer_WizardButton))
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
    
    clickButton(waitForObject(names.frWizardPlace_V_ike_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Keskmise_suurusega_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Suur_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Teadmata_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Pehme_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Keskmise_suurusega_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_K_va_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Kusejuha_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_P_is_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_V_ike_6_WizardButton),
            waitForObject(names.frWizardPlace_Keskmise_suurusega_6_10_WizardButton),
            waitForObject(names.frWizardPlace_Suur_10_WizardButton),
            waitForObject(names.frWizardPlace_Teadmata_WizardButton),
            waitForObject(names.frWizardPlace_Pehme_500_WizardButton),
            waitForObject(names.frWizardPlace_Keskmise_suurusega_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_K_va_1000_WizardButton)
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

    test.compare(str(waitForObjectExists(names.frWizardPlace_ASUKOHT_WizardTitle).text), "ASUKOHT")
    if str(waitForObjectExists(names.frWizardPlace_ASUKOHT_WizardTitle).text) == "ASUKOHT": 
        test.passes("Assistant Lithotripsy Screen verified")
    else: test.fail("Assistant Lithotripsy Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_Pehme_kude_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_VASAK_PEDAAL_PAREM_PEDAAL_WizardTitle), 113, 12, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_VASAK_PEDAAL_PAREM_PEDAAL_WizardTitle), 363, 18, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Aurustamine_Hemostaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Kasvaja_Hemostaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Sissel_ige_Hemostaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Aurustamine_Hemostaas_WizardButton))  
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_VASAK_PEDAAL_PAREM_PEDAAL_WizardTitle),
            waitForObject(names.frWizardPlace_VASAK_PEDAAL_PAREM_PEDAAL_WizardTitle),
            waitForObject(names.frWizardPlace_Aurustamine_Hemostaas_WizardButton),
            waitForObject(names.frWizardPlace_Kasvaja_Hemostaas_WizardButton),
            waitForObject(names.frWizardPlace_Sissel_ige_Hemostaas_WizardButton),
            waitForObject(names.frWizardPlace_Aurustamine_Hemostaas_WizardButton)
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
    
    test.compare(str(waitForObjectExists(names.frWizardPlace_Aurustamine_Hemostaas_WizardButton).text), "Aurustamine|Hemostaas")
    if str(waitForObjectExists(names.frWizardPlace_Aurustamine_Hemostaas_WizardButton).text) == "Aurustamine|Hemostaas": 
        test.passes("Assistant Soft Tissue Screen verified")
    else: test.fail("Assistant Soft Tissue Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_Eesn_rme_healoomuline_h_perplaasia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleatsioon_Hemostaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleatsioon_V_ike_v_imsus_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Enukleatsioon_Hemostaas_WizardButton),
            waitForObject(names.frWizardPlace_Enukleatsioon_V_ike_v_imsus_WizardButton),
            waitForObject(names.frWizardPlace_EDASI_WizardApplyButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )

    test.compare(str(waitForObjectExists(names.frWizardPlace_Enukleatsioon_V_ike_v_imsus_WizardButton).text), "Enukleatsioon|V_ike v_imsus")
    if str(waitForObjectExists(names.frWizardPlace_Enukleatsioon_V_ike_v_imsus_WizardButton).text) == "Enukleatsioon|V_ike v_imsus": 
        test.passes("Assistant BPH Screen verified")
    else: test.fail("Assistant BPH Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_lbHeader_QLabel), 52, 8, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 24, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPower_QLabel), 39, 5, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPulseWidth_QLabel), 137, 37, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbPulsedMode_QToolButton))
    clickButton(waitForObject(names.centralWidget_pbCwMode_QToolButton))
    mouseClick(waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget), 457, 469, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 179, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 119, 28, Qt.NoModifier, Qt.LeftButton)
    validate_aiming_beam_label()
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
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 47, 25, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Enukleatsioon"), 153, 29, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 26, 24, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Enukleatsioon_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_V_ike_v_imsus_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Neerukivid_k_rge_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Neerukivid_madal_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_L_henenud_neerukivid_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Neerukivi_fragment_k_rge_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Neerukivi_fragment_madal_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kusejuha_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kusejuhakivide_tolm_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_P_iekivi_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_KOAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Eesn_rme_enukleatsioon_k_rge_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Eesn_rme_enukleatsioon_madal_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Koe_aurustamine_pulseeritud_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Koe_aurustamine_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kasvaja_ablatsioon_ekstsisioon_QModelIndex)
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
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Neer_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 31, 23, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Neerukivi_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Neerukivid_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Kidney Fragment",
            "Kidney Dust"
        ],
    )

    test.vp("Verifying Lithotripsy Kidney Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 10, 29, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Kusejuha_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 28, 32, Qt.NoModifier, Qt.LeftButton)      
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Kusejuha_fragment_QModelIndex_2),
            waitForObjectExists(names.aivComboBoxPopup_Kusejuhakivide_tolm_QModelIndex)
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
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_P_is_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 396, 19, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Kusep_ie_killustumine_QModelIndex) 
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )
    
    test.vp("Verifying Lithotripsy Bladder Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 20, 18, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Pehme_kude_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Aurustamine_Hemostaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 30, 30, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Aurustamine_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Hemostaas_QModelIndex)
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
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Pehme_kude_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Kasvaja_Hemostaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 18, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Kasvaja_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Tumor"
        ],
    )
    
    test.vp("Verifying Soft Tissue Tumor Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 26, 11, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Pehme_kude_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Sissel_ige_Hemostaas_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 28, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Sissel_ige_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )

    test.vp("Verifying Soft Tissue Incision Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 8, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsia_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Neer_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_EDASI_WizardApplyButton))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 219, 59, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Kas sulgeda abiliserežiim?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Kas sulgeda abiliserežiim?": 
        test.passes("Exit Assistant mode? popup verified")
    else: test.fail("Exit Assistant mode? popup verification failed")
    validate_localization(
        objects=[
           waitForObjectExists(names.apollo_TextLabel_QLabel),
           waitForObjectExists(names.apollo_JAH_QPushButton),
           waitForObjectExists(names.apollo_EI_QPushButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Exit Assistant mode?",
            "YES",
            "NO"
        ],
    )
    
    clickButton(waitForObject(names.apollo_JAH_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Kas kinnitada sulgemine?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Kas kinnitada sulgemine?": 
        test.passes("Confirm Exit? popup is verified")
    else: test.fail("Confirm Exit? popup verification failed")
    clickButton(waitForObject(names.apollo_JAH_QPushButton))
    
