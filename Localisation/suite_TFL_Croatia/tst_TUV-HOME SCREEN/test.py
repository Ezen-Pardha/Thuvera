# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 91, 42, Qt.NoModifier, Qt.LeftButton)
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
    test.compare(str(waitForObjectExists(names.stateSwitch_lbReady_QLabel).text), "SPREMNO")
    if str(waitForObjectExists(names.stateSwitch_lbReady_QLabel).text) == "SPREMNO":
        test.passes("Home Screen READY verified")
    else: test.fail("Home Screen READY verification failed")
    mouseClick(waitForObject(names.stateSwitch_lbStandby_QLabel), 176, 34, Qt.NoModifier, Qt.LeftButton) 
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel), 225, 26, Qt.NoModifier, Qt.LeftButton)
    validate_aiming_beam_label()
    
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
    test.compare(str(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).text), "STANJE\nMIROVANJA")
    if str(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).text) == "STANJE\nMIROVANJA": 
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
    
    test.compare(str(waitForObjectExists(names.comboBox_lbValue_AutoReducibleFontSizeLabel).text), "PRILAGOĐENO")
    if str(waitForObjectExists(names.comboBox_lbValue_AutoReducibleFontSizeLabel).text) == "PRILAGOĐENO": 
        test.passes("Home Screen CUSTOM verified")
    else: test.fail("Home Screen CUSTOM verification failed")
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 27, 31, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Bubrežni pijesak (visoko)"), 208, 29, Qt.NoModifier, Qt.LeftButton)

    
