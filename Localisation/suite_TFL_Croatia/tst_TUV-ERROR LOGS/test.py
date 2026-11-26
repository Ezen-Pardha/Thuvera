# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 320, 41, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 114, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbErrorLogs_QRadioButton))
    mouseClick(waitForObject(names.frmHeader_lbHeader_QLabel), 184, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.dATUM_I_VRIJEME_HeaderViewItem), 95, 0, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.kOD_POGRE_KE_HeaderViewItem), 20, 1, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.oPIS_POGRE_KE_HeaderViewItem), 326, 13, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.errorLogsPage_tvErrorLog_QTreeView, "Device Configuration Error Please restart the system\\. Contact manufacturer if the error persists\\._1"), 298, 21, Qt.NoModifier, Qt.LeftButton)
   
    validate_localization(

        objects=[
            
            waitForObject(names.frmHeader_lbHeader_QLabel),
            waitForObject(names.dATUM_I_VRIJEME_HeaderViewItem),
            waitForObject(names.kOD_POGRE_KE_HeaderViewItem),
            waitForObject(names.oPIS_POGRE_KE_HeaderViewItem),
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
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "ZAPISNICI O POGREŠKAMA")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "ZAPISNICI O POGREŠKAMA": 
        test.passes("ERROR LOGS screen verified")
    else: test.fail("ERROR LOGS screen verification failed")
