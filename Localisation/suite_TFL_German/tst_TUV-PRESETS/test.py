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
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    
    test.compare(str(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).text), "VOREINSTELLUNGEN")
    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget_2).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_centralWidget_QWidget_2).windowIconText), "")
    test.log("Presets Screen")
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 815, 176, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 819, 183, -120, 0, 2)
    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget_2).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_centralWidget_QWidget_2).windowIconText), "")
    test.log("Scrolling through the Presets Screen")
    scrollTo(waitForObject(names.tvPresets_QScrollBar), 0)

    validate_localization(
        objects=[

            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.nAME_DER_VOREINSTELLUNG_HeaderViewItem),
            waitForObject(names.eNERGIE_HeaderViewItem),
            waitForObject(names.fREQUENZ_HeaderViewItem),
            waitForObject(names.lEISTUNG_HeaderViewItem),
            waitForObject(names.iMPULSBREITE_HeaderViewItem),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nieren-Dust (hoch)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nieren-Dust (niedrig)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nieren-Popcorn"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nieren-Fragment (hoch)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Nieren-Fragment (niedrig)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ureter (Fragment)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Ureter-Dust"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Harnblasen-Fragment"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "COAG"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Prostata-Enukleat (hoch)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Prostata-Enukleat (niedrig)"),
            waitForObject(names.apollo_tvPresets_PresetsTable),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Gewebe-Vaporisation (gepulst)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Gewebe-Vaporisation (CW)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Tumorablation/Exzision ")

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
