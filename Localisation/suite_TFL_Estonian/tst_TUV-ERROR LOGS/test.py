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
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbErrorLogs_QRadioButton))
   
    validate_localization(

        objects=[
            
            waitForObject(names.frmHeader_lbHeader_QLabel),
            waitForObject(names.t_RKE_KIRJELDUS_HeaderViewItem),
            waitForObject(names.t_RKEKOOD_HeaderViewItem),
            waitForObject(names.kUUP_EV_JA_KELLAAEG_HeaderViewItem),
            waitForObjectItem(names.errorLogsPage_tvErrorLog_QTreeView, "Device Configuration Error Please restart the system\\. Contact manufacturer if the error persists\\._1"),
            waitForObjectExists(names.errorLogsPage_pbDownload_QPushButton)
        ],

        screen_name="ERROR LOGS",

        expected_strings=[
            "ERROR LOGS",
            "ERROR CODE",
            "ERROR DESCRIPTION",
            "DATE TIME",
            "Device Configuration Error",
            "Please restart the system. Contact manufacturer if the error persists.",
            "DOWNLOAD"
        ],
    )

    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "TÕRKELOGID")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "TÕRKELOGID": 
        test.passes("ERROR LOGS Screen verified")
    else: test.fail("ERROR LOGS Screen verification failed") 
