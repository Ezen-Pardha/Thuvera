from common import *
import names
import test


PRESET_NAMES_TO_CREATE = [
    "soft",
    "tissues",
    "softy",
    "softtissues"
]


def create_preset(preset_name, configure_callback=None):
    """Create a new user-defined preset."""

    try:
        test.log(
            "REQUESTED USER PRESET CREATION: {}".format(preset_name)
        )

        if not validate_preset_name(preset_name):
            test.fail(
                "FAIL: Invalid preset name - {}".format(preset_name)
            )
            return False

        clickButton(
            waitForObject(
                names.frToolbar_tbAddPreset_QToolButton,
                20000
            )
        )

        mouseClick(
            waitForObject(names.apollo_edName_QLineEdit, 20000),
            116, 31,
            Qt.NoModifier,
            Qt.LeftButton
        )
        enter_preset_name(preset_name)
        if configure_callback is not None:
            configure_callback()
        clickButton(
            waitForObject(names.apollo_btSave_QPushButton, 20000)
        )

        if object.exists(names.warning_OK_QPushButton):
            test.log(
                "PRESET ALREADY EXISTS: {}".format(preset_name)
            )

            clickButton(
                waitForObject(names.warning_OK_QPushButton, 20000)
            )

            if object.exists(names.apollo_btCancel_QPushButton):
                clickButton(
                    waitForObject(names.apollo_btCancel_QPushButton, 20000)
                )

            test.log(
                "DUPLICATE PRESET CREATION CANCELLED: {}".format(
                    preset_name
                )
            )
            return False

        snooze(1)

        if preset_exists(preset_name):
            test.passes(
                "PASS: User-defined preset created successfully - {}".format(
                    preset_name
                )
            )
            return True

        test.fail(
            "FAIL: Newly created preset not found - {}".format(
                preset_name
            )
        )
        return False

    except Exception as error:
        test.fail(
            "FAIL: Preset creation failed for {} - {}".format(
                preset_name, error
            )
        )
        raise


def enter_preset_name(preset_name):
    """Enter a preset name using the application's on-screen keyboard."""

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

            clickButton(waitForObject(key_object, 20000))
        clickButton(
            waitForObject(
                names.keyboardFrame_Enter_KeyButtonEnter,
                20000
            )
        )

        test.log(
            "PRESET NAME ENTERED: {}".format(preset_name)
        )

    except Exception as error:
        test.fail(
            "FAIL: Unable to enter preset name - {}".format(error)
        )
        raise


def get_preset_names():
    """Read all displayed preset names from the current preset table."""

    try:
        table = waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )

        model = table.model()
        row_count = model.rowCount()
        column_count = model.columnCount()
        test.log("PRESET TABLE DETAILS")
        test.log("TABLE OBJECT: {}".format(table))
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

                if value is None:
                    continue

                value = str(value).strip()

                if value and value not in preset_names:
                    preset_names.append(value)

        test.log(
            "EXISTING PRESETS: {}".format(preset_names)
        )
        return preset_names

    except Exception as error:
        test.fail(
            "FAIL: Unable to read preset names - {}".format(error)
        )
        raise


def find_preset_row(preset_name):
    """Find an exact, case-insensitive preset name in the table."""

    try:
        table = waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )
        model = table.model()

        test.log(
            "SEARCHING TABLE FOR PRESET: {}".format(preset_name)
        )

        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                index = model.index(row, column)
                value = model.data(index, Qt.DisplayRole)

                if value is None:
                    continue

                value = str(value).strip()

                test.log(
                    "SEARCH CELL - ROW: {}, COLUMN: {}, VALUE: {}".format(
                        row, column, value
                    )
                )

                if value.lower() == preset_name.strip().lower():
                    test.log(
                        "PRESET FOUND AT ROW: {}, COLUMN: {}".format(
                            row, column
                        )
                    )
                    return row, column
        test.log(
            "PRESET NOT FOUND IN TABLE: {}".format(preset_name)
        )
        return None

    except Exception as error:
        test.fail(
            "FAIL: Unable to find preset row for {} - {}".format(
                preset_name, error
            )
        )
        raise


def preset_exists(preset_name):
    """Check whether the requested preset exists in the current table."""

    try:
        return find_preset_row(preset_name) is not None

    except Exception as error:
        test.fail(
            "FAIL: Preset existence check failed - {}".format(error)
        )
        raise


def validate_preset_name(preset_name):
    """Validate a preset name against the 12-character maximum."""

    if preset_name is None:
        test.log("REJECTED: Preset name cannot be empty")
        return False

    preset_name = str(preset_name).strip()

    if not preset_name:
        test.log("REJECTED: Preset name cannot be empty")
        return False

    if len(preset_name) > 12:
        test.log(
            "REJECTED: Preset name exceeds 12 characters - {}".format(
                preset_name
            )
        )
        return False

    test.log(
        "PASS: Preset name is valid - {} ({} characters)".format(
            preset_name, len(preset_name)
        )
    )
    return True


def validate_existing_preset_names():
    """Check existing preset names against the 12-character limit."""

    try:
        existing_presets = get_preset_names()

        valid_presets = []
        invalid_presets = []

        for preset_name in existing_presets:
            if len(preset_name) > 12:
                invalid_presets.append(preset_name)
            else:
                valid_presets.append(preset_name)

        test.log("VALID PRESETS: {}".format(valid_presets))
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
            "FAIL: Existing preset name validation failed - {}".format(
                error
            )
        )
        raise


def get_preset_logo(preset_name):
    """
    Retrieve the logo associated with a preset using Qt.DecorationRole.
    """

    try:
        test.log(
            "GETTING LOGO FOR PRESET: {}".format(preset_name)
        )

        preset_location = find_preset_row(preset_name)

        if preset_location is None:
            test.fail(
                "FAIL: Preset row not found while retrieving logo - {}".format(
                    preset_name
                )
            )
            return None

        row, matching_column = preset_location

        table = waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )
        model = table.model()

        test.log(
            "LOGO SEARCH ROW: {}, MATCHING COLUMN: {}".format(
                row, matching_column
            )
        )

        for column in range(model.columnCount()):
            index = model.index(row, column)
            icon = model.data(index, Qt.DecorationRole)

            test.log(
                "LOGO CHECK - ROW: {}, COLUMN: {}, VALUE: {}".format(
                    row, column, icon
                )
            )

            if icon is None:
                continue

            if hasattr(icon, "isNull"):
                if icon.isNull():
                    test.log(
                        "EMPTY ICON AT ROW {}, COLUMN {}".format(
                            row, column
                        )
                    )
                    continue

                test.log(
                    "NON-EMPTY LOGO RETRIEVED - ROW: {}, COLUMN: {}".format(
                        row, column
                    )
                )
                test.passes(
                    "PASS: Logo retrieved for preset - {}".format(
                        preset_name
                    )
                )
                return icon

            test.log(
                "DECORATION ROLE OBJECT TYPE: {}".format(type(icon))
            )
            test.passes(
                "PASS: Decoration data retrieved for preset - {}".format(
                    preset_name
                )
            )
            return icon

        test.log(
            "NO NON-EMPTY DECORATION ROLE FOUND FOR: {}".format(
                preset_name
            )
        )
        return None

    except Exception as error:
        test.fail(
            "FAIL: Unable to retrieve logo for {} - {}".format(
                preset_name, error
            )
        )
        raise


def verify_user_created_preset_logo(preset_name):
    """Retrieve and verify the logo associated with a preset."""

    try:
        test.log(
            "VERIFYING PRESET LOGO: {}".format(preset_name)
        )

        icon = get_preset_logo(preset_name)

        if icon is None:
            test.fail(
                "FAIL: No logo retrieved for preset - {}".format(
                    preset_name
                )
            )
            return False

        if hasattr(icon, "isNull") and icon.isNull():
            test.fail(
                "FAIL: Retrieved logo is empty - {}".format(
                    preset_name
                )
            )
            return False

        test.passes(
            "PASS: Preset logo retrieved successfully - {}".format(
                preset_name
            )
        )
        return True

    except Exception as error:
        test.fail(
            "FAIL: Logo verification failed for {} - {}".format(
                preset_name, error
            )
        )
        raise


def select_created_presets_and_report_details():
    """Select and verify all four user-defined presets."""

    try:
        preset_table = waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )
        presets = [
            ("soft", 16, 26),
            ("tissues", 57, 29),
            ("softy", 54, 19),
            ("softtissues", 57, 27)
        ]

        all_presets_verified = True

        for preset_name, x, y in presets:
            test.log(
                "SELECTING USER-DEFINED PRESET: {}".format(
                    preset_name
                )
            )

            mouseClick(
                preset_table,
                x, y,
                Qt.NoModifier,
                Qt.LeftButton
            )

            mouseClick(
                preset_table,
                x, y,
                Qt.NoModifier,
                Qt.LeftButton
            )

            snooze(1)

            preset_location = find_preset_row(preset_name)

            if preset_location is None:
                all_presets_verified = False
                test.fail(
                    "FAIL: Preset not found in table - {}".format(
                        preset_name
                    )
                )
                continue

            row, column = preset_location

            table = waitForObject(
                names.apollo_tvPresets_PresetsTable,
                20000
            )
            model = table.model()
            index = model.index(row, column)

            preset_text = model.data(index, Qt.DisplayRole)

            test.log(
                "PRESET TEXT: {}".format(preset_text)
            )
            test.passes(
                "PASS: Preset name verified - {}".format(
                    preset_name
                )
            )

            logo_verified = verify_user_created_preset_logo(
                preset_name
            )

            if not logo_verified:
                all_presets_verified = False

        preset_table.clearSelection()
        test.log("SELECTED CELL CLEARED FROM PRESET TABLE")

        if all_presets_verified:
            test.passes(
                "PASS: All four user-defined preset names "
                "and logos verified successfully"
            )
        else:
            test.fail(
                "FAIL: One or more preset names or logos "
                "could not be verified"
            )

        return all_presets_verified

    except Exception as error:
        test.fail(
            "FAIL: Preset selection and logo verification failed - {}".format(
                error
            )
        )
        raise


def main():
    """Execute the user-defined preset creation and verification test."""

    try:
        test.log("This TC Contains TU-131 to TU-273")

        clickButton(
            waitForObject(
                names.frmPopup_pbAccept_QPushButton,
                20000
            )
        )

        enterpin()
        open_default_profile_presets()

        test.log("CHECKING EXISTING USER-DEFINED PRESETS")

        existing_presets = get_preset_names()
        existing_preset_names_lower = [
            preset.strip().lower()
            for preset in existing_presets
        ]

        existing_user_presets = [
            preset_name
            for preset_name in PRESET_NAMES_TO_CREATE
            if preset_name.lower() in existing_preset_names_lower
        ]
        if existing_user_presets:
            test.fail(
                "FAIL: User-defined presets are available, but "
                "Edit and Delete buttons are not disabled. "
                "Presets found: {}".format(existing_user_presets)
            )
            return

        test.log(
            "NO USER-DEFINED PRESETS FOUND. "
            "CONTINUING WITH THE ORIGINAL TEST."
        )

        test.log(
            "PRESETS TO CREATE: {}".format(PRESET_NAMES_TO_CREATE)
        )

        created_presets = []

        for preset_name in PRESET_NAMES_TO_CREATE:
            if create_preset(preset_name):
                created_presets.append(preset_name)
            else:
                test.log(
                    "PRESET CREATION FAILED: {}".format(preset_name)
                )

        if len(created_presets) != len(PRESET_NAMES_TO_CREATE):
            test.fail(
                "FAIL: Not all user-defined presets were created. "
                "Created: {}".format(created_presets)
            )
            return

        test.log("VERIFYING CREATED PRESETS AND LOGOS")
        select_created_presets_and_report_details()

        sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 629, 407, -120, 0, 2)
        sendEvent("QWheelEvent", waitForObject(names.apollo_tvPresets_PresetsTable), 632, 407, -120, 0, 2)
        clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
        mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "soft"), 260, 22, Qt.NoModifier, Qt.LeftButton)
        clickButton(waitForObject(names.question_OK_QPushButton))
        clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
        mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "tissues"), 304, 27, Qt.NoModifier, Qt.LeftButton)
        clickButton(waitForObject(names.question_OK_QPushButton))
        clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
        mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "softy"), 329, 12, Qt.NoModifier, Qt.LeftButton)
        clickButton(waitForObject(names.question_OK_QPushButton))
        clickButton(waitForObject(names.frToolbar_tbDeletePreset_QToolButton))
        mouseClick(waitForObjectItem(names.apollo_tvPresets_PresetsTable, "softtissues"), 331, 22, Qt.NoModifier, Qt.LeftButton)
        clickButton(waitForObject(names.question_OK_QPushButton))
    except Exception as error:
        test.fail(
            "FAIL: Main test execution failed - {}".format(error)
        )
        raise
