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
    
    clickButton(waitForObject(names.apollo_btTreatmentLogs_QPushButton))
    
    test.vp("treatmentLogs")

    validate_localization(
        objects=[
            waitForObject(names.apollo_lbProfileTitle_QLabel),
            waitForObject(names.apollo_lbProfileName_QLabel),
            waitForObject(names.apollo_lbFiberDiameterTitle_QLabel),
            waitForObject(names.apollo_lbUsesLeftTitle_QLabel),
            waitForObject(names.apollo_lbExpirationTitle_QLabel),
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.frmHeader_lbDate_QLabel),
            waitForObject(names.frmHeader_lbTime_QLabel),
            waitForObject(names.frmHeader_lbLasingTime_QLabel),
            waitForObject(names.frmHeader_lbTotal_QLabel),
            waitForObject(names.frmHeader_lbFiber_QLabel),
            waitForObjectExists(names.treatmentLogs_pbDownload_QPushButton),
        ],
        screen_name="Treatment Logs Screen",
        expected_strings=[
            "PROFILE",
            "DEFAULT",
            "FIBER (μm)",
            "USES LEFT",
            "EXPIRATION",
            "TREATMENT LOGS",
            "DATE",
            "TIME",
            "LASING TIME",
            "TOTAL Kj",
            "FIBER",
            "DOWNLOAD"
        ],
    
    )