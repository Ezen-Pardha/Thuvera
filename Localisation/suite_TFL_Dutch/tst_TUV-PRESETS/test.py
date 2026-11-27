# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 471, 39, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Nederlands (The Netherlands)"), 177, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))

    test.compare(str(waitForObjectExists(names.apollo_centralWidget_QWidget_2).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget_2).visible, True)
    test.log("Presets Screen")

    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 704, 153, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 704, 153, -120, 0, 2)    
    test.compare(str(waitForObjectExists(names.apollo_centralWidget_QWidget_2).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget_2).visible, True)
    test.log("Scrolling through the Presets Screen")
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 1026, 175, -120, 0, 2)
    scrollTo(waitForObject(names.tvPresets_QScrollBar), 0)

    validate_localization(
        objects=[

            waitForObjectExists(names.apollo_lbScreenTitle_QLabel),
            waitForObjectExists(names.nAAM_VOORINSTELLING_HeaderViewItem),
            waitForObjectExists(names.eNERGIE_HeaderViewItem),
            waitForObjectExists(names.fREQUENTIE_HeaderViewItem),
            waitForObjectExists(names.vERMOGEN_HeaderViewItem),
            waitForObjectExists(names.pULSBREEDTE_HeaderViewItem),
            waitForObjectExists(names.tvPresets_Niergruis_hoog_QModelIndex),
            waitForObjectExists(names.tvPresets_Niergruis_laag_QModelIndex),
            waitForObjectExists(names.tvPresets_Niersteenfragmenten_met_popcornstructuur_QModelIndex),
            waitForObjectExists(names.tvPresets_Nierfragment_Hoog_QModelIndex),
            waitForObjectExists(names.tvPresets_Nierfragment_Laag_QModelIndex),
            waitForObjectExists(names.tvPresets_Ureter_Fragment_QModelIndex),
            waitForObjectExists(names.tvPresets_Uretergruis_QModelIndex),
            waitForObjectExists(names.tvPresets_Blaasfragment_QModelIndex),
            waitForObjectExists(names.tvPresets_COAG_QModelIndex),
            waitForObjectExists(names.tvPresets_Prostaatenucleatie_hoog_QModelIndex),
            waitForObjectExists(names.tvPresets_Prostaatenucleatie_laag_QModelIndex),
            waitForObjectExists(names.tvPresets_Weefsel_verdampen_gepulseerd_QModelIndex),
            waitForObjectExists(names.tvPresets_Weefsel_verdampen_CW_QModelIndex),
            waitForObjectExists(names.tvPresets_Tumorablatie_excisie_QModelIndex),

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
