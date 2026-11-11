from common import *
from squish import *
import test
import names

EXPECTED_HEADERS = [
    "Preset Name",
    "Energy",
    "Frequency",
    "Power",
    "Pulse Width"
]

EXPECTED_PULSE_WIDTH_VALUES = [
    "Short",
    "Medium",
    "Long",
    "StepPulse"
]

EXPECTED_PRESET_NAMES = [
    "Kidney Dust (High)",
    "Kidney Dust (Low)",
    "Kidney Popcorn",
    "Kidney Fragment (High)",
    "Kidney Fragment (Low)",
    "Ureter (Fragment)",
    "Ureter Dust",
    "Bladder Fragment",
    "COAG",
    "Prostate Enucleate (High)",
    "Prostate Enucleate (Low)"
]


def normalize_string(value):
    """
    Convert a retrieved UI value into a stripped string.
    """
    if value is None:
        return ""
    return str(value).strip()

def click_and_report(object_name, description):
    """
    Wait for a mapped object, click it, and report the result.
    """
    try:
        clickButton(waitForObject(object_name, 20000))
        test.passes("PASS: " + description)
        return True
    except Exception as error:
        test.fail(
            "FAIL: {} - {}".format(description, error)
        )
        return False

def mouse_click_and_report(object_name, x, y, description):
    """
    Click a mapped object at the supplied coordinates.
    """
    try:
        obj = waitForObject(object_name, 20000)
        mouseClick(
            obj,
            x,
            y,
            Qt.NoModifier,
            Qt.LeftButton
        )

        test.passes("PASS: " + description)
        return True
    except Exception as error:
        test.fail(
            "FAIL: {} - {}".format(description, error)
        )
        return False

def navigate_to_treatment_and_presets():
    """
    Navigating to TreatmentScreen
    """
    try:
        mouseClick(
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            565,
            25,
            Qt.NoModifier,
            Qt.LeftButton
        )

        clickButton(waitForObject(names.apollo_btHome_QPushButton))

        mouseClick(
            waitForObject(
                names.comboBox_lbValue_AutoReducibleFontSizeLabel
            ),
            125,
            20,
            Qt.NoModifier,
            Qt.LeftButton
        )

        mouseClick(
            waitForObject(
                names.frmComboBoxHeader_lbValue_AutoReducibleFontSizeLabel
            ),
            232,
            45,
            Qt.NoModifier,
            Qt.LeftButton
        )
        mouseClick(
            waitForObject(names.centralWidget_standby_QWidget),
            597,
            13,
            Qt.NoModifier,
            Qt.LeftButton
        )
        clickButton(waitForObject(names.apollo_btPresets_QPushButton))
        waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )
        test.passes("PASS: Navigated to Presets screen using recorded flow")
        snooze(2)
        return True
    except Exception as error:
        test.fail("FAIL: Treatment/Home/Presets navigation failed - {}".format(error))
        return False
def verify_preset_headers():
    """
    Verify the displayed preset table headers using the Qt model.
    """
    result = True
    try:
        table = waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )
        model = table.model()
        for column, expected_header in enumerate(EXPECTED_HEADERS):
            actual_header = normalize_string(
                model.headerData(
                    column,
                    Qt.Horizontal,
                    Qt.DisplayRole
                )
            )
            if actual_header.lower() == expected_header.lower():
                test.passes(
                    "PASS: Header '{}' verified".format(actual_header)
                )
            else:
                test.fail(
                    "FAIL: Header mismatch. Expected '{}', actual '{}'".format(
                        expected_header,
                        actual_header
                    )
                )
                result = False

        return result

    except Exception as error:
        test.fail(
            "FAIL: Header verification error - {}".format(error)
        )
        return False


def find_column_index(model, expected_header):
    """
    Find a table column by its header text.
    """
    try:
        expected = expected_header.lower().replace("_", " ")
        for column in range(model.columnCount()):
            header = normalize_string(
                model.headerData(
                    column,
                    Qt.Horizontal,
                    Qt.DisplayRole
                )
            )
            if header.lower().replace("_", " ") == expected:
                return column
        return -1
    except Exception as error:
        test.log(
            "Column lookup error for '{}': {}".format(
                expected_header,
                error
            )
        )
        return -1

def read_table_cell(model, row, column):
    """
    Read a table cell using Qt DisplayRole, EditRole and ToolTipRole.
    """
    try:
        index = model.index(row, column)
        for role in [
            Qt.DisplayRole,
            Qt.EditRole,
            Qt.ToolTipRole
        ]:
            value = normalize_string(
                model.data(index, role)
            )

            if value:
                return value

        return ""

    except Exception as error:
        test.log(
            "Cell read failed at row {}, column {}: {}".format(
                row,
                column,
                error
            )
        )
        return ""


def verify_preset_names():
    """
    Verify expected preset names in the first table column.
    """
    result = True

    try:
        table = waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )

        model = table.model()
        actual_names = []

        for row in range(model.rowCount()):

            name = read_table_cell(model, row, 0)

            if name:
                actual_names.append(name)

        test.log(
            "Total presets displayed: {}".format(len(actual_names))
        )

        test.log(
            "Preset names: {}".format(actual_names)
        )

        for expected_name in EXPECTED_PRESET_NAMES:

            if expected_name in actual_names:
                test.passes(
                    "PASS: Preset '{}' found".format(expected_name)
                )
            else:
                test.fail(
                    "FAIL: Preset '{}' not found".format(expected_name)
                )
                result = False

        return result

    except Exception as error:
        test.fail(
            "FAIL: Preset name verification error - {}".format(error)
        )
        return False


def verify_pulse_width_indicator(actual_value, preset_name):
    """
    Verify that Pulse Width is Short, Medium, Long or StepPulse.
    """
    actual = normalize_string(actual_value)

    if actual in EXPECTED_PULSE_WIDTH_VALUES:
        test.passes(
            "PASS: Pulse Width for '{}' is '{}'".format(
                preset_name,
                actual
            )
        )
        return True

    test.fail(
        "FAIL: Pulse Width for '{}' expected one of {} "
        "but actual displayed value was '{}'".format(
            preset_name,
            EXPECTED_PULSE_WIDTH_VALUES,
            actual
        )
    )

    return False


def verify_all_pulse_width_values():
    """
    Verify Pulse Width values for all rows in the preset table.
    """
    result = True

    try:
        table = waitForObject(
            names.apollo_tvPresets_PresetsTable,
            20000
        )

        model = table.model()

        pulse_column = find_column_index(
            model,
            "Pulse Width"
        )

        if pulse_column == -1:
            test.fail(
                "FAIL: Pulse Width column not found"
            )
            return False

        for row in range(model.rowCount()):

            preset_name = read_table_cell(model, row, 0)

            if not preset_name:
                continue

            actual_value = read_table_cell(
                model,
                row,
                pulse_column
            )

            test.log(
                "Preset '{}': Pulse Width raw value = '{}'".format(
                    preset_name,
                    actual_value
                )
            )

            if not verify_pulse_width_indicator(
                actual_value,
                preset_name
            ):
                result = False

        return result

    except Exception as error:
        test.fail(
            "FAIL: Pulse Width verification error - {}".format(error)
        )
        return False


def perform_recorded_preset_interactions():
    """
    Perform the exact recorded preset header and row interactions.
    """
    try:
        # Preset Name header
        for unused in range(2):
            mouseClick(
                waitForObject(names.pRESET_NAME_HeaderViewItem),
                94, 14, Qt.NoModifier, Qt.LeftButton
            )

        # Energy header
        mouseClick(
            waitForObject(names.eNERGY_HeaderViewItem),
            99, 17, Qt.NoModifier, Qt.LeftButton
        )

        # Frequency header
        for unused in range(2):
            mouseClick(
                waitForObject(names.fREQUENCY_HeaderViewItem),
                105, 14, Qt.NoModifier, Qt.LeftButton
            )

        # Power header
        for unused in range(2):
            mouseClick(
                waitForObject(names.pOWER_HeaderViewItem),
                38, 13, Qt.NoModifier, Qt.LeftButton
            )

        # Pulse Width header
        for unused in range(2):
            mouseClick(
                waitForObject(names.pULSE_WIDTH_HeaderViewItem),
                115, 18, Qt.NoModifier, Qt.LeftButton
            )

        # First group of preset rows
        preset_clicks = [
            ("Kidney Dust (High)", 35, 31),
            ("Kidney Dust (Low)", 251, 23),
            ("Kidney Popcorn", 299, 19),
            ("Kidney Fragment (High)", 302, 21),
            ("Kidney Fragment (Low)", 302, 16),
            ("Ureter (Fragment)", 322, 16),
            ("Ureter Dust", 317, 16),
            ("Bladder Fragment", 333, 20),
            ("COAG", 334, 27),
            ("Prostate Enucleate (High)", 348, 33),
            ("Prostate Enucleate (Low)", 352, 22)
        ]

        for preset_name, x, y in preset_clicks:

            for unused in range(2):
                mouseClick(
                    waitForObjectItem(
                        names.apollo_tvPresets_PresetsTable,
                        preset_name
                    ),
                    x,
                    y,
                    Qt.NoModifier,
                    Qt.LeftButton
                )

        # Scroll to lower preset rows
        scrollTo(
            waitForObject(names.tvPresets_QScrollBar),
            217
        )

        lower_preset_clicks = [
            (r"1\.5_2", 14, 21),
            (r"1\.5_1", 15, 16),
            ("2_2", 16, 39),
            (r"-\_1", 17, 26),
            ("1_4", 14, 18)
        ]

        for preset_name, x, y in lower_preset_clicks:

            for unused in range(2):
                mouseClick(
                    waitForObjectItem(
                        names.apollo_tvPresets_PresetsTable,
                        preset_name
                    ),
                    x,
                    y,
                    Qt.NoModifier,
                    Qt.LeftButton
                )

        test.passes(
            "PASS: All recorded preset interactions completed"
        )

        return True

    except Exception as error:
        test.fail(
            "FAIL: Recorded preset interaction failed - {}".format(
                error
            )
        )
        return False


def exit_preset_screen():
    """
    Exit the Presets screen using the recorded confirmation sequence.
    """
    try:
        clickButton(
            waitForObject(
                names.apollo_btExitProfile_QPushButton,
                20000
            )
        )

        clickButton(
            waitForObject(
                names.question_YES_QPushButton,
                20000
            )
        )

        test.passes(
            "PASS: Exited Presets screen successfully"
        )

        return True

    except Exception as error:
        test.fail(
            "FAIL: Unable to exit Presets screen - {}".format(error)
        )
        return False


def main():
    test.log("This TC contains the tags from TU-107 to TU-111")
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
        enterpin()
        open_default_profile_presets()
      
        if not navigate_to_treatment_and_presets():
            raise Exception(
                "Treatment and Presets navigation failed"
            )
        if not perform_recorded_preset_interactions():
            raise Exception(
                "Recorded preset interactions failed"
            )
        snooze(2)
        headers_result = verify_preset_headers()
        names_result = verify_preset_names()
        pulse_result = verify_all_pulse_width_values()
        if headers_result and names_result and pulse_result:
            test.passes(
                "PASS: Preset table verification completed successfully"
            )
        else:
            test.fail(
                "FAIL: Preset table verification completed with failures"
            )

        if not exit_preset_screen():
            raise Exception(
                "Preset screen exit failed"
            )

    except Exception as error:
        test.fail(
            "FAIL: Preset test execution failed - {}".format(error)
        )
        raise
