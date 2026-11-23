# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()    
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 91, 42, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 635, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_VRSTA_LIJE_ENJA_WizardTitle), 90, 16, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_VRSTA_LIJE_ENJA_WizardTitle),
            waitForObject(names.frWizardPlace_Litotripsija_WizardButton),
            waitForObject(names.frWizardPlace_Meko_tkivo_WizardButton),
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
    
    clickButton(waitForObject(names.frWizardPlace_Litotripsija_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Meko_tkivo_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsija_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_LOKACIJA_WizardTitle),
            waitForObject(names.frWizardPlace_VELI_INA_KAMENA_mm_WizardTitle),
            waitForObject(names.frWizardPlace_GUSTO_A_KAMENA_HU_WizardTitle),
            waitForObject(names.frWizardPlace_Bubreg_WizardButton),
            waitForObject(names.frWizardPlace_Mokra_ovod_WizardButton),
            waitForObject(names.frWizardPlace_Mjehur_WizardButton)
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
    
    mouseClick(waitForObject(names.frWizardPlace_LOKACIJA_WizardTitle), 108, 15, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_VELI_INA_KAMENA_mm_WizardTitle), 100, 21, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_GUSTO_A_KAMENA_HU_WizardTitle), 144, 12, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Bubreg_WizardButton))
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
    
    clickButton(waitForObject(names.frWizardPlace_Mali_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Srednji_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Veliki_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Nepoznato_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mekan_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Srednji_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tvrd_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mokra_ovod_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mjehur_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Mali_6_WizardButton),
            waitForObject(names.frWizardPlace_Srednji_6_10_WizardButton),
            waitForObject(names.frWizardPlace_Veliki_10_WizardButton),
            waitForObject(names.frWizardPlace_Nepoznato_WizardButton),
            waitForObject(names.frWizardPlace_Mekan_500_WizardButton),
            waitForObject(names.frWizardPlace_Srednji_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_Tvrd_1000_WizardButton)
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
    
    test.compare(str(waitForObjectExists(names.frWizardPlace_LOKACIJA_WizardTitle).text), "LOKACIJA")
    if str(waitForObjectExists(names.frWizardPlace_LOKACIJA_WizardTitle).text) == "LOKACIJA": 
        test.passes("Assistant Lithotripsy Screen verified")
    else: test.fail("Assistant Lithotripsy Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_Meko_tkivo_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_LIJEVA_PAPU_ICA_DESNA_PAPU_ICA_WizardTitle), 99, 18, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_LIJEVA_PAPU_ICA_DESNA_PAPU_ICA_WizardTitle), 351, 12, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Vaporizacija_Hemostaza_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostaza_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Rez_Hemostaza_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Vaporizacija_Hemostaza_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_LIJEVA_PAPU_ICA_DESNA_PAPU_ICA_WizardTitle),
            waitForObject(names.frWizardPlace_LIJEVA_PAPU_ICA_DESNA_PAPU_ICA_WizardTitle),
            waitForObject(names.frWizardPlace_Vaporizacija_Hemostaza_WizardButton),
            waitForObject(names.frWizardPlace_Tumor_Hemostaza_WizardButton),
            waitForObject(names.frWizardPlace_Rez_Hemostaza_WizardButton),
            waitForObject(names.frWizardPlace_Vaporizacija_Hemostaza_WizardButton)
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
    
    test.compare(str(waitForObjectExists(names.frWizardPlace_Vaporizacija_Hemostaza_WizardButton).text), "Vaporizacija|Hemostaza")
    if str(waitForObjectExists(names.frWizardPlace_Vaporizacija_Hemostaza_WizardButton).text) == "Vaporizacija|Hemostaza": 
        test.passes("Assistant Soft Tissue Screen verified")
    else: test.fail("Assistant Soft Tissue Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleacija_Hemostaza_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enukleacija_Niska_snaga_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Enukleacija_Hemostaza_WizardButton),
            waitForObject(names.frWizardPlace_Enukleacija_Niska_snaga_WizardButton),
            waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )
    
    test.compare(str(waitForObjectExists(names.frWizardPlace_Enukleacija_Niska_snaga_WizardButton).text), "Enukleacija|Niska snaga")
    if str(waitForObjectExists(names.frWizardPlace_Enukleacija_Niska_snaga_WizardButton).text) == "Enukleacija|Niska snaga": 
        test.passes("Assistant BPH Screen verified")
    else: test.fail("Assistant BPH Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
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

    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 47, 25, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Enukleacija"), 71, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 26, 24, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Enukleacija_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Niska_snaga_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bubre_ni_pijesak_visoko_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bubre_ni_pijesak_nisko_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bubre_ni_kamenac_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bubre_ni_fragment_visoko_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bubre_ni_fragment_nisko_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Mokra_ovod_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Pijesak_u_mokra_ovodu_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Fragment_u_bubregu_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Enukleacija_prostate_visoko_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Enukleacija_prostate_nisko_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Vaporizacija_tkiva_pulsiranje_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Vaporizacija_tkiva_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ablacija_ekscizija_tumora_QModelIndex)
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
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsija_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bubreg_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 31, 23, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Bubre_ni_fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bubre_ni_pijesak_QModelIndex)
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
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsija_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mokra_ovod_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 28, 32, Qt.NoModifier, Qt.LeftButton)      
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Mokra_ovod_fragment_QModelIndex_2),
            waitForObjectExists(names.aivComboBoxPopup_Pijesak_u_mokra_ovodu_QModelIndex)
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
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsija_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Mjehur_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 396, 19, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Fragmentacija_mjehura_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )
    
    test.vp("Verifying Lithotripsy Bladder Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 20, 18, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Meko_tkivo_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Vaporizacija_Hemostaza_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 30, 30, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Vaporizacija_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Hemostaza_QModelIndex)
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
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Meko_tkivo_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostaza_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
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
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Meko_tkivo_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Rez_Hemostaza_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 28, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Rez_QModelIndex)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Incision"
        ],
    )

    test.vp("Verifying Soft Tissue Incision Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 8, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_DA_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Litotripsija_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bubreg_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_NASTAVI_WizardApplyButton))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 219, 59, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Želite li izaći iz načina rada pomoćnika?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Želite li izaći iz načina rada pomoćnika?": 
        test.passes("Želite li izaći iz načina rada pomoćnika? popup verified")
    else: test.fail("Želite li izaći iz načina rada pomoćnika? popup verification failed")
    validate_localization(
        objects=[
           waitForObjectExists(names.apollo_TextLabel_QLabel),
           waitForObjectExists(names.apollo_DA_QPushButton),
           waitForObjectExists(names.apollo_NE_QPushButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Exit Assistant mode?",
            "YES",
            "NO"
        ],
    )
    clickButton(waitForObject(names.apollo_DA_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Želite li potvrditi izlaz?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Želite li potvrditi izlaz?": 
        test.passes("Želite li potvrditi izlaz? popup is verified")
    else: test.fail("Želite li potvrditi izlaz? popup verification failed")
    clickButton(waitForObject(names.apollo_DA_QPushButton))
    
