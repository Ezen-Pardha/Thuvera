# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 451, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Eesti (Estonia)"), 120, 36, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 591, 21, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(

        objects=[
            
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.eTTEM_RATUD_NIMI_HeaderViewItem),
            waitForObject(names.eNERGIA_HeaderViewItem),
            waitForObject(names.sAGEDUS_HeaderViewItem),
            waitForObject(names.v_IMSUS_HeaderViewItem),
            waitForObject(names.iMPULSILAIUS_HeaderViewItem),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Neerukivid (kõrge)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Neerukivid (madal)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Lõhenenud neerukivid"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Neerukivi fragment (kõrge)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Neerukivi fragment (madal)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kusejuha (fragment)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kusejuhakivide tolm"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Põiekivi fragment"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "KOAG"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Eesnäärme enukleatsioon (kõrge)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Eesnäärme enukleatsioon (madal)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Koe aurustamine (pulseeritud)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Koe aurustamine (CW)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kasvaja ablatsioon/ekstsisioon ")
            
        ],

        screen_name="PRESETS",

        expected_strings=[  
            
            "PRESETS",
            "PRESET NAME",
            "ENERGY",
            "FREQUENCY",
            "POWER",
            "PULSE WIDTH",
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

    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text), "EELSÄTTED")
    if str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text) == "EELSÄTTED": 
        test.passes("PRESETS Screen verified")
    else: test.fail("PRESETS Screen verification failed")
