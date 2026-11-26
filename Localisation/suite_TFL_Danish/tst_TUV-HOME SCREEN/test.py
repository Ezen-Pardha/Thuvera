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
    clickButton(waitForObject(names.apollo_btHome_QPushButton))
    mouseClick(waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget), 18, 9, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbHeader_QLabel), 57, 3, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 52, 2, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPower_QLabel), 38, 9, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbPulseWidth_QLabel), 105, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbPulsedMode_QToolButton))
    clickButton(waitForObject(names.centralWidget_pbCwMode_QToolButton))
    mouseClick(waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget), 457, 469, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 155, 48, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 104, 35, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.stateSwitch_lbReady_QLabel).text), "KLAR")
    if str(waitForObjectExists(names.stateSwitch_lbReady_QLabel).text) == "KLAR":
        test.passes("Home Screen READY verified")
    else: test.fail("Home Screen READY verification failed")
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 176, 34, Qt.NoModifier, Qt.LeftButton) 
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 225, 26, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(

        objects=[
            waitForObject(names.centralWidget_lbHeader_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbPower_QLabel),
            waitForObject(names.centralWidget_lbPulseWidth_QLabel),
            waitForObject(names.centralWidget_pbPulsedMode_QToolButton),
            waitForObject(names.centralWidget_pbCwMode_QToolButton),
            waitForObject(names.stateSwitch_lbStandby_QLabel),
            waitForObject(names.stateSwitch_lbReady_QLabel),
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

        screen_name="HOME SCREEN/TREATMENT",

        expected_strings=[
            
            "ENERGY (J)",
            "FREQUENCY (Hz)",
            "POWER (W)",
            "PULSE WIDTH",
            "PULSED",
            "CW",
            "STANDBY",
            "READY",
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
    
    validate_aiming_beam_label()
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 16, 22, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).text), "STANDBY")
    if str(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).text) == "STANDBY": 
        test.passes("Home Screen STANDBY verified")
    else: test.fail("Home Screen STANDBY verification failed")
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 69, 20, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frmComboBoxHeader_lbValue_AutoReducibleFontSizeLabel), 69, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbSaveSettings_QPushButton))
    clickButton(waitForObject(names.apollo_btCancel_QPushButton))
  
    validate_localization(
         objects=[
            waitForObjectExists(names.comboBox_lbValue_AutoReducibleFontSizeLabel),
            waitForObjectExists(names.centralWidget_pbSaveSettings_QPushButton)
          
        ],

        screen_name="HOME SCREEN/TREATMENT",

        expected_strings=[
            "CUSTOM",
            "Save Settings"
        ]
    )
   
    test.compare(str(waitForObjectExists(names.comboBox_lbValue_AutoReducibleFontSizeLabel).text), "BRUGERTILPASSET")
    if str(waitForObjectExists(names.comboBox_lbValue_AutoReducibleFontSizeLabel).text) == "BRUGERTILPASSET": 
        test.passes("Home Screen CUSTOM verified")
    else: test.fail("Home Screen CUSTOM verification failed")
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 27, 31, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Nyregrus (højt)"), 158, 20, Qt.NoModifier, Qt.LeftButton)
    
