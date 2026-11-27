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
   
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbErrorLogs_QRadioButton))
    
    test.compare(waitForObjectExists(names.apollo_lbHeader_QLabel).visible, True)
    test.log("Error Logs Screen Verification")
  
    validate_localization(

        objects=[
                waitForObject(names.apollo_lbHeader_QLabel),
                waitForObjectExists(names.vIKAKOODI_HeaderViewItem),
                waitForObject(names.p_IV_MM_R_N_KELLONAIKA_HeaderViewItem),
                waitForObject(names.vIAN_KUVAUS_HeaderViewItem),
                waitForObjectItem(names.errorLogsPage_tvErrorLog_QTreeView, "Device Configuration Error Please restart the system\\. Contact manufacturer if the error persists\\._1"),
                waitForObjectExists(names.treatmentLogs_pbDownload_QPushButton)
      
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
           
