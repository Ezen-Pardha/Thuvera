
# -*- coding: utf-8 -*-

import names
from common import *

def select_profile(profile_name, scroll_distance):
    scrollArea = waitForObject(names.sclProfiles_scrollAreaWidgetContents_QWidget)

    mouseDrag(scrollArea, 641, 268, scroll_distance, 0, 1, Qt.LeftButton)
    snooze(2)

    clickButton(waitForObject(profile_name))
    snooze(2)


def main():
    test.log("This TC contains TG-026 & TG-028")
    test.log("SVV TAG: User Profiles- TG-026")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton, 1147693))
    enterpin()

    """Create Test1"""
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    test.passes("Keyboard Popup is displayed successfully.")

    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

    if str(waitForObjectExists(names.sclProfiles_Test1_ProfileButton).text) == "Test1":
        test.passes("Test1 profile is created successfully.")
    else:
        test.fail("Test1 profile is not displayed.")

    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    test.passes("Treatment screen is verified successfully.")
    snooze(2)

    """Exit Test1"""
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))

    """Create Test2"""
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

    
    if str(waitForObjectExists(names.sclProfiles_Test2_ProfileButton).text) == "Test2":
        test.passes("Test2 profile is created successfully.")
    else:
        test.fail("Test2 profile is not displayed.")

    clickButton(waitForObject(names.sclProfiles_Test2_ProfileButton))
    test.passes("Treatment screen is verified successfully.")
    snooze(2)

    """Exit Test2"""
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))

    """Create Test3"""
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))

    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test3_ProfileButton).text) == "Test3":
        test.passes("Test3 profile is created successfully.")
    else:
        test.fail("Test3 profile is not displayed.")

    clickButton(waitForObject(names.sclProfiles_Test3_ProfileButton))
    test.passes("Treatment screen is verified successfully.")
    snooze(2)

    snooze(2)

    """Select Test3 using horizontal scroll"""
    select_profile(names.sclProfiles_Test3_ProfileButton, -200)

    """Exit and delete Test3"""
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))

    """Create Test4"""
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))

    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test4_ProfileButton).text) == "Test4":
        test.passes("Test4 profile is created successfully.")
    else:
        test.fail("Test4 profile is not displayed.")

    clickButton(waitForObject(names.sclProfiles_Test4_ProfileButton))
    test.passes("Treatment screen is verified successfully.")

    snooze(2)

    """Select Test4 using horizontal scroll"""
    select_profile(names.sclProfiles_Test4_ProfileButton, -250)

    """ Exit and delete Test4"""
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))

    """Create Test5"""
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))

    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    snooze(2)
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test5_ProfileButton).text) == "Test5":
        test.passes("Test5 profile is created successfully.")
    else:
        test.fail("Test5 profile is not displayed.")

    clickButton(waitForObject(names.sclProfiles_Test5_ProfileButton))
    test.passes("Treatment screen is verified successfully.")
    snooze(4) 
    select_profile(names.sclProfiles_Test5_ProfileButton, -400)
    snooze(4)
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    try:
        context = currentApplicationContext()
        context.detach()
        snooze(3)
        test.log("AUT context detached")
    except Exception as error:
        test.log("Error while closing AUT: " + str(error))
    startApplication("run.sh")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton, 1147693))
    enterpin()
    profiles = [
    (names.sclProfiles_Test1_ProfileButton, "Test1"),
    (names.sclProfiles_Test2_ProfileButton, "Test2"),
    (names.sclProfiles_Test3_ProfileButton, "Test3"),
    (names.sclProfiles_Test4_ProfileButton, "Test4"),
    (names.sclProfiles_Test5_ProfileButton, "Test5")]

    for profile_name, expected_text in profiles:
        profile = waitForObjectExists(profile_name)

        if str(profile.text) == expected_text:
            test.passes(expected_text + " Newly created User profile is present and verified.")
        else:
            test.fail(expected_text + " Newly created User profile not found.")
            
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(3)
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test2_ProfileButton))
    snooze(3)
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test3_ProfileButton))
    snooze(3)
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test4_ProfileButton))
    snooze(3)
    clickButton(waitForObject(names.question_OK_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test5_ProfileButton))
    snooze(3)
    clickButton(waitForObject(names.question_OK_QPushButton))

    test.log("SVV TAG: Maximum User Profiles - TG-028")

    """Create Test1"""
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    test.passes("Keyboard Popup is displayed successfully.")

    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

    if str(waitForObjectExists(names.sclProfiles_Test1_ProfileButton).text) == "Test1":
        test.passes("Test1 profile is created successfully.")
    else:
        test.fail("Test1 profile is not displayed.")
  
    snooze(2)

    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

    if str(waitForObjectExists(names.sclProfiles_Test2_ProfileButton).text) == "Test2":
        test.passes("Test2 profile is created successfully.")
    else:
        test.fail("Test2 profile is not displayed.")
    
    snooze(2)

    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_3_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test3_ProfileButton).text) == "Test3":
        test.passes("Test3 profile is created successfully.")
    else:
        test.fail("Test3 profile is not displayed.")
    snooze(2)

    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_4_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test4_ProfileButton).text) == "Test4":
        test.passes("Test4 profile is created successfully.")
    else:
        test.fail("Test4 profile is not displayed.")
    snooze(2)
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    snooze(2)
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test5_ProfileButton).text) == "Test5":
        test.passes("Test5 profile is created successfully.")
    else:
        test.fail("Test5 profile is not displayed.")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_6_KeyButtonLetter))
    snooze(2)
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test6_ProfileButton).text) == "Test6":
        test.passes("Test6 profile is created successfully.")
    else:
        test.fail("Test6 profile is not displayed.")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_7_KeyButtonLetter))
    snooze(2)
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test7_ProfileButton).text) == "Test7":
        test.passes("Test7 profile is created successfully.")
    else:
        test.fail("Test7 profile is not displayed.")
  
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_8_KeyButtonLetter))
    snooze(2)
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test8_ProfileButton).text) == "Test8":
        test.passes("Test8 profile is created successfully.")
    else:
        test.fail("Test8 profile is not displayed.")

    addProfileButton = waitForObjectExists(names.frToolbar_tbAddProfile_QToolButton)

    if not addProfileButton.enabled:
        test.passes("Add Profile button is disabled - unable to add 9th profile")
    else:
        test.fail("Add Profile button is enabled - a new profile can be added")   
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(3)
    snooze(3)
    clickButton(waitForObject(names.question_OK_QPushButton))
    test.passes("Profile is Deleted Successfully")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))      
    addProfileButton = waitForObjectExists(names.frToolbar_tbAddProfile_QToolButton)
    test.passes("Profile is created")
    if not addProfileButton.enabled:
        test.passes("Add Profile button is disabled - unable to add 9th profile")
    else:
        test.fail("Add Profile button is enabled - a new profile can be added") 
    
    snooze(3)
    

