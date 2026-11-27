# -*- coding: utf-8 -*-
import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 480, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "čeština (Czech Republic)"), 181, 43, Qt.NoModifier, Qt.LeftButton)
   
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbErrorLogs_QRadioButton))
    
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "PROTOKOLY CHYB")
    test.compare(waitForObjectExists(names.apollo_lbHeader_QLabel).visible, True)
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).windowIconText), "")
    test.log("Error Logs Screen Verification")
    
    validate_localization(

        objects=[

            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.dATUM_AS_HeaderViewItem),
            waitForObject(names.k_D_CHYBY_HeaderViewItem),
            waitForObject(names.pOPIS_CHYBY_HeaderViewItem),
            waitForObjectItem(names.errorLogsPage_tvErrorLog_QTreeView, "Device Configuration Error Please restart the system\\. Contact manufacturer if the error persists\\._1"),
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
