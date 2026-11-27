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
   
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbErrorLogs_QRadioButton))

    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "FOUTLOGBOEKEN")
    test.compare(waitForObjectExists(names.apollo_lbHeader_QLabel).visible, True)
    test.log("Error Logs Screen Verification")
  
    validate_localization(

        objects=[

        waitForObjectExists(names.apollo_lbHeader_QLabel),
        waitForObjectExists(names.dATUM_TIJD_HeaderViewItem),
        waitForObjectExists(names.fOUTCODE_HeaderViewItem),
        waitForObjectExists(names.fOUTBESCHRIJVING_HeaderViewItem),
        waitForObjectExists(names.tvErrorLog_Device_Configuration_Error_Please_restart_the_system_Contact_manufacturer_if_the_error_persists_QModelIndex),
        waitForObjectExists(names.treatmentLogs_pbDownload_QPushButton),
            
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
