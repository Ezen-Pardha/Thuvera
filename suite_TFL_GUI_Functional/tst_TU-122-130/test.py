
# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enterpin()
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    
    snooze(2)
    preset_table = waitForObject(
        names.apollo_tvPresets_PresetsTable
    )

    test.verify(
        preset_table.visible,
        "PASS: Presets table is displayed"
    )

 
    user_preset = waitForObjectItem(
        names.apollo_tvPresets_PresetsTable,
        "kidney"
    )

    test.verify(
        user_preset is not None,
        "PASS: Kidney preset is displayed"
    )

 
    headers = [
        (names.pRESET_NAME_HeaderViewItem, "Preset Name"),
        (names.eNERGY_HeaderViewItem, "Pulse Energy"),
        (names.fREQUENCY_HeaderViewItem, "Frequency"),
        (names.pOWER_HeaderViewItem, "Average Power"),
        (names.pULSE_WIDTH_HeaderViewItem, "Pulse Width")
    ]

    for header, description in headers:

        obj = waitForObject(header)

        test.verify(
            obj.visible,
            "PASS: {} header is displayed".format(description)
        )

  
    sendEvent(
        "QWheelEvent",
        preset_table,
        500, 300,
        -120, 0, 2
    )

    snooze(1)

    test.verify(
        preset_table.visible,
        "PASS: Preset list remains displayed after scrolling"
    )

