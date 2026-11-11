# -*- coding: utf-8 -*-

import names
from common import *


def verify_screen(description, object_name):
    try:
        waitForObjectExists(object_name)
        test.passes(description)
        return True
    except Exception as error:
        test.fail(description + " | " + str(error))
        return False


def verify_popup():
    return verify_screen(
        "Exit Profile confirmation popup displayed",
        names.apollo_Question_MessageBox
    )


def exit_to_treatment():
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    snooze(1)


def main():

    enterpin()

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    snooze(2)

    clickButton(waitForObject(names.apollo_btTreatmentLogs_QPushButton))
    snooze(1)

    verify_screen(
        "Treatment Logs screen opened from Treatment screen",
        names.frmTable_logView_QTreeView
    )

    mouseClick(
        waitForObject(names.frmTable_logView_QTreeView),
        227, 140,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.apollo_lbHeader_QLabel),
        278, 13,
        Qt.NoModifier,
        Qt.LeftButton
    )

   
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    snooze(1)

    verify_screen(
        "Settings screen opened from Treatment Logs",
        names.centralWidget_sldBrightness_QSlider
    )

   
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    snooze(1)

    verify_screen(
        "Utilities screen opened from Settings",
        names.stackedWidget_systemInformationPage_QFrame
    )

    mouseClick(
        waitForObject(names.stackedWidget_systemInformationPage_QFrame),
        363, 77,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.stackedWidget_systemInformationPage_QFrame),
        275, 443,
        Qt.NoModifier,
        Qt.LeftButton
    )

  

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))

    verify_popup()

    
    clickButton(waitForObject(names.question_YES_QPushButton))
    snooze(2)

    verify_screen(
        "Program exits to Profile Selection screen",
        names.apollo_ProfileSelectionScreen_ProfileSelectionScreen
    )