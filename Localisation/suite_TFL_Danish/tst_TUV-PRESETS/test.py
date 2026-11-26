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
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 591, 21, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(

        objects=[
            
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.fORUDSTILLINGSNAVN_HeaderViewItem),
            waitForObject(names.eNERGI_HeaderViewItem),
            waitForObject(names.fREKVENS_HeaderViewItem),
            waitForObject(names.eFFEKT_HeaderViewItem),
            waitForObject(names.iMPULSBREDDE_HeaderViewItem),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nyregrus (højt)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nyregrus (lavt)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Små nyresten"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nyrestensfragment (højt)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nyrestensfragment (lavt)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Urinleder (fragment)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Urenledergrus"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Blærefragment"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "COAG"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Prostataenukleat (højt)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Prostataenukleat (lavt)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Vævsfordampning (pulseret)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Vævsfordampning (CW)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ablation/excision af tumor ")
            
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
    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text), "FORUDINDSTILLINGER")
    if str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text) == "FORUDINDSTILLINGER": 
        test.passes("PRESETS Screen verified")
    else: test.fail("PRESETS Screen verification failed")
