# -*- coding: utf-8 -*-

import names

def enter_service_passcode():
    clickButton(waitForObject(names.wdKeypad_pushButton_7_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_4_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_1_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_4_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_7_QPushButton))

def main():
    test.log("This TC contains TU-287 to TU-290")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    sendEvent("QMouseEvent", waitForObject(names.passwordScreen_pbService_QPushButton), QEvent.MouseButtonPress, 15, 19, Qt.LeftButton, 1, 0)
    clickButton(waitForObject(names.serviceModePasswordScreen_pbBackspace_QPushButton, 38232))
    clickButton(waitForObject(names.serviceModePasswordScreen_pbBackspace_QPushButton))

    test.log("SVV TAG: Service Mode Passcode Screen TU-287")
    if str(waitForObjectExists(names.serviceModePasswordScreen_lbLogo_QLabel).text) == "SERVICE MODE":
        test.passes("Service Mode Passcode screen is displayed successfully.")
    else:
        test.fail("Service Mode Passcode screen is not displayed.")

    test.log("SVV TAG: Service Mode Passcode Invalid TU-288")
    clickButton(waitForObject(names.wdKeypad_pushButton_1_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_2_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_3_QPushButton_2))
    clickButton(waitForObject(names.wdKeypad_pushButton_4_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_5_QPushButton_2))

    if str(waitForObjectExists(names.serviceModePasswordScreen_mInvalidPassNotif_QLabel).text) == "Invalid Service Passcode":
        test.passes("Invalid Service Passcode message is displayed successfully.")
    else:
        test.fail("Invalid Service Passcode message is not displayed.")
        
    test.log("SVV TAG: Service Mode Passcode Valid TU-289")
    enter_service_passcode()
    
    if str(waitForObjectExists(names.serviceModeScreen_lbTopTitle_QLabel).text) == "SERVICE MODE":
        test.passes("Service Mode Login is successful using valid passcode.")
    else:
        test.fail("Service Mode Login is not successful using valid passcode.")

    mouseClick(waitForObject(names.serviceModeScreen_tabWidget_QTabWidget), 720, 72, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.serviceModeScreen_pbExit_QPushButton))

    test.log("SVV TAG: Service Mode Passcode Valid TU-290") 
    sendEvent("QMouseEvent", waitForObject(names.passwordScreen_pbService_QPushButton), QEvent.MouseButtonPress, 15, 19, Qt.LeftButton, 1, 0)
    clickButton(waitForObject(names.serviceModePasswordScreen_pbBackspace_QPushButton, 38232))
    clickButton(waitForObject(names.serviceModePasswordScreen_pbBackspace_QPushButton))
    enter_service_passcode()
    clickButton(waitForObject(names.serviceModeScreen_pbExit_QPushButton))
    test.passes("Service screen Exit Button is clicked successfully")
    if waitForObjectExists(names.passwordScreen_lbLogo_QLabel).visible:
        test.passes("Login screen is successfully displayed.")
    else:
        test.fail("Login screen is not displayed.")

    


