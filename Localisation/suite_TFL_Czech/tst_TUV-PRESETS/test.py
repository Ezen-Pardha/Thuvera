# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 480, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "čeština (Czech Republic)"), 181, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))

    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text), "PŘEDVOLBY")
    test.log("Presets Screen Verification")
    validate_localization(
        objects=[

        waitForObject(names.apollo_lbScreenTitle_QLabel),
        waitForObject(names.n_ZEV_P_EDVOLBY_HeaderViewItem),
        waitForObject(names.eNERGIE_HeaderViewItem),
        waitForObject(names.fREKVENCE_HeaderViewItem),
        waitForObject(names.v_KON_HeaderViewItem),
        waitForObject(names.o_KA_PULSU_HeaderViewItem),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ledvinový prach (vysoký)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ledvinový prach (nízký)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ledvinové částečky"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ledvinový fragment (vysoký)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ledvinový fragment (nízký)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Močovod (fragment)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Prach v močovodu"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Fragment močového měchýře"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "COAG"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Enukleace prostaty (vysoká)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Enukleace prostaty (nízká)"),
        waitForObject(names.apollo_tvPresets_PresetsTable),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Odpařování tkáně (pulzní)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Odpařování tkáně (CW)"),
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ablace/excize nádoru "),

        ],
        screen_name="Presets Screen",
        expected_strings=[
            "PRESETS",
            "PRESET NAME",
            "ENERGY",
            "FREQUENCY",
            "POWER",
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
            "Tumor Ablation/Excision",
        ],
    )
