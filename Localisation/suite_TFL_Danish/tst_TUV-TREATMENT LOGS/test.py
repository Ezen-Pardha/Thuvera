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
    clickButton(waitForObject(names.apollo_btTreatmentLogs_QPushButton))

    validate_localization(

        objects=[
            
            waitForObject(names.apollo_lbHeader_QLabel), 
            waitForObject(names.frmHeader_lbDate_QLabel), 
            waitForObject(names.frmHeader_lbTime_QLabel), 
            waitForObject(names.frmHeader_lbLasingTime_QLabel), 
            waitForObject(names.frmHeader_lbTotal_QLabel), 
            waitForObject(names.frmHeader_lbFiber_QLabel),
            waitForObjectExists(names.apollo_pbDownload_QPushButton)
        ],

        screen_name="TREATMENT LOGS",

        expected_strings=[
            
            "TREATMENT LOGS",
            "DATE",
            "TIME",
            "LASING TIME",
            "TOTAL Kj",
            "FIBER",
            "DOWNLOAD"
        ],
    )
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "BEHANDLINGSLOGFILER")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "BEHANDLINGSLOGFILER": 
        test.passes("TREATMENT LOGS Screen verified")
    else: test.fail("TREATMENT LOGS Screen verification failed")





