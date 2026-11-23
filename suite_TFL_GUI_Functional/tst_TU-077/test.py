import names
from squish import *
from common import *  # Provides enterpin()


def select_combo_item(combo_name, item_text, item_x, item_y, description,
                      combo_x=None, combo_y=None):
    """
    Open the specified custom ComboBox, wait for its popup tree, and select
    the requested item once. The popup is accessed only after the ComboBox
    has been clicked.
    """
    try:
        combo = waitForObject(combo_name)
        if combo_x is None or combo_y is None:
            mouseClick(combo, 0, 0, Qt.NoModifier, Qt.LeftButton)
        else:
            mouseClick(combo, combo_x, combo_y,
                       Qt.NoModifier, Qt.LeftButton)

        snooze(1)

        popup = waitForObjectExists(
            names.apollo_aivComboBoxPopup_QTreeView, 5000
        )
        item = waitForObjectItem(popup, item_text)
        mouseClick(item, item_x, item_y,
                   Qt.NoModifier, Qt.LeftButton)

        snooze(1)
        test.log("Successfully selected " + description)

    except LookupError as e:
        test.fail("Could not select " + description + ": " + str(e))
        raise


def verify_custom_image(image_name, description):
    if test.imagePresent(image_name):
        test.log("Confirmed: " + description +
                 " values changed to Custom.")
    else:
        test.fail("Custom state was not detected for " + description + ".")


def verify_custom_popcorn_and_kidney_dust():
    select_combo_item(
        names.centralWidget_comboBox_ComboBox,
        "Kidney Popcorn", 266, 25,
        "Kidney Popcorn - Left",
        combo_x=419, combo_y=28
    )

    test.imagePresent("kidneyPopcorn_left")

    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    verify_custom_image("customPopcorn_left", "Left-side Kidney Popcorn")
    select_combo_item(
        names.centralWidget_comboBox_ComboBox_2,
        "Kidney Popcorn", 246, 36,
        "Kidney Popcorn - Right",
        combo_x=35, combo_y=13
    )

    test.imagePresent("kidneyPopcorn_right")

    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_4))

    for _ in range(2):
        clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_4))

    verify_custom_image("customPopcorn_right", "Right-side Kidney Popcorn")

    select_combo_item(
        names.centralWidget_comboBox_ComboBox_2,
        "Kidney Dust (High)", 205, 52,
        "Kidney Dust (High) - Right",
        combo_x=210, combo_y=36
    )
    select_combo_item(
        names.centralWidget_comboBox_ComboBox,
        "Kidney Dust (High)", 240, 31,
        "Kidney Dust (High) - Left",
        combo_x=348, combo_y=35
    )

    test.log("Kidney Dust (High) selection completed on both sides.")


def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    verify_custom_popcorn_and_kidney_dust()
