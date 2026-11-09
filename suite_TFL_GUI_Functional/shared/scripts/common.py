from squish import *
import os
import test
import datetime
import names

def enterpin():
    """Login to the application by accepting the popup and entering PIN 0000."""
    for i in range(4):
            clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton, 20000))
    
    test.passes("PASS: PIN 0000 entered")


def exit_default_profile():
    """Select Default Profile and confirm exit."""

    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")

        clickButton(waitForObject(
            names.apollo_btExitProfile_QPushButton, 20000))
        test.passes("PASS: Exit Profile clicked")

        clickButton(waitForObject(
            names.question_YES_QPushButton, 20000))
        test.passes("PASS: Exit Profile confirmed")

    except Exception as error:
        test.fail("FAIL: Exit Default Profile - {}".format(error))
        raise
   
 
def navigate_to_kidney_lithotripsy():
    """Navigate to Assistant → Lithotripsy → Kidney."""

    try:
        clickButton(waitForObject(names.apollo_tbAssistant_QToolButton, 20000))
        test.passes("PASS: Assistant screen opened")

        clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton, 20000))
        test.passes("PASS: Lithotripsy selected")

        clickButton(waitForObject(names.frWizardPlace_Kidney_WizardButton, 20000))
        test.passes("PASS: Kidney selected")

    except Exception as error:
        test.fail("FAIL: Navigate to Kidney Lithotripsy - {}".format(error))
        raise
  
 
def navigate_to_ureter_lithotripsy():
    """Navigate to Lithotripsy → Ureter."""

    try:
        clickButton(waitForObject(
            names.frWizardPlace_Lithotripsy_WizardButton, 20000))
        test.passes("PASS: Lithotripsy selected")

        clickButton(waitForObject(
            names.frWizardPlace_Ureter_WizardButton, 20000))
        test.passes("PASS: Ureter selected")

    except Exception as error:
        test.fail("FAIL: Navigate to Ureter Lithotripsy - {}".format(error))
        raise
   
 
def navigate_to_bladder_lithotripsy():
    """Navigate to Lithotripsy → Bladder."""

    try:
        clickButton(waitForObject(
            names.frWizardPlace_Lithotripsy_WizardButton, 20000))
        test.passes("PASS: Lithotripsy selected")

        clickButton(waitForObject(
            names.frWizardPlace_Bladder_WizardButton, 20000))
        test.passes("PASS: Bladder selected")

    except Exception as error:
        test.fail("FAIL: Navigate to Bladder Lithotripsy - {}".format(error))
        raise
   
 
def navigate_to_vaporize_hemostasis():
    """Navigate to Soft Tissue → Vaporize Hemostasis."""

    try:
        clickButton(waitForObject(
            names.frWizardPlace_Soft_Tissue_WizardButton, 20000))
        test.passes("PASS: Soft Tissue selected")

        clickButton(waitForObject(
            names.frWizardPlace_Vaporize_Hemostasis_WizardButton, 20000))
        test.passes("PASS: Vaporize Hemostasis selected")

    except Exception as error:
        test.fail("FAIL: Navigate to Vaporize Hemostasis - {}".format(error))
        raise


def navigate_to_tumor_hemostasis():
    """Navigate to Soft Tissue → Tumor Hemostasis."""

    try:
        clickButton(waitForObject(
            names.frWizardPlace_Soft_Tissue_WizardButton, 20000))
        test.passes("PASS: Soft Tissue selected")

        clickButton(waitForObject(
            names.frWizardPlace_Tumor_Hemostasis_WizardButton, 20000))
        test.passes("PASS: Tumor Hemostasis selected")

    except Exception as error:
        test.fail("FAIL: Navigate to Tumor Hemostasis - {}".format(error))
        raise
  
    
def navigate_to_incision_hemostasis():
    """Navigate to Soft Tissue → Incision Hemostasis."""

    try:
        clickButton(waitForObject(
            names.frWizardPlace_Soft_Tissue_WizardButton, 20000))
        test.passes("PASS: Soft Tissue selected")

        clickButton(waitForObject(
            names.frWizardPlace_Incision_Hemostasis_WizardButton, 20000))
        test.passes("PASS: Incision Hemostasis selected")

    except Exception as error:
        test.fail("FAIL: Navigate to Incision Hemostasis - {}".format(error))
        raise



def navigate_to_bph_enucleation_hemostasis():
    """Navigate to BPH → Enucleation Hemostasis."""

    try:
        clickButton(waitForObject(
            names.frWizardPlace_BPH_WizardButton, 20000))
        test.passes("PASS: BPH selected")

        clickButton(waitForObject(
            names.frWizardPlace_Enucleation_Hemostasis_WizardButton, 20000))
        test.passes("PASS: Enucleation Hemostasis selected")

    except Exception as error:
        test.fail("FAIL: Navigate to BPH Enucleation Hemostasis - {}".format(error))
        raise
 
    
def navigate_to_bph_enucleation_low_power():
    """Navigate to BPH → Enucleation Low Power."""

    try:
        clickButton(waitForObject(
            names.frWizardPlace_BPH_WizardButton, 20000))
        test.passes("PASS: BPH selected")

        clickButton(waitForObject(
            names.frWizardPlace_Enucleation_Low_Power_WizardButton, 20000))
        test.passes("PASS: Enucleation Low Power selected")

    except Exception as error:
        test.fail("FAIL: Navigate to BPH Enucleation Low Power - {}".format(error))
        raise  
    
    
def open_default_profile_presets():
    """Select Default Profile and open Presets."""

    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")

        clickButton(waitForObject(
            names.apollo_btPresets_QPushButton, 20000))
        test.passes("PASS: Presets screen opened")

    except Exception as error:
        test.fail("FAIL: Open Default Profile Presets - {}".format(error))
        raise
  
    
def open_default_profile_treatment_logs():
    """Select Default Profile and open Treatment Logs."""

    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")

        clickButton(waitForObject(
            names.apollo_btTreatmentLogs_QPushButton, 20000))
        test.passes("PASS: Treatment Logs screen opened")

    except Exception as error:
        test.fail("FAIL: Open Default Profile Treatment Logs - {}".format(error))
        raise
    
def open_default_profile_settings():
    """Select Default Profile and open Settings."""

    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")

        clickButton(waitForObject(
            names.apollo_btSettings_QPushButton, 20000))
        test.passes("PASS: Settings screen opened")

    except Exception as error:
        test.fail("FAIL: Open Default Profile Settings - {}".format(error))
        raise
    

def open_default_profile_utilities():
    """Select Default Profile and open Utilities."""

    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")

        clickButton(waitForObject(
            names.apollo_btUtilities_QPushButton, 20000))
        test.passes("PASS: Utilities screen opened")

    except Exception as error:
        test.fail("FAIL: Open Default Profile Utilities - {}".format(error))
        raise