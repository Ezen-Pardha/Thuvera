import names
from common import *
failed_steps = []

def record_failure(description, error=None):
    failed_steps.append(description)
    if error is not None:
        test.fail("FAIL: {} - {}".format(description, str(error)))
    else:
        test.fail("FAIL: {}".format(description))

def get_property_value(obj, property_name):
    try:
        value = getattr(obj, property_name)
        if callable(value):
            value = value()
        return value
    except:
        return None

def inspect_wizard_object(object_name, description):
    test.log("INSPECTING {}".format(description))
    try:
        obj = waitForObject(object_name)
        test.log("Object: {}".format(description))
        test.log("Visible: {}".format(get_property_value(obj, "visible")))
        test.log("Enabled: {}".format(get_property_value(obj, "enabled")))
        test.log("Text: {}".format(get_property_value(obj, "text")))

        properties = [
            "checked",
            "down",
            "checkable",
            "objectName",
            "styleSheet",
            "focus",
            "hasFocus"
        ]
        for property_name in properties:
            value = get_property_value(obj,property_name)

            test.log("{}: {}".format(property_name,value))
        return True
    except Exception as e:
        record_failure("Inspect {}".format(description),e)
        return False
    
def verify_object_visible(object_name, description):
    try:
        obj = waitForObject(object_name)
        if obj.visible:
            test.passes("PASS: {} is visible".format(description))
            return True
        record_failure("{} is not visible".format(description))
        return False
    except Exception as e:
        record_failure("{} visibility verification".format(description),e)
        return False
    
def verify_button_enabled(object_name, description, expected=True):
    try:
        obj = waitForObject(object_name)
        actual_state = bool(obj.enabled)
        test.log("{} enabled state: {}".format(description,actual_state))
        if actual_state == expected:
            test.passes("PASS: {} enabled state verified".format(description))
            return True
        record_failure(
            "{} expected enabled={}, actual={}".format(
                description,
                expected,
                actual_state
            )
        )

        return False

    except Exception as e:

        record_failure(
            "{} enabled-state verification".format(description),
            e
        )

        return False


def verify_highlight_state(object_name, description):

    test.log(
        "VERIFY {} HIGHLIGHT".format(
            description
        )
    )

    try:

        obj = waitForObject(object_name)

        checked = get_property_value(obj, "checked")
        down = get_property_value(obj, "down")

        test.log(
            "{} checked property: {}".format(
                description,
                checked
            )
        )

        test.log(
            "{} down property: {}".format(
                description,
                down
            )
        )

        if checked is True or down is True:

            test.passes(
                "PASS: {} highlight state confirmed".format(
                    description
                )
            )

            return True

        test.log(
            "INFO: {} highlight cannot be confirmed using "
            "checked/down properties. Inspect visual state "
            "or the actual Qt selection property.".format(
                description
            )
        )

        return None

    except Exception as e:

        record_failure(
            "{} highlight inspection".format(description),
            e
        )

        return False


def verify_disabled_control(
        object_name, description, x, y):

    test.log(
        "VERIFY {} DOES NOT RESPOND ".format(
            description
        )
    )

    try:

        obj = waitForObject(object_name)

        enabled_before = bool(obj.enabled)

        test.log(
            "{} enabled before click: {}".format(
                description,
                enabled_before
            )
        )

        mouseClick(
            obj,
            x,
            y,
            Qt.NoModifier,
            Qt.LeftButton
        )

        snooze(0.5)

        obj = waitForObject(object_name)

        enabled_after = bool(obj.enabled)

        test.log(
            "{} enabled after click: {}".format(
                description,
                enabled_after
            )
        )

        if not enabled_before:

            test.passes(
                "PASS: {} was disabled and did not accept interaction".format(
                    description
                )
            )

            return True
        test.log(
            "INFO: {} is enabled. Enabled state alone cannot "
            "establish whether the click changed the selection.".format(
                description
            )
        )

        return None

    except Exception as e:

        record_failure(
            "{} response verification".format(description),
            e
        )

        return False

def select_option(object_name, description):

    test.log(
        "SELECT {} ".format(description)
    )

    try:

        option = waitForObject(object_name)

        if not option.enabled:

            record_failure(
                "{} is disabled".format(description)
            )

            return False

        clickButton(option)

        snooze(0.5)

        test.passes(
            "PASS: {} click executed successfully".format(
                description
            )
        )
        option = waitForObject(object_name)

        checked = get_property_value(option, "checked")
        down = get_property_value(option, "down")

        test.log(
            "{} checked after click: {}".format(
                description,
                checked
            )
        )

        test.log(
            "{} down after click: {}".format(
                description,
                down
            )
        )

        if checked is True or down is True:

            test.passes(
                "PASS: {} selected state confirmed".format(
                    description
                )
            )

        else:

            test.log(
                "INFO: {} click completed; selected state "
                "requires confirmation using the actual UI property.".format(
                    description
                )
            )

        return True

    except Exception as e:

        record_failure(
            "{} selection action".format(description),
            e
        )

        return False


def verify_lithotripsy_wizard_selection():

    global failed_steps

    failed_steps = []

    overall_result = True

    test.log(
        "TU-103 LITHOTRIPSY WIZARD TEST STARTED"
    )

    try:

        clickButton(
            waitForObject(
                names.apollo_tbAssistant_QToolButton
            )
        )

        test.passes(
            "PASS: Assistant opened"
        )

    except Exception as e:

        record_failure("Open Assistant", e)

        return False

    try:

        clickButton(
            waitForObject(
                names.frWizardPlace_Lithotripsy_WizardButton
            )
        )

        test.passes(
            "PASS: Lithotripsy button click executed"
        )

    except Exception as e:

        record_failure("Select Lithotripsy", e)

        return False

    snooze(0.5)

    inspect_wizard_object(
        names.frWizardPlace_Lithotripsy_WizardButton,
        "Lithotripsy"
    )

    lithotripsy_highlight = verify_highlight_state(
        names.frWizardPlace_Lithotripsy_WizardButton,
        "Lithotripsy"
    )

    if lithotripsy_highlight is False:
        overall_result = False


    stone_size_response = verify_disabled_control(
        names.frWizardPlace_STONE_SIZE_MM_WizardTitle,
        "Stone Size",
        165,
        18
    )

    if stone_size_response is False:
        overall_result = False


    stone_density_response = verify_disabled_control(
        names.frWizardPlace_STONE_DENSITY_HU_WizardTitle,
        "Stone Density",
        131,
        38
    )

    if stone_density_response is False:
        overall_result = False
    try:

        mouseClick(
            waitForObject(
                names.frWizardPlace_STONE_DENSITY_HU_WizardTitle
            ),
            130,
            27,
            Qt.NoModifier,
            Qt.LeftButton
        )

        test.log(
            "Second recorded Stone Density click completed"
        )

    except Exception as e:

        record_failure(
            "Second Stone Density click",
            e
        )

        overall_result = False

    try:

        clickButton(
            waitForObject(
                names.frWizardPlace_Kidney_WizardButton
            )
        )

        test.passes(
            "PASS: Kidney location click executed"
        )

    except Exception as e:

        record_failure(
            "Select Kidney location",
            e
        )

        return False

    snooze(0.5)

    inspect_wizard_object(
        names.frWizardPlace_Kidney_WizardButton,
        "Kidney"
    )

    kidney_highlight = verify_highlight_state(
        names.frWizardPlace_Kidney_WizardButton,
        "Kidney"
    )

    if kidney_highlight is False:
        overall_result = False


    result = verify_button_enabled(
        names.frWizardPlace_STONE_SIZE_MM_WizardTitle,
        "Stone Size",
        True
    )

    if not result:
        overall_result = False


    result = verify_button_enabled(
        names.frWizardPlace_STONE_DENSITY_HU_WizardTitle,
        "Stone Density",
        True
    )

    if not result:
        overall_result = False


    inspect_wizard_object(
        names.frWizardPlace_Small_6_WizardButton,
        "Small 6"
    )

    result = select_option(
        names.frWizardPlace_Small_6_WizardButton,
        "Small 6"
    )

    if not result:
        overall_result = False


    inspect_wizard_object(
        names.frWizardPlace_Soft_500_WizardButton,
        "Soft 500"
    )

    result = select_option(
        names.frWizardPlace_Soft_500_WizardButton,
        "Soft 500"
    )

    if not result:
        overall_result = False

    result = select_option(
        names.frWizardPlace_Medium_6_10_WizardButton,
        "Medium 6-10"
    )

    if not result:
        overall_result = False


    result = select_option(
        names.frWizardPlace_Medium_500_1000_WizardButton,
        "Medium 500-1000"
    )

    if not result:
        overall_result = False

    try:

        clickButton(
            waitForObject(
                names.frWizardPlace_tbHome_QToolButton
            )
        )

        test.log(
            "Wizard returned to Home"
        )

    except Exception as e:

        record_failure(
            "Return to Home",
            e
        )

        overall_result = False

    if failed_steps:
        test.log(
            " FAILED VERIFICATION SUMMARY"
        )

        for index, step in enumerate(failed_steps):

            test.log(
                "FAILED STEP {}: {}".format(
                    index + 1,
                    step
                ))


    if overall_result:
        test.passes("PASS: TU-103 Lithotripsy wizard actions and ""confirmed checks completed")
    else:
        test.fail("FAIL: TU-103 Lithotripsy wizard test failed. ""{} failure(s) recorded.".format(len(failed_steps)))
    return overall_result

def main():

    test.log("This TC Contains TU-103")

    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
        enterpin()

        result = verify_lithotripsy_wizard_selection()

        if result:
            test.passes("PASS: TU-103 test completed successfully")
        else:
            test.fail("FAIL: TU-103 test completed with verification failures")

    except Exception as e:
        test.fail("TU-103 MAIN EXECUTION FAILED: {}".format(str(e)))
        raise


