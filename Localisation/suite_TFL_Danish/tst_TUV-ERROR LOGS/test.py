# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Dansk (Denmark)"), 91, 42, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbErrorLogs_QRadioButton))
   
    validate_localization(

        objects=[
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.bESKRIVELSE_AF_FEJL_HeaderViewItem),
            waitForObject(names.fEJLKODE_HeaderViewItem),
            waitForObject(names.dATO_KLOKKESL_T_HeaderViewItem),
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
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "FEJLLOGFILER")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "FEJLLOGFILER": 
        test.passes("ERROR LOGS Screen verified")
    else: test.fail("ERROR LOGS Screen verification failed") 
