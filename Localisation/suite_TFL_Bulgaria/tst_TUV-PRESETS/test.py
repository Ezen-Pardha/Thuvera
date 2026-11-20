# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 184, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Български (Bulgaria)"), 130, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))

    test.vp("presetsScreen")

    validate_localization(
        objects=[

            waitForObjectExists(names.apollo_lbScreenTitle_QLabel),
            waitForObjectExists(names.o_HeaderViewItem_4),
            waitForObjectExists(names.o_HeaderViewItem_5),
            waitForObjectExists(names.o_HeaderViewItem_6),
            waitForObjectExists(names.o_HeaderViewItem_7),
            waitForObjectExists(names.o_HeaderViewItem_8),
            waitForObjectExists(names.tvPresets_QModelIndex),
            waitForObjectExists(names.tvPresets_QModelIndex_2),
            waitForObjectExists(names.tvPresets_Popcorn_QModelIndex),
            waitForObjectExists(names.tvPresets_QModelIndex_3),
            waitForObjectExists(names.tvPresets_QModelIndex_4),
            waitForObjectExists(names.tvPresets_QModelIndex_5),
            waitForObjectExists(names.tvPresets_QModelIndex_6),
            waitForObjectExists(names.tvPresets_QModelIndex_7),
            waitForObjectExists(names.tvPresets_QModelIndex_8),
            waitForObjectExists(names.tvPresets_QModelIndex_9),
            waitForObjectExists(names.tvPresets_QModelIndex_10),
            waitForObject(names.apollo_tvPresets_PresetsTable),
            waitForObjectExists(names.tvPresets_QModelIndex_11),
            waitForObjectExists(names.tvPresets_CW_QModelIndex),
            waitForObjectExists(names.tvPresets_QModelIndex_12),
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
           # "Ureter Fragment",
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
