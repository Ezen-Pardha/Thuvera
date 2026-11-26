# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Eesti (Estonia)"), 120, 36, Qt.NoModifier, Qt.LeftButton)
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
    test.compare(str(waitForObjectExists(names.stateSwitch_lbReady_QLabel).text), "VALMIS")
    if str(waitForObjectExists(names.stateSwitch_lbReady_QLabel).text) == "VALMIS":
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
    test.compare(str(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).text), "OOTEREŽIIM")
    if str(waitForObjectExists(names.stateSwitch_lbStandby_QLabel).text) == "OOTEREŽIIM": 
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
    
    test.compare(str(waitForObjectExists(names.comboBox_lbValue_AutoReducibleFontSizeLabel).text), "KOHANDATUD")
    if str(waitForObjectExists(names.comboBox_lbValue_AutoReducibleFontSizeLabel).text) == "KOHANDATUD": 
        test.passes("Home Screen CUSTOM verified")
    else: test.fail("Home Screen CUSTOM verification failed")
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 27, 31, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Neerukivid (kõrge)"), 218, 22, Qt.NoModifier, Qt.LeftButton)
