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
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))

    validate_localization(

        objects=[
            
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.nAZIV_UNAPRIJED_ODRE_ENE_POSTAVKE_HeaderViewItem),
            waitForObject(names.eNERGIJA_HeaderViewItem),
            waitForObject(names.fREKVENCIJA_HeaderViewItem),
            waitForObject(names.sNAGA_HeaderViewItem),
            waitForObject(names.o_IRINA_IMPULSA_HeaderViewItem),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Bubrežni pijesak (visoko)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Bubrežni pijesak (nisko)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Bubrežni kamenac"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Bubrežni fragment (visoko)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Bubrežni fragment (nisko)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Mokraćovod (fragment)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Pijesak u mokraćovodu"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Fragment u bubregu"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "COAG"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Enukleacija prostate (visoko)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Enukleacija prostate (nisko)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Vaporizacija tkiva (pulsiranje)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Vaporizacija tkiva (CW)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ablacija/ekscizija tumora ")
            
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
    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text), "UNAPRIJED ODREĐENE POSTAVKE")
    if str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text) == "UNAPRIJED ODREĐENE POSTAVKE": 
        test.passes("Presets Screen verified")
    else: test.fail("Presets Screen verification failed")
