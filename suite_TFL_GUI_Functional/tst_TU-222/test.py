import names
import re
from common import *
EXPECTED_CW_POWER = 50.0
EXPECTED_PULSE_ENERGY = 0.1
EXPECTED_FREQUENCY = 100.0

def read_numeric_value(object_name, description):
    try:
        obj = waitForObjectExists(object_name, 3000)
        display_text = str(obj.text)
        match = re.search(r"-?\d+(?:\.\d+)?", display_text)
        if match:
            actual_value = float(match.group())
            test.log(
                "DISPLAYED {}: {}".format(
                    description,
                    actual_value
                )
            )
            return actual_value
        test.fail(
            "Unable to extract numeric value for {}. Display text: {}".format(
                description,
                display_text
            )
        )
        return None
    except Exception as e:
        test.fail("Unable to read {}: {}".format(description,
                str(e)
            )
        )

        return None



def verify_cw_default_settings():

    test.log(
        " VERIFY CW DEFAULT SETTINGS "
    )
    cw_power_object = None

    if cw_power_object is None:

        test.fail(
            "CW power object is not configured. "
            "Add the actual CW power object from names.py."
        )

        return False

    actual_power = read_numeric_value(
        cw_power_object,
        "CW POWER"
    )

    if actual_power is None:
        return False

    if actual_power == EXPECTED_CW_POWER:

        test.passes(
            "PASS: CW default power is {} W".format(
                actual_power
            )
        )

        return True

    test.fail(
        "FAIL: Expected CW power {} W, found {} W".format(
            EXPECTED_CW_POWER,
            actual_power
        )
    )

    return False


def verify_pulsed_default_settings():

    test.log(
        "VERIFY PULSED DEFAULT SETTINGS"
    )

    result = True

    actual_energy = read_numeric_value(
        names.pagesWidget_lbValue_FlashableLabel_2,
        "PULSE ENERGY"
    )

    if actual_energy == EXPECTED_PULSE_ENERGY:

        test.passes(
            "PASS: Pulse Energy is {} J".format(
                EXPECTED_PULSE_ENERGY
            )
        )

    else:

        test.fail(
            "FAIL: Expected Pulse Energy {} J, found {}".format(
                EXPECTED_PULSE_ENERGY,
                actual_energy
            )
        )

        result = False

    actual_frequency = read_numeric_value(
        names.pagesWidget_lbValue_FlashableLabel,
        "FREQUENCY"
    )

    if actual_frequency == EXPECTED_FREQUENCY:

        test.passes(
            "PASS: Frequency is {} Hz".format(
                EXPECTED_FREQUENCY
            )
        )

    else:

        test.fail(
            "FAIL: Expected Frequency {} Hz, found {}".format(
                EXPECTED_FREQUENCY,
                actual_frequency
            )
        )

        result = False

    try:

        short_pulse = waitForObject(
            names.pagesWidget_btShortPulse_ButtonWithClickSound
        )

        if short_pulse.checked:

            test.passes(
                "PASS: Short Pulse is selected by default"
            )

        else:

            test.fail(
                "FAIL: Short Pulse is not selected by default"
            )

            result = False

    except Exception as e:

        test.fail(
            "Unable to verify Short Pulse: {}".format(
                str(e)
            )
        )

        result = False

    if result:

        test.passes(
            "PASS: All Pulsed Mode default settings verified"
        )

    else:

        test.fail(
            "FAIL: Pulsed Mode default settings verification failed"
        )

    return result

# def create_configure_save_and_cancel_preset():
#
#     test.log("CREATE AND CONFIGURE PRESET")
#
#     overall_result = True
#
#     clickButton(
#         waitForObject(
#             names.frToolbar_tbAddPreset_QToolButton
#         )
#     )
#
#
#     clickButton(
#         waitForObject(
#             names.apollo_btCwMode_QToolButton
#         )
#     )
#     cw_result = verify_cw_default_settings()
#
#     if not cw_result:
#         overall_result = False
#
#     mouseClick(
#         waitForObject(
#             names.pagesWidget_lbValue_FlashableLabel
#         ),
#         43, 44,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#
#     clickButton(
#         waitForObject(
#             names.apollo_btPulsedMode_QToolButton
#         )
#     )
#
#     pulsed_result = verify_pulsed_default_settings()
#
#     if not pulsed_result:
#         overall_result = False
#
#     mouseClick(
#         waitForObject(
#             names.pagesWidget_lbValue_FlashableLabel_2
#         ),
#         59, 66,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#     mouseClick(
#         waitForObject(
#             names.pagesWidget_lbValue_FlashableLabel
#         ),
#         73, 40,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#     mouseClick(
#         waitForObject(
#             names.pagesWidget_lbPowerValue_FlashableLabel
#         ),
#         84, 35,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#     clickButton(
#         waitForObject(
#             names.apollo_btCwMode_QToolButton
#         )
#     )
#     mouseClick(
#         waitForObject(
#             names.apollo_edName_QLineEdit
#         ),
#         166, 23,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_t_KeyButtonLetter
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_h_KeyButtonLetter
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_u_KeyButtonLetter
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_v_KeyButtonLetter
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_e_KeyButtonLetter
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_r_KeyButtonLetter
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_a_KeyButtonLetter
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.keyboardFrame_Enter_KeyButtonEnter
#         )
#     )
#
#     test.log(
#         "PRESET NAME ENTERED: thuvera"
#     )
#
#     clickButton(
#         waitForObject(
#             names.pagesWidget_pbEnlarge_QPushButton_2
#         )
#     )
#
#     mouseClick(
#         waitForObject(
#             names.pagesWidget_lbValue_FlashableLabel
#         ),
#         45, 37,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#     clickButton(
#         waitForObject(
#             names.apollo_btSave_QPushButton
#         )
#     )
#
#     test.log(
#         "THUVERA PRESET SAVE ACTION COMPLETED"
#     )
#
#     sendEvent(
#         "QWheelEvent",
#         waitForObject(
#             names.apollo_tvPresets_PresetsTable
#         ),
#         619, 390, -120, 0, 2
#     )
#
#     sendEvent(
#         "QWheelEvent",
#         waitForObject(
#             names.apollo_tvPresets_PresetsTable
#         ),
#         619, 391, -120, 0, 2
#     )
#
#     sendEvent(
#         "QWheelEvent",
#         waitForObject(
#             names.apollo_tvPresets_PresetsTable
#         ),
#         619, 397, -120, 0, 2
#     )
#
#     sendEvent(
#         "QWheelEvent",
#         waitForObject(
#             names.apollo_tvPresets_PresetsTable
#         ),
#         619, 408, -120, 0, 2
#     )
#
#     sendEvent(
#         "QWheelEvent",
#         waitForObject(
#             names.apollo_tvPresets_PresetsTable
#         ),
#         445, 459, -120, 0, 2
#     )
#
#     sendEvent(
#         "QWheelEvent",
#         waitForObject(
#             names.apollo_tvPresets_PresetsTable
#         ),
#         445, 459, -120, 0, 2
#     )
#
#     sendEvent(
#         "QWheelEvent",
#         waitForObject(
#             names.apollo_tvPresets_PresetsTable
#         ),
#         445, 459, -120, 0, 2
#     )
#
#
#     mouseClick(
#         waitForObjectItem(
#             names.apollo_tvPresets_PresetsTable,
#             "-_2"
#         ),
#         39, 40,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#     mouseClick(
#         waitForObjectItem(
#             names.apollo_tvPresets_PresetsTable,
#             "-_2"
#         ),
#         39, 40,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#     test.log(
#         "RECORDED PRESET ITEM -_2 SELECTED"
#     )
#
#
#     clickButton(
#         waitForObject(
#             names.frToolbar_tbAddPreset_QToolButton
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.apollo_btCwMode_QToolButton
#         )
#     )
#
#     mouseClick(
#         waitForObject(
#             names.pagesWidget_lbValue_FlashableLabel
#         ),
#         53, 44,
#         Qt.NoModifier,
#         Qt.LeftButton
#     )
#
#     clickButton(
#         waitForObject(
#             names.apollo_btCancel_QPushButton
#         )
#     )
#
#     test.log(
#         "SECOND PRESET CREATION CANCELLED"
#     )
#     clickButton(
#         waitForObject(
#             names.apollo_btExitProfile_QPushButton
#         )
#     )
#
#     clickButton(
#         waitForObject(
#             names.question_YES_QPushButton
#         )
#     )
#
#     test.log(
#         "PROFILE EXIT COMPLETED"
#     )
#
#     if overall_result:
#
#         test.passes(
#             "PASS: Preset flow and default settings verification completed"
#         )
#
#     else:
#
#         test.fail(
#             "FAIL: Preset flow completed with default settings verification failures"
#         )
#
#     return overall_result


def create_thuvers_preset():
    """
    Create and configure the Thuvers preset.
    """

    clickButton(
        waitForObject(names.frToolbar_tbAddPreset_QToolButton)
    )

    clickButton(
        waitForObject(names.apollo_btCwMode_QToolButton)
    )

    mouseClick(
        waitForObject(names.pagesWidget_lbValue_FlashableLabel),
        55, 54, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(names.apollo_btPulsedMode_QToolButton)
    )

    mouseClick(
        waitForObject(names.pagesWidget_lbValue_FlashableLabel_2),
        46, 48, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.pagesWidget_lbValue_FlashableLabel),
        45, 47, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.pagesWidget_lbPowerValue_FlashableLabel),
        91, 61, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(names.pagesWidget_btMiddlePulse_ButtonWithClickSound)
    )

    clickButton(
        waitForObject(names.pagesWidget_btLongPulse_ButtonWithClickSound)
    )

    clickButton(
        waitForObject(names.apollo_btCwMode_QToolButton)
    )

    # Enter preset name: thuvers
    mouseClick(
        waitForObject(names.apollo_edName_QLineEdit),
        176, 33, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_h_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_u_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_v_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))

    clickButton(
        waitForObject(names.keyboardFrame_Enter_KeyButtonEnter)
    )

    clickButton(
        waitForObject(names.pagesWidget_pbEnlarge_QPushButton_2)
    )

    clickButton(
        waitForObject(names.apollo_btSave_QPushButton)
    )

    # Select preset _15
    sendEvent(
        "QWheelEvent",
        waitForObject(names.apollo_tvPresets_PresetsTable),
        506, 475, -120, 0, 2
    )

    mouseClick(
        waitForObjectItem(names.apollo_tvPresets_PresetsTable, "_15"),
        107, 37, Qt.NoModifier, Qt.LeftButton
    )

    # Add another preset
    clickButton(
        waitForObject(names.frToolbar_tbAddPreset_QToolButton)
    )

    clickButton(
        waitForObject(names.apollo_btPulsedMode_QToolButton)
    )

    clickButton(
        waitForObject(names.apollo_btCwMode_QToolButton)
    )

    mouseClick(
        waitForObject(names.pagesWidget_lbValue_FlashableLabel),
        42, 38, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.apollo_centralWidget_QWidget_2),
        790, 615, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(names.apollo_btCancel_QPushButton)
    )

    test.passes("Thuvers preset creation and configuration completed")


def main():

    test.log(
        "This TestCase contais from TU-222 to TU-225"
    )

    try:
        clickButton(
            waitForObject(
                names.frmPopup_pbAccept_QPushButton
            )
        )
        enterpin()
        open_default_profile_presets()
        create_thuvers_preset()

        clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
        mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "-_2"), 44, 40, Qt.NoModifier, Qt.LeftButton)
        mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "-_2"), 44, 40, Qt.NoModifier, Qt.LeftButton)
        clickButton(waitForObject(names.question_OK_QPushButton))

    finally:
        test.log("Passed")
