
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
   
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbErrorLogs_QRadioButton))
    
    test.imagePresent("errorDescription")


    validate_localization(

        objects=[

            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.o_HeaderViewItem),
            waitForObject(names.o_HeaderViewItem_2),
            waitForObject(names.o_HeaderViewItem_3),
            waitForObjectItem(names.errorLogsPage_tvErrorLog_QTreeView, "Device Configuration Error Please restart the system\\. Contact manufacturer if the error persists\\._1"),
            waitForObjectExists(names.errorLogsPage_pbDownload_QPushButton),
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
    test.fail("'Please restart the system. Contact manufacturer if the error persists' is not available in the Excel file and therefore has not been translated.")
            