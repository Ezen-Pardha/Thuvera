# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()    
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 635, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_TREATMENT_TYPE_WizardTitle), 184, 18, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.frWizardPlace_TREATMENT_TYPE_WizardTitle),
            waitForObject(names.frWizardPlace_Lithotripsy_WizardButton),
            waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton),
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
    
    clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_LOCATION_WizardTitle),
            waitForObject(names.frWizardPlace_STONE_SIZE_MM_WizardTitle),
            waitForObject(names.frWizardPlace_STONE_DENSITY_HU_WizardTitle),
            waitForObject(names.frWizardPlace_Kidney_WizardButton),
            waitForObject(names.frWizardPlace_Ureter_WizardButton),
            waitForObject(names.frWizardPlace_Bladder_WizardButton)
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
    
    mouseClick(waitForObject(names.frWizardPlace_LOCATION_WizardTitle), 116, 14, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_STONE_SIZE_MM_WizardTitle), 162, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_STONE_DENSITY_HU_WizardTitle), 100, 9, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Kidney_WizardButton))
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
    
    clickButton(waitForObject(names.frWizardPlace_Small_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Medium_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Large_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Unknown_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Hard_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Ureter_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bladder_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Small_6_WizardButton),
            waitForObject(names.frWizardPlace_Medium_6_10_WizardButton),
            waitForObject(names.frWizardPlace_Large_10_WizardButton),
            waitForObject(names.frWizardPlace_Unknown_WizardButton),
            waitForObject(names.frWizardPlace_Soft_500_WizardButton),
            waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton),
            waitForObject(names.frWizardPlace_Hard_1000_WizardButton)
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

    test.compare(str(waitForObjectExists(names.frWizardPlace_LOCATION_WizardTitle).text), "LOCATION")
    if str(waitForObjectExists(names.frWizardPlace_LOCATION_WizardTitle).text) == "LOCATION": 
        test.passes("Assistant Lithotripsy Screen verified")
    else: test.fail("Assistant Lithotripsy Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    mouseClick(waitForObject(names.frWizardPlace_LEFT_PEDAL_RIGHT_PEDAL_WizardTitle), 113, 12, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frWizardPlace_LEFT_PEDAL_RIGHT_PEDAL_WizardTitle), 363, 18, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incision_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton))  
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_LEFT_PEDAL_RIGHT_PEDAL_WizardTitle),
            waitForObject(names.frWizardPlace_LEFT_PEDAL_RIGHT_PEDAL_WizardTitle),
            waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton),
            waitForObject(names.frWizardPlace_Tumor_Hemostasis_WizardButton),
            waitForObject(names.frWizardPlace_Incision_Hemostasis_WizardButton),
            waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton)
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
    
    test.compare(str(waitForObjectExists(names.frWizardPlace_Vaporize_Hemostasis_WizardButton).text), "Vaporize|Hemostasis")
    if str(waitForObjectExists(names.frWizardPlace_Vaporize_Hemostasis_WizardButton).text) == "Vaporize|Hemostasis": 
        test.passes("Assistant Soft Tissue Screen verified")
    else: test.fail("Assistant Soft Tissue Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enucleation_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enucleation_Low_Power_WizardButton))
    validate_localization(
        objects=[
            waitForObject(names.frWizardPlace_Enucleation_Hemostasis_WizardButton),
            waitForObject(names.frWizardPlace_Enucleation_Low_Power_WizardButton),
            waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Enucleation",
            "Low Power",
            "ADVANCE"
        ],
    )

    test.compare(str(waitForObjectExists(names.frWizardPlace_Enucleation_Low_Power_WizardButton).text), "Enucleation|Low Power")
    if str(waitForObjectExists(names.frWizardPlace_Enucleation_Low_Power_WizardButton).text) == "Enucleation|Low Power": 
        test.passes("Assistant BPH Screen verified")
    else: test.fail("Assistant BPH Screen verification failed")
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
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
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Enucleation"), 68, 35, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 26, 24, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Enucleation_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Low_Power_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kidney_Dust_High_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kidney_Dust_Low_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kidney_Popcorn_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kidney_Fragment_High_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kidney_Fragment_Low_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Dust_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Bladder_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostate_Enucleate_High_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostate_Enucleate_Low_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Tissue_Vaporize_Pulsed_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Tissue_Vaporize_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Tumor_Ablation_Excision_QModelIndex)
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
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Kidney_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 31, 23, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Kidney_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Kidney_Dust_QModelIndex)
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
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Ureter_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 28, 32, Qt.NoModifier, Qt.LeftButton)      
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Fragment_QModelIndex_2),
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Dust_QModelIndex)
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
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bladder_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 396, 19, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
           waitForObjectExists(names.aivComboBoxPopup_Bladder_Fragmentation_QModelIndex) 
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Bladder Fragmentation"
        ],
    )
    
    test.vp("Verifying Lithotripsy Bladder Adv")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 20, 18, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 30, 30, Qt.NoModifier, Qt.LeftButton)
    validate_localization(
        objects=[
            waitForObjectExists(names.aivComboBoxPopup_Vaporize_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Hemostasis_QModelIndex)
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
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
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
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incision_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
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
    test.vp("Verifying Soft Tissue Incision")
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 8, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Kidney_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    mouseClick(waitForObject(names.apollo_TextLabel_QLabel), 219, 59, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Exit Assistant mode?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Exit Assistant mode?": 
        test.passes("Exit Assistant mode? popup verified")
    else: test.fail("Exit Assistant mode? popup verification failed")
    validate_localization(
        objects=[
           waitForObjectExists(names.apollo_TextLabel_QLabel),
           waitForObjectExists(names.apollo_YES_QPushButton),
           waitForObjectExists(names.apollo_NO_QPushButton)
        ],
        screen_name="ASSISTANT MODE",
        expected_strings=[
            "Exit Assistant mode?",
            "YES",
            "NO"
        ],
    )
    
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    test.compare(str(waitForObjectExists(names.apollo_TextLabel_QLabel).text), "Confirm Exit?")
    if str(waitForObjectExists(names.apollo_TextLabel_QLabel).text) == "Confirm Exit?": 
        test.passes("Confirm Exit? popup is verified")
    else: test.fail("Confirm Exit? popup verification failed")
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    
