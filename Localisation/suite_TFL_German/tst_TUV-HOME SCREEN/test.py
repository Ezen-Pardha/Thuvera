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

    test.compare(str(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).text), "STAND-BY")
    test.compare(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).visible, True)
    test.log("Home/Treatment Screen Standby Mode Verification")
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 65, 31, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.stateSwitch_lbReady_QLabel).text), "BEREIT")
    test.compare(waitForObjectExists(names.stateSwitch_lbReady_QLabel).visible, True)
    test.log("Home/Treatment Screen Ready Mode Verification")

    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 177, 25, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 23, 12, Qt.NoModifier, Qt.LeftButton)

    validate_aiming_beam_label()

    validate_localization(
 
        objects=[

            waitForObject(names.centralWidget_lbHeader_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbPower_QLabel),
            waitForObject(names.centralWidget_lbPulseWidth_QLabel),
            waitForObject(names.centralWidget_pbPulsedMode_QToolButton),
            waitForObject(names.centralWidget_pbCwMode_QToolButton),
            waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget),
            waitForObject(names.stateSwitch_lbStandby_QLabel),
            waitForObject(names.stateSwitch_lbReady_QLabel),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Dust_hoch_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Dust_niedrig_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Popcorn_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Fragment_hoch_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Nieren_Fragment_niedrig_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Ureter_Dust_QModelIndex_2),
            waitForObjectExists(names.aivComboBoxPopup_Harnblasen_Fragment_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_COAG_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostata_Enukleat_hoch_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Prostata_Enukleat_niedrig_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Gewebe_Vaporisation_gepulst_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Gewebe_Vaporisation_CW_QModelIndex),
            waitForObjectExists(names.aivComboBoxPopup_Tumorablation_Exzision_QModelIndex)
                     
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
    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel), 16, 22, Qt.NoModifier, Qt.LeftButton)
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
    
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 19, 24, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Nieren-Dust (hoch)"), 196, 26, Qt.NoModifier, Qt.LeftButton)
