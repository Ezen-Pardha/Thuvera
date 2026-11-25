# -*- coding: utf-8 -*-

import names
from common import *

def main():
    test.log("This TC contains TU-009 to TU-026")
    test.log("SVV TAG: Profile Selection Screen Product Name Displayed: TU-009")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    test.compare(waitForObjectExists(names.apollo_lbTitle_QLabel).visible, True)
    try:
        product_title = waitForObjectExists(names.apollo_lbTitle_QLabel)

        if product_title.visible:
            test.passes("Product name is displayed on the page.")
        else:
            test.fail("Product name is not displayed on the page.")

    except Exception as e:
        test.fail("Product name verification failed: " + str(e))

    
    test.log("SVV TAG: Profile Selection Screen Assistant Mode Button: TU-010")
    try:
        assistant_button = waitForObjectExists(names.apollo_tbAssistant_QToolButton)
    
        if assistant_button.isEnabled() and assistant_button.isVisible():
            clickButton(assistant_button)
            snooze(2)
            test.passes("Assistant button is clickable and clicked successfully.")
        else:
            test.fail("Assistant button is not enabled or visible.")

    except Exception as e:
        test.fail("Assistant button is not clickable: " + str(e))
 
    clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton))
    test.log("SVV TAG: Profile Selection Screen Add Profile Button: TU-014")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    test.passes("Keyboard Popup is verified successfully")
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
        test.passes("Test1 Profile created successfully")
    else:
        test.fail("Test1 Profile creation failed")
        
    test.log("SVV TAG: Profile Selection Screen Edit Profile Button: TU-015")
    clickButton(waitForObject(names.frToolbar_tbEditProfile_QToolButton))
    test.passes("Edit button is allow to edit the user profiles")
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    test.passes("Keyboard verified successfully")
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "<Backspace>") 
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    if str(waitForObjectExists(names.sclProfiles_Test_ProfileButton).text) == "Test":
        test.passes("Test Profile Updated successfully")
    else:
        test.fail("Test Profile Update failed")
    test.log("SVV TAG: Profile Selection Screen Delete Profile Button: TU-016")   
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    test.passes("Delete button is selected")
    clickButton(waitForObject(names.sclProfiles_Test_ProfileButton))
    test.passes("Profile selected from profile selection screen")
    if object.exists(names.question_OK_QPushButton):
        clickButton(waitForObject(names.question_OK_QPushButton))
        test.passes("profile Deleted successfully")
    else:
        test.fail("Profile is not Deleted")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    setWindowState(waitForObject(names.apollo_MainWindow), WindowState.Minimize)
    
    test.log("SVV TAG: Profile Selection Screen Default Profile Button Disabled: TU-017") 
    setWindowState(waitForObject(names.apollo_MainWindow), WindowState.Normal)
    clickButton(waitForObject(names.frToolbar_tbEditProfile_QToolButton))
    snooze(2)
    profile_button = waitForObjectExists(names.sclProfiles_Default_ProfileButton)
    
    if not profile_button.isEnabled():
        test.passes("Default Profile button is disabled after clicking Edit button, as expected")
    else:
        test.fail("Default Profile button is still enabled after clicking Edit button")

    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    snooze(2)
    
    profile_button = waitForObjectExists(names.sclProfiles_Default_ProfileButton)
    
    if not profile_button.isEnabled():
        test.passes("Default Profile button is disabled after clicking Delete button, as expected")
    else:
        test.fail("Default Profile button is still enabled after clicking Delete button")
    
    test.log("SVV TAG: Profile Selection Screen Assistant Mode Button Disabled: TU-018") 
     
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    snooze(2)

    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))

    profile_button = waitForObjectExists(names.apollo_tbAssistant_QToolButton) 
    if not profile_button.isEnabled():
        test.passes("Default Profile button is disabled after Delete Profile and Assistant button clicks, as expected")
    else:
        test.fail("Default Profile button is enabled after Delete Profile and Assistant button clicks")
        clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton))
        
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    snooze(2)
    
    assistant_button = waitForObjectExists(names.apollo_tbAssistant_QToolButton)
    
    if assistant_button.isEnabled():
        test.passes("Assistance button is able to click")
    else:
        test.fail("Assistant button not able to click")  
    test.log("SVV TAG: Profile Selection Screen Add Profile Button Disabled: TU-020")
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
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
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    snooze(2)
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_6_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    snooze(2)
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_7_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    snooze(2)
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_8_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    snooze(2)
    profile_button = waitForObjectExists(names.frToolbar_tbAddProfile_QToolButton)

    if not profile_button.isEnabled():
        test.passes("9th profile is unable to add because Add Profile button is not clickable.")
    else:
        clickButton(profile_button)
        test.fail("Add Profile button is clickable. 9th profile can be added.")
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    test.passes("Profile is Deleted")
    profile_button = waitForObjectExists(names.frToolbar_tbAddProfile_QToolButton)

    if profile_button.isEnabled():
        clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
        test.passes("Profile can created using add button")
    else:
        clickButton(profile_button)
        test.fail("Profile can not add using add button")
    
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    test.passes("Profile is Created")
    try:
        context = currentApplicationContext()
        context.detach()
        snooze(3)
        test.log("AUT context detached")
    except Exception as error:
        test.log("Error while closing AUT: " + str(error))
    startApplication("run.sh")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    test.log("SVV TAG: Profile Selection Screen Edit Profile Button Disabled: TU-021")
    delete_profile("Test2", names.sclProfiles_Test2_ProfileButton)
    delete_profile("Test3", names.sclProfiles_Test3_ProfileButton)
    delete_profile("Test4", names.sclProfiles_Test4_ProfileButton)
    delete_profile("Test5", names.sclProfiles_Test5_ProfileButton)
    delete_profile("Test6", names.sclProfiles_Test6_ProfileButton)
    delete_profile("Test7", names.sclProfiles_Test7_ProfileButton)
    delete_profile("Test8", names.sclProfiles_Test8_ProfileButton)
    edit_button = waitForObjectExists(names.frToolbar_tbEditProfile_QToolButton)

    if not edit_button.isEnabled():
        test.passes("Edit button is disabled because no user profiles are available on the screen.")
    else:
        clickButton(edit_button)
        test.fail("Edit button is enabled and clickable.")
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
    test.passes("Profile is Created")
    
    if edit_button.isEnabled():
        test.passes("Edit button is enabled and clickable.")
    else:
        test.fail("Edit button not enabled.")
    test.log("SVV TAG: Profile Selection Screen Delete Profile Button Disabled: TU-022")    
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    Delete_button = waitForObjectExists(names.frToolbar_tbDeleteProfile_QToolButton)

    if not Delete_button.isEnabled():
        test.passes("Delete button is disabled because no user profiles are available on the screen.")
    else:
        test.fail("Delete button is enabled and clickable.")
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
    test.passes("Profile is Created")
    Delete_button = waitForObjectExists(names.frToolbar_tbDeleteProfile_QToolButton)

    if Delete_button.isEnabled():
        test.passes("Delete button enable.")
    else:
        
        test.fail("Delete button not enable")
    
    test.log("SVV TAG: Profile Selection Screen Profile Buttons Scroll: TU-023")
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))   
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_2_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    
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
   
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))   
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_5_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))   
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_6_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))   
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_7_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))   
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_8_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    profile_screen = waitForObject(names.apollo_ProfileSelectionScreen_ProfileSelectionScreen)

    """Swipe Left"""
    mouseDrag(profile_screen, 500, 300, -350, 0,
              Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    test.passes("Left swipe performed on Profile Selection screen.")
    
    """ Swipe Right"""
    mouseDrag(profile_screen, 150, 300, 350, 0,
              Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    test.passes("Right swipe performed on Profile Selection screen.")
    
    test.log("SVV TAG: Profile Selection Screen Delete Profile Confirmation Popup: TU-024")
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    delete_message = str(waitForObjectExists(names.question_TextLabel_QLabel).text)

    if delete_message == "DELETE PROFILE?":
        test.passes("Delete Profile confirmation message identified successfully.")
    else:
        test.fail("Delete Profile confirmation message not identified. Actual message: " + delete_message)  
          
    test.log("SVV TAG: Profile Selection Screen Delete Profile Confirmation Popup Confirmed: TU-025")
    """Select Delete Profile button"""
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    snooze(1)
    test.passes("Delete Profile button selected successfully.")
    
    """Select Test1 profile"""
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(1)
    test.passes("Test1 profile selected for deletion.")
    
    """Verify delete confirmation message"""
    delete_message = str(waitForObjectExists(names.question_TextLabel_QLabel).text)
    
    if delete_message == "DELETE PROFILE?":
        test.passes("Delete Profile confirmation message identified successfully.")
    
        # 4. Select OK
        clickButton(waitForObject(names.question_OK_QPushButton))
        snooze(2)
        test.passes("Test1 profile deletion confirmed successfully.")
    else:
        test.fail("Delete confirmation message not identified. Actual message: " + delete_message) 

    test.log("SVV TAG: Profile Selection Screen Delete Profile Confirmation Popup Aborted: TU-026")   
    mouseClick(waitForObject(names.apollo_ProfileSelectionScreen_ProfileSelectionScreen), 653, 638, Qt.NoModifier, Qt.LeftButton)
    """ Select Delete Profile button"""
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    snooze(1)
    test.passes("Delete Profile mode activated successfully.")
    
    """ Select Test2 profile"""
    clickButton(waitForObject(names.sclProfiles_Test2_ProfileButton))
    snooze(1)
    test.passes("Test2 profile selected for deletion.")
    
    """Verify confirmation popup"""
    delete_message = str(waitForObjectExists(names.question_TextLabel_QLabel).text)
    
    if delete_message == "DELETE PROFILE?":
        test.passes("Delete Profile confirmation popup displayed successfully.")
    
        # 4. Select Cancel
        clickButton(waitForObject(names.question_CANCEL_QPushButton))
        snooze(2)
        test.passes("Cancel button selected successfully. Profile deletion cancelled.")
    
        """Verify Test2 profile is still present"""
        profile_button = waitForObjectExists(names.sclProfiles_Test2_ProfileButton)
    
        if profile_button.visible:
            test.passes("Test2 profile is still present on the Profile Selection screen.")
        else:
            test.fail("Test2 profile is not present on the Profile Selection screen.")
    else:
        test.fail("Delete Profile confirmation popup not displayed. Actual message: " + delete_message) 
    
    snooze(2)
    delete_profile("Test1", names.sclProfiles_Test1_ProfileButton)
    delete_profile("Test2", names.sclProfiles_Test2_ProfileButton)
    delete_profile("Test3", names.sclProfiles_Test3_ProfileButton)
    delete_profile("Test4", names.sclProfiles_Test4_ProfileButton)
    delete_profile("Test5", names.sclProfiles_Test5_ProfileButton)
    delete_profile("Test6", names.sclProfiles_Test6_ProfileButton)
    delete_profile("Test7", names.sclProfiles_Test7_ProfileButton)
    delete_profile("Test8", names.sclProfiles_Test8_ProfileButton)       
