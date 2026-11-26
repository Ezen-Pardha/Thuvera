import openpyxl
import re
import os
import names
import unicodedata

from squish import *

SUITE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)



EXCEL_PATH = os.path.abspath(
    os.path.join(
        SUITE_DIR, "..", "testdata", "Thuvera_Strings.xlsx"
    )
)


LANGUAGE = "Croatian"



def normalize(text):

    if text is None:
        return ""

    text = str(text)
    text = re.sub(
        r"<br\s*/?>",
        " ",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )
    text = " ".join(text.split())

    return text.casefold().strip()


def get_text_lines(obj):

    lines = []

    try:

        if not obj.visible:
            return lines

    except:

        pass


    try:

        text = str(obj.text).strip()

        if text:

            text = re.sub(
                r"<br\s*/?>",
                "\n",
                text,
                flags=re.IGNORECASE
            )

            text = re.sub(
                r"<[^>]+>",
                "",
                text
            )

            for line in text.splitlines():

                line = " ".join(
                    line.split()
                ).strip()

                if line:
                    lines.append(line)

    except:

        pass


    try:

        title = str(obj.title).strip()

        if title:

            title = re.sub(
                r"<[^>]+>",
                "",
                title
            )

            title = " ".join(
                title.split()
            ).strip()

            if title:
                lines.append(title)

    except:

        pass



    try:

        for child in object.children(obj):

            lines.extend(
                get_text_lines(child)
            )

    except:

        pass


    return lines


def get_all_text_combinations(obj):

    result = []

    lines = get_text_lines(obj)

    for start in range(len(lines)):

        combined = ""

        for end in range(start, len(lines)):

            if combined:

                combined += " " + lines[end]

            else:

                combined = lines[end]

            result.append(combined)


    return list(set(result))



def load_localized_strings(
        language=LANGUAGE,
        excel_path=EXCEL_PATH):



    workbook = openpyxl.load_workbook(
        excel_path,
        data_only=True
    )


    sheet = workbook.active

    print(
        "Localization Excel Sheet Used: "
        + sheet.title
    )

    headers = []

    for cell in sheet[1]:

        if cell.value is None:

            headers.append("")

        else:

            headers.append(
                str(cell.value).strip()
            )


    try:

        english_column = headers.index(
            "English"
        )

    except ValueError:

        workbook.close()

        raise Exception(
            "English column not found in active sheet: "
            + sheet.title
        )


    try:

        language_column = headers.index(
            language
        )

    except ValueError:

        workbook.close()

        raise Exception(
            "Language '"
            + language
            + "' not found in active sheet: "
            + sheet.title
        )


    strings = []


    for row in sheet.iter_rows(
            min_row=2,
            values_only=True):


        if not row:
            continue


        if len(row) <= max(
                english_column,
                language_column):

            continue


        english = row[english_column]
        localized = row[language_column]


        if english is None or localized is None:
            continue


        english = str(english).strip()
        localized = str(localized).strip()


        if not english or not localized:
            continue



        strings.append({

            "english": english,

            "localized": localized,

            "normalized_english":
                normalize(english),

            "normalized":
                normalize(localized)

        })


    workbook.close()

    return strings




def verify_strings(
        objects,
        screen_name,
        excel_strings,
        expected_english_strings):


    runtime_candidates = []

    for obj in objects:

        runtime_candidates.extend(
            get_all_text_combinations(obj)
        )



    runtime_candidates = list(
        set(runtime_candidates)
    )

    normalized_runtime = []

    for text in runtime_candidates:

        normalized = normalize(text)

        if normalized:

            normalized_runtime.append(
                (normalized, text)
            )


    pass_count = 0
    fail_count = 0



    for expected_english in expected_english_strings:

        excel_item = None
        
        for item in excel_strings:

            if (
                item["normalized_english"]
                ==
                normalize(expected_english)
            ):

                excel_item = item

                break


        if excel_item is None:

            message = (
                "English string not found in Excel -> "
                + expected_english
            )

            print("FAIL: " + message)

            test.fail(message)

            fail_count += 1

            continue


        expected_localized = (
            excel_item["localized"]
        )

        expected_normalized = (
            excel_item["normalized"]
        )


        matched = False
        untranslated = False


     
        for actual_normalized, actual_text in normalized_runtime:

            if "XXXX" in str(expected_localized):
        
                if match_profile_placeholder(
                    actual_text,
                    expected_localized
                ):
                    matched = True
        
                    test.log(
                        "PASS: Dynamic placeholder matched -> "
                        + repr(actual_text)
                    )
                    break

            else:
        
                if actual_normalized == expected_normalized:
                    matched = True
                    break
        
                elif (
                    len(expected_normalized) >= 4
                    and expected_normalized in actual_normalized
                ):
                    matched = True
                    break

            if actual_normalized == excel_item["normalized_english"]:
                untranslated = True


            if actual_normalized == expected_normalized:

                matched = True

                break



            elif (
                len(expected_normalized) >= 4
                and
                expected_normalized
                in actual_normalized
            ):

                matched = True

                break


            if (
                actual_normalized
                ==
                excel_item["normalized_english"]
            ):

                untranslated = True


        if matched:

            print(
                "PASS: "
                + expected_english
                + " -> "
                + expected_localized
            )

            test.passes(
                expected_english
                + " -> "
                + expected_localized
            )

            pass_count += 1

        elif untranslated:

            message = (
                "UNTRANSLATED: "
                + expected_english
                + " is displayed instead of "
                + expected_localized
            )

            print("FAIL: " + message)

            test.fail(message)

            fail_count += 1


        else:

            message = (
                "Expected "
                + expected_english
                + " -> "
                + expected_localized
                + " but localized string was not found on "
                + screen_name
            )

            print("FAIL: " + message)

            test.fail(message)

            fail_count += 1

    print(
        screen_name
        + " Localization Result: PASS = "
        + str(pass_count)
        + ", FAIL = "
        + str(fail_count)
    )


    if fail_count == 0 and pass_count > 0:

        test.passes(
            screen_name
            + " LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            screen_name
            + " LOCALIZATION VALIDATION FAILED"
        )

def validate_localization(
        objects,
        screen_name,
        expected_strings,
        language=LANGUAGE,
        excel_path=EXCEL_PATH):

    excel_strings = load_localized_strings(
        language=LANGUAGE,
        excel_path=excel_path
    )

    verify_strings(
        objects=objects,
        screen_name=screen_name,
        excel_strings=excel_strings,
        expected_english_strings=expected_strings
    )
    
    
def enterpin():
    """Login to the application by accepting the popup and entering PIN 0000."""
    for i in range(4):
            clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton, 20000))
    
    test.passes("PASS: PIN 0000 entered")
    
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
    
    
def get_text_lines(obj):
    lines = []

    try:
        if not obj.visible:
            return lines
    except:
        pass

    try:
        text = str(obj.text).strip()
        if text:
            lines.append(text)
    except:
        pass

    # READ PLACEHOLDER TEXT
    try:
        placeholder = str(obj.placeholderText).strip()
        if placeholder:
            lines.append(placeholder)
    except:
        pass

    try:
        title = str(obj.title).strip()
        if title:
            lines.append(title)
    except:
        pass

    try:
        for child in object.children(obj):
            lines.extend(get_text_lines(child))
    except:
        pass

    return lines



def match_profile_placeholder(actual_text, expected_text):

    def clean_text(text):
        text = unicodedata.normalize("NFKC", str(text))

        text = text.casefold()

        text = text.translate(str.maketrans({
            "„": '"',
            "”": '"',
            "“": '"',
            "‟": '"',
            "’": "'",
            "‘": "'"
        }))

        text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+", " ", text).strip()

        return text

    actual = clean_text(actual_text)
    expected = clean_text(expected_text)

    if "xxxx" not in expected:
        return actual == expected

    pattern = re.escape(expected)

    pattern = pattern.replace(
        re.escape("xxxx"),
        r".+?"
    )

    return re.fullmatch(pattern, actual) is not None



def validate_aiming_beam_label():
 
    from openpyxl import load_workbook
 
    english_text = "AIMING BEAM"
 
    workbook = load_workbook(
        EXCEL_PATH,
        read_only=True,
        data_only=True
    )
 
    try:
        sheet = workbook["GUI Strings"]
 
        language_column = None
 
        for column in range(1, sheet.max_column + 1):
 
            language_name = sheet.cell(row=1, column=column).value
 
            if (
                language_name
                and str(language_name).strip().casefold()
                == LANGUAGE.strip().casefold()
            ):
                language_column = column
                break
 
        if language_column is None:
            test.fail(
                "Language '{}' not found in Excel.".format(LANGUAGE)
            )
            return
 
        expected_text = None
 
        for row in range(2, sheet.max_row + 1):
 
            english_value = sheet.cell(row=row, column=1).value
 
            if (
                english_value
                and str(english_value).strip().casefold()
                == english_text.casefold()
            ):
                expected_text = sheet.cell(
                    row=row,
                    column=language_column
                ).value
                break
 
        if expected_text is None or not str(expected_text).strip():
            test.fail(
                "'{}' translation not found in Excel for language '{}'.".format(
                    english_text,
                    LANGUAGE
                )
            )
            return
 
        expected_text = str(expected_text).strip()
 
    finally:
        workbook.close()
 
    aiming_beam_label = waitForObject({
        "name": "lbAimingBeam",
        "type": "QLabel"
    })
 
    actual_text = str(aiming_beam_label.text).strip()
 
    if normalize(actual_text) == normalize(expected_text):
 
        test.passes(
            english_text + " -> " + expected_text
        )
 
    else:
 
        test.fail(
            "FAIL: "
            + english_text
            + " -> "
            + expected_text
            + " | Actual UI text: "
            + actual_text
        )
        
        
def validate_assistant_label():

    from openpyxl import load_workbook

    english_text = "Assistant"

    workbook = load_workbook(
        EXCEL_PATH,
        read_only=True,
        data_only=True
    )

    try:
        sheet = workbook["GUI Strings"]

        language_column = None

        for column in range(1, sheet.max_column + 1):
            language_name = sheet.cell(row=1, column=column).value

            if (
                language_name
                and str(language_name).strip().casefold()
                == LANGUAGE.strip().casefold()
            ):
                language_column = column
                break

        if language_column is None:
            test.fail(
                "Language '{}' not found in Excel.".format(LANGUAGE)
            )
            return

        expected_text = None

        for row in range(2, sheet.max_row + 1):
            english_value = sheet.cell(row=row, column=1).value

            if (
                english_value
                and str(english_value).strip().casefold()
                == english_text.casefold()
            ):
                expected_text = sheet.cell(
                    row=row,
                    column=language_column
                ).value
                break

        if expected_text is None or not str(expected_text).strip():
            test.fail(
                "'{}' translation not found in Excel for language '{}'.".format(
                    english_text,
                    LANGUAGE
                )
            )
            return

        expected_text = str(expected_text).strip()

    finally:
        workbook.close()

    assistant_button = waitForObject(
        names.apollo_tbAssistant_QToolButton
    )

    actual_text = str(
        assistant_button.property("localizationText")
    ).strip()

    if normalize(actual_text) == normalize(expected_text):

        test.passes(
            english_text + " -> " + expected_text
        )

    else:

        test.fail(
            "FAIL: "
            + english_text
            + " -> "
            + expected_text
            + " | Actual UI text: "
            + actual_text
        )
