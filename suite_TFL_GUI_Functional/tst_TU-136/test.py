from common import *
import names
import test
from squish import *

def create_preset(preset_name, configure_callback=None):
    """
    WHEN user need to create a new preset,
    THEN click Add Preset and enter the preset name,
    AND save the preset.
    WHEN the preset name already exists,
    THEN close the warning popup and cancel the creation.
    AND verify whether the new preset was created successfully.
    """
    try:
        test.log("REQUESTED PRESET CREATION: {}".format(preset_name))
        clickButton(
            waitForObject(names.frToolbar_tbAddPreset_QToolButton)
        )
        mouseClick(
            waitForObject(names.apollo_edName_QLineEdit),
            116, 31,
            Qt.NoModifier,
            Qt.LeftButton
        )
        enter_preset_name(preset_name)
        if configure_callback is not None:
            configure_callback()
        clickButton(
            waitForObject(names.apollo_btSave_QPushButton)
        )
        if object.exists(names.warning_OK_QPushButton):
            test.log(
                "PRESET ALREADY EXISTS: {}".format(preset_name)
            )
            clickButton(
                waitForObject(names.warning_OK_QPushButton)
            )
            clickButton(
                waitForObject(names.apollo_btCancel_QPushButton)
            )
            test.log(
                "Duplicate preset creation cancelled: {}".format(
                    preset_name
                )
            )
            return False
        updated_presets = get_preset_names()
        if preset_exists(preset_name):
            test.passes(
                "PASS: Preset created successfully - {}".format(
                    preset_name
                )
            )
            return True
        test.log(
            "WARNING: Preset not found in table inventory: {}".format(
                preset_name
            )
        )
        test.log(
            "Check diagnostic table logs for actual preset values."
        )
        return False
    except Exception as error:
        test.fail(
            "FAIL: Preset creation failed - {}".format(error)
        )
        raise

def enter_preset_name(preset_name):
    """
    WHEN user need to enter a preset name,
    THEN click the required letters on the on-screen keyboard,
    AND press Enter after entering the complete name.
    """
    try:
        for char in preset_name.lower():
            if not char.isalpha():
                raise ValueError(
                    "Only alphabetic preset names are supported."
                )
            key_object = getattr(
                names,
                "keyboardFrame_{}_KeyButtonLetter".format(char)
            )

            clickButton(waitForObject(key_object))
        clickButton(
            waitForObject(names.keyboardFrame_Enter_KeyButtonEnter)
        )
    except Exception as error:
        test.fail(
            "FAIL: Unable to enter preset name - {}".format(error)
        )
        raise

def get_preset_names():
    """
    WHEN the preset screen is open,
    THEN read all preset names from the preset table,
    AND return the list of preset names.
    """

    try:
        table = waitForObject(names.apollo_tvPresets_PresetsTable)

        test.log("PRESET TABLE DETAILS")
        test.log("TABLE OBJECT: {}".format(table))

        model = table.model()

        row_count = model.rowCount()
        column_count = model.columnCount()

        test.log("MODEL ROW COUNT: {}".format(row_count))
        test.log("MODEL COLUMN COUNT: {}".format(column_count))
        preset_names = []
        for row in range(row_count):
            for column in range(column_count):
                index = model.index(row, column)
                value = model.data(index, Qt.DisplayRole)
                test.log(
                    "ROW: {}, COLUMN: {}, VALUE: {}".format(
                        row, column, value
                    )
                )
                if value is not None:
                    value = str(value).strip()
                    if value and value not in preset_names:
                        preset_names.append(value)

        test.log("EXISTING PRESETS: {}".format(preset_names))
        return preset_names
    except Exception as error:
        test.fail(
            "FAIL: Unable to read preset names - {}".format(error)
        )
        raise

def preset_exists(preset_name):
    """
    WHEN user need to check whether a preset exists,
    THEN search for the given preset name in the preset list,
    AND return True if it exists or False if it does not.
    """
    try:
        existing_presets = get_preset_names()
        if preset_name.lower() in [
            name.lower() for name in existing_presets
        ]:
            return True
        return False
    except Exception as error:

        test.fail(
            "FAIL: Preset existence check failed - {}".format(error)
        )
        raise
    
def validate_preset_name(preset_name):
    """
    Validate a preset name against the 12-character limit.
    """
    if not preset_name:
        raise ValueError("Preset name cannot be empty.")

    if len(preset_name) > 12:
        test.log(
            "REJECTED: Preset name exceeds 12 characters - {}".format(
                preset_name
            )
        )
        return False

    return True


def validate_existing_preset_names():
    """
    Check existing preset names and reject names longer than 12 characters..
    """
    try:
        existing_presets = get_preset_names()

        valid_presets = []
        invalid_presets = []

        for preset_name in existing_presets:
            if len(preset_name) > 12:
                invalid_presets.append(preset_name)
            else:
                valid_presets.append(preset_name)

        test.log(
            "VALID PRESETS: {}".format(valid_presets)
        )

        test.log(
            "PRESETS EXCEEDING 12 CHARACTERS: {}".format(
                invalid_presets
            )
        )

        if invalid_presets:
            test.log(
                "WARNING: Existing presets exceeding 12 characters "
                "will not be selected."
            )

        return valid_presets

    except Exception as error:
        test.fail(
            "FAIL: Existing preset name validation - {}".format(error)
        )
        raise


def verify_preset_name_maximum_length():
    """
    Given: The Add Preset dialog is available.
    When: Twelve characters and three additional characters are entered.
    Then: The preset name field must not accept more than twelve characters.
    """
    validation_passed = False

    try:
        clickButton(
            waitForObject(
                names.frToolbar_tbAddPreset_QToolButton
            )
        )

        mouseClick(
            waitForObject(names.apollo_edName_QLineEdit),
            65,
            27,
            Qt.NoModifier,
            Qt.LeftButton
        )
        for char in "abcdefghijkl":
            key_object = getattr(
                names,
                "keyboardFrame_{}_KeyButtonLetter".format(char)
            )
            clickButton(waitForObject(key_object))
        for _ in range(3):
            clickButton(
                waitForObject(
                    names.keyboardFrame_l_KeyButtonLetter
                )
            )
        name_field = waitForObject(
            names.apollo_edName_QLineEdit
        )
        actual_name = str(name_field.text)

        if len(actual_name) <= 12:
            test.passes(
                "PASS: Maximum preset name length is 12 characters. "
                "Actual length: {}".format(len(actual_name))
            )
            validation_passed = True
        else:
            raise AssertionError(
                "Preset name accepted {} characters; maximum allowed is 12."
                .format(len(actual_name))
            )

    except Exception as error:
        test.fail(
            "FAIL: Maximum preset name length validation - {}".format(
                error
            )
        )

    finally:
        try:
            clickButton(
                waitForObject(
                    names.keyboardFrame_Cancel_KeyButtonCancel
                )
            )
        except Exception:
            pass

        try:
            mouseClick(
                waitForObject(names.apollo_wdNavigationBar_QWidget),
                58,
                661,
                Qt.NoModifier,
                Qt.LeftButton
            )
            clickButton(
                waitForObject(names.apollo_btCancel_QPushButton)
            )
        except Exception as cleanup_error:
            test.log(
                "Cleanup information: {}".format(cleanup_error)
            )

    if not validation_passed:
        raise AssertionError(
            "Maximum preset name length validation failed."
        )

    return True

def select_four_recorded_presets():
    """
    Scroll the Presets table and select the four requested presets.
    """
    scroll_object(
        names.apollo_tvPresets_PresetsTable,
        534, 376, -120, 7
    )

    valid_presets = validate_existing_preset_names()

    presets = [
        ("soft", 65, 39),
        ("tissues", 79, 22),
        ("softy", 82, 18),
        ("softtissues", 241, 42)
    ]

    for preset_name, x, y in presets:
        if preset_name not in valid_presets:
            test.log(
                "SKIPPING PRESET: {}".format(preset_name)
            )
            continue

        select_preset_twice(preset_name, x, y)

        test.log(
            "Selected preset: {}".format(preset_name)
        )


def configure_recorded_profile_dropdowns():
    """
    Execute the recorded dropdown scrolling and selection actions.
    """
    mouseClick(
        waitForObject(names.centralWidget_comboBox_ComboBox),
        282, 37,
        Qt.NoModifier,
        Qt.LeftButton
    )

    scroll_object(
        names.apollo_aivComboBoxPopup_QTreeView,
        263, 126, -120, 1
    )

    scroll_object(
        names.apollo_aivComboBoxPopup_QTreeView,
        263, 128, -120, 1
    )

    scroll_object(
        names.apollo_aivComboBoxPopup_QTreeView,
        263, 130, -120, 1
    )

    scroll_object(
        names.apollo_aivComboBoxPopup_QTreeView,
        264, 131, -120, 3
    )

    mouseClick(
        waitForObject(names.apollo_frmComboBoxShadow_QFrame),
        869, 135,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.comboBox_lbValue_AutoReducibleFontSizeLabel_2
        ),
        145, 35,
        Qt.NoModifier,
        Qt.LeftButton
    )

    scroll_object(
        names.apollo_aivComboBoxPopup_QTreeView,
        166, 217, -120, 1
    )

    scroll_object(
        names.apollo_aivComboBoxPopup_QTreeView,
        165, 218, -120, 1
    )

    scroll_object(
        names.apollo_aivComboBoxPopup_QTreeView,
        164, 219, -120, 4
    )

    mouseClick(
        waitForObject(names.apollo_frmComboBoxShadow_QFrame),
        36, 236,
        Qt.NoModifier,
        Qt.LeftButton
    )


def create_recorded_cw_preset():
    """
    Create the recorded CW-mode preset and perform its name update.
    """
    clickButton(
        waitForObject(names.apollo_btPresets_QPushButton)
    )

    clickButton(
        waitForObject(names.frToolbar_tbAddPreset_QToolButton)
    )

    clickButton(
        waitForObject(names.apollo_btCwMode_QToolButton)
    )

    mouseClick(
        waitForObject(names.apollo_edName_QLineEdit),
        194, 22,
        Qt.NoModifier,
        Qt.LeftButton
    )

    enter_preset_name("soft")

    clickButton(
        waitForObject(names.pagesWidget_pbEnlarge_QPushButton_2)
    )

    clickButton(
        waitForObject(names.apollo_btSave_QPushButton)
    )

    clickButton(
        waitForObject(names.warning_OK_QPushButton)
    )

    mouseClick(
        waitForObject(names.apollo_edName_QLineEdit),
        102, 24,
        Qt.NoModifier,
        Qt.LeftButton
    )

    doubleClick(
        waitForObject(names.keyboardFrame_i_KeyButtonLetter),
        42, 56,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(names.keyboardFrame_o_KeyButtonLetter)
    )

    clickButton(
        waitForObject(names.keyboardFrame_Enter_KeyButtonEnter)
    )

    clickButton(
        waitForObject(names.pagesWidget_pbEnlarge_QPushButton_2)
    )

    clickButton(
        waitForObject(names.apollo_btSave_QPushButton)
    )


def select_recorded_cw_table_entry():
    """
    Scroll the Presets table and select the recorded '-_2' entry twice.
    """
    scroll_object(
        names.apollo_tvPresets_PresetsTable,
        458, 495, -120, 1
    )

    scroll_object(
        names.apollo_tvPresets_PresetsTable,
        456, 497, -120, 4
    )

    select_preset_twice("-_2", 19, 21)


def cancel_additional_preset():
    """
    Execute the recorded additional preset cancellation sequence.

    Enter the first 12 letters, attempt three extra letters,
    close the keyboard, and cancel the preset.
    """
    verify_preset_name_maximum_length()


def complete_latest_recorded_preset_flow():
    """
    Execute the complete latest recorded preset workflow.
    """
    try:
        test.log("STEP: Selecting recorded presets")
        select_four_recorded_presets()

        test.log("STEP: Returning to Home")
        clickButton(
            waitForObject(names.apollo_btHome_QPushButton)
        )

        test.log("STEP: Configuring profile dropdowns")
        configure_recorded_profile_dropdowns()

        test.log("STEP: Creating CW-mode preset")
        create_recorded_cw_preset()

        test.log("STEP: Selecting recorded CW table entry")
        select_recorded_cw_table_entry()

        test.log("STEP: Testing maximum preset name length")
        cancel_additional_preset()

        test.log("STEP: Exiting profile")
        clickButton(
            waitForObject(names.apollo_btExitProfile_QPushButton)
        )

        clickButton(
            waitForObject(names.question_YES_QPushButton)
        )

        test.passes(
            "PASS: Latest recorded preset workflow completed"
        )

    except Exception as error:
        test.fail(
            "FAIL: Latest recorded preset workflow - {}".format(error)
        )
        raise




def scroll_object(object_name, x, y, direction, count):
    """
    Given: A mapped UI object and scroll coordinates.
    When: The specified number of scroll events are performed.
    Then: The object is scrolled in the requested direction.
    """
    try:
        obj = waitForObject(object_name)

        for _ in range(count):
            sendEvent(
                "QWheelEvent",
                obj,
                x,
                y,
                direction,
                0,
                2
            )

        return True

    except Exception as error:
        test.fail(
            "FAIL: Unable to scroll object - {}".format(error)
        )
        raise



def select_preset_twice(preset_name, x, y):
    """
    Given: A preset name and its table coordinates.
    When: The preset is selected twice in the Presets table.
    Then: The specified preset is selected successfully.
    """
    try:
        preset_item = waitForObjectItem(
            names.apollo_tvPresets_PresetsTable,
            preset_name
        )

        for _ in range(2):
            mouseClick(
                preset_item,
                x,
                y,
                Qt.NoModifier,
                Qt.LeftButton
            )

        test.passes(
            "PASS: Preset selected - {}".format(preset_name)
        )
        return True

    except Exception as error:
        test.fail(
            "FAIL: Unable to select preset '{}': {}".format(
                preset_name,
                error
            )
        )
        raise


def main():
    test.log("This TC contain TU-150 to TU-164")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_presets()
    create_preset("soft")
    create_preset("tissues")
    create_preset("softy")
    create_preset("softtissues")
    complete_latest_recorded_preset_flow()