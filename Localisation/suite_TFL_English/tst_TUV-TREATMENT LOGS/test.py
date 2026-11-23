# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_treatment_logs()

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
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "TREATMENT LOGS")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "TREATMENT LOGS": 
        test.passes("TREATMENT LOGS Screen verified")
    else: test.fail("TREATMENT LOGS Screen verification failed")





