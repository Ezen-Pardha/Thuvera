
# -*- coding: utf-8 -*-

import names


def verifyPower():
    energy = float(str(waitForObject(names.centralWidget_lbValue_FlashableLabel).text))
    frequency = float(str(waitForObject(names.centralWidget_lbValue_FlashableLabel_2).text))

    mouseClick(
        waitForObject(names.centralWidget_lbPowerValue_FlashableLabel),
        23, 28, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.centralWidget_lbPower_QLabel),
        40, 11, Qt.NoModifier, Qt.LeftButton
    )

    power = float(str(waitForObject(names.centralWidget_lbPowerValue_FlashableLabel).text))

    message = (
        "Energy = %.2f J | Frequency = %.2f Hz | "
        "Displayed Maximum Power = %.2f W"
        % (energy, frequency, power)
    )

    if 2 <= power <= 60:
        test.passes(message + " | Power limit is within 2W-60W")
    else:
        test.fail(message + " | Power limit is outside 2W-60W")


def main():
    sendEvent(
        "QMoveEvent",
        waitForObject(names.apollo_MainWindow),
        103, 80, 713, 99
    )

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))

    for i in range(4):
        clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))

    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))

    verifyPower()

    adjustment_sequence = [
        (names.centralWidget_pbEnlarge_QPushButton, 3),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 3),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 3),
        (names.centralWidget_pbEnlarge_QPushButton_3, 3),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 3),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1),
        (names.centralWidget_pbEnlarge_QPushButton, 1),
        (names.centralWidget_pbEnlarge_QPushButton_3, 1)
    ]

    for button, count in adjustment_sequence:
        for i in range(count):
            clickButton(waitForObject(button))
            snooze(1)
            verifyPower()
