# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 480, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "suomi (Finland)"), 136, 27, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))

    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget_2).visible, True)
    test.log("Presets Screen")
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 874, 199, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 880, 219, -120, 0, 2)
    test.compare(waitForObjectExists(names.apollo_centralWidget_QWidget_2).visible, True)
    test.log("Scrolling through the Presets Screen")
    scrollTo(waitForObject(names.tvPresets_QScrollBar), 0)

    validate_localization(
        objects=[

            waitForObject(names.apollo_lbScreenTitle_QLabel),
            waitForObject(names.eSIASETUKSEN_NIMI_HeaderViewItem),
            waitForObject(names.eNERGIA_HeaderViewItem),
            waitForObject(names.tAAJUUS_HeaderViewItem),
            waitForObject(names.tEHO_HeaderViewItem),
            waitForObject(names.pULSSINLEVEYS_HeaderViewItem),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Munuaiskivihiukkaset (paljon)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Munuaiskivihiukkaset (vähän)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Munuaispopcorn"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Munuaiskivipalat (paljon)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Munuaiskivipalat (vähän)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Virtsaputki (pala)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Hiukkaset virtsaputkessa"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Pala virtsarakossa"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "COAG"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Eturauhasen enukleaatio (suuri)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Eturauhasen enukleaatio (pieni)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kudoken höyrystys (pulssinen)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Kudoksen höyrystys (CW)"),
            waitForObjectItem(names.apollo_tvPresets_PresetsTable, "Tuumorin ablaatio/poistaminen "),

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
