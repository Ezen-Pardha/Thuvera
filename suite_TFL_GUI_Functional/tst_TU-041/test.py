
# -*- coding: utf-8 -*-

import names
from common import *


def click_and_verify(button_name, description):

    try:
        button = waitForObject(button_name)
        clickButton(button)
        snooze(1)

        test.verify(
            True,
            description
        )

    except Exception as e:

        test.fail(
            "FAIL: {} | {}".format(description, str(e))
        )


def verify_object_exists(object_name, description):

    try:
        waitForObjectExists(object_name)

        test.verify(
            True,
            description
        )

    except Exception as e:

        test.fail(
            "FAIL: {} | {}".format(description, str(e))
        )


def main():

    enterpin()

    clickButton(
        waitForObject(names.frmPopup_pbAccept_QPushButton)
    )

    clickButton(
        waitForObject(names.sclProfiles_Default_ProfileButton)
    )

    snooze(2)


    verify_object_exists(
        names.apollo_centralWidget_QStackedWidget,
        "PASS: Treatment screen displayed"
    )

    click_and_verify(
        names.centralWidget_pbEnlarge_QPushButton,
        "PASS: Left pedal laser parameter changed"
    )

    click_and_verify(
        names.centralWidget_pbEnlarge_QPushButton_2,
        "PASS: Right pedal laser parameter changed"
    )

    verify_object_exists(
        names.centralWidget_pbSaveSettings_QPushButton,
        "PASS: Save Settings button displayed for left pedal"
    )

    verify_object_exists(
        names.centralWidget_pbSaveSettings_QPushButton,
        "PASS: Save Settings button displayed for right pedal"
    )

    clickButton(
        waitForObject(
            names.centralWidget_pbSaveSettings_QPushButton
        )
    )

    snooze(2)

    verify_object_exists(
        names.apollo_edName_QLineEdit,
        "PASS: Program navigated to Save Settings screen"
    )

    mouseClick(waitForObject(names.apollo_wdNavigationBar_QWidget), 61, 60, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btCancel_QPushButton))
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 471, 12, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Kidney Dust (High)"), 281, 49, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel_2), 45, 37, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Kidney Dust (High)"), 75, 29, Qt.NoModifier, Qt.LeftButton)


  
