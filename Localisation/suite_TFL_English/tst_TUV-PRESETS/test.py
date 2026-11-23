# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_presets()
    
    validate_localization(

        objects=[
            
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.pRESET_NAME_HeaderViewItem),
            waitForObject(names.eNERGY_HeaderViewItem),
            waitForObject(names.fREQUENCY_HeaderViewItem),
            waitForObject(names.pOWER_HeaderViewItem),
            waitForObject(names.pULSE_WIDTH_HeaderViewItem),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kidney Dust (High)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kidney Dust (Low)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kidney Popcorn"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kidney Fragment (High)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kidney Fragment (Low)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ureter (Fragment)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ureter Dust"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Bladder Fragment"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "COAG"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Prostate Enucleate (High)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Prostate Enucleate (Low)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Tissue Vaporize (Pulsed)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Tissue Vaporize (CW)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Tumor Ablation/Excision"),
            
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
    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text), "PRESETS")
    if str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text) == "PRESETS": 
        test.passes("PRESETS Screen verified")
    else: test.fail("PRESETS Screen verification failed")
