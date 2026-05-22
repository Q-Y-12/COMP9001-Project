##Test file for Oopsmate.py.
##To run: python3 OopsmateTest.py.
##These tests check the main non-interactive parts of the program.
import os
import Oopsmate

TEST_HISTORY_FILE = "test_history.txt"
TEST_FAVOURITES_FILE = "test_favourites.txt"
TEST_CUSTOM_FILE = "test_custom_templates.txt"

##Removing old test files before starting, so results are clean.
def clean_test_files():
    files = [TEST_HISTORY_FILE, TEST_FAVOURITES_FILE, TEST_CUSTOM_FILE]
    for filename in files:
        if os.path.exists(filename):
            os.remove(filename)

##Testing whether RescueMessage can be saved as one correct line.
def test_rescue_message_to_line():
    message = Oopsmate.RescueMessage("Late for class", "Confused", "Wasn't this online?")
    assert message.to_line() == "Late for class|Confused|Wasn't this online?"

##Testing whether the template dictionary has the expected situations and styles.
def test_default_templates():
    templates = Oopsmate.get_default_templates()
    assert "Late for class" in templates
    assert "Forgot assignments" in templates
    assert "Chaotic" in templates["Late for class"]
    assert "Honest" in templates["Late for class"]
    assert "Confused" in templates["Late for class"]
    assert "Let it go" in templates["Late for class"]
    assert len(templates["Late for class"]["Chaotic"]) == 3

##Testing whether generate_message_text returns one message from the correct list.
def test_generate_message_text():
    text = Oopsmate.generate_message_text("Forgot assignments", "Confused")
    possible_texts = Oopsmate.get_default_templates()["Forgot assignments"]["Confused"]
    assert text in possible_texts

##Testing whether save_to_file and count_lines work correctly.
def test_save_and_count_lines():
    Oopsmate.save_to_file(TEST_FAVOURITES_FILE, "one")
    Oopsmate.save_to_file(TEST_FAVOURITES_FILE, "two")
    assert Oopsmate.count_lines(TEST_FAVOURITES_FILE) == 2

##Testing whether history statistics can find the most common situation and style.
def test_find_most_common_from_history():
    original_history_file = Oopsmate.HISTORY_FILE
    Oopsmate.HISTORY_FILE = TEST_HISTORY_FILE
    Oopsmate.save_to_file(TEST_HISTORY_FILE, "Late for class|Chaotic|Test message one")
    Oopsmate.save_to_file(TEST_HISTORY_FILE, "Late for class|Honest|Test message two")
    Oopsmate.save_to_file(TEST_HISTORY_FILE, "Forgot to reply|Chaotic|Test message three")
    assert Oopsmate.find_most_common_from_history(0) == "Late for class"
    assert Oopsmate.find_most_common_from_history(1) == "Chaotic"
    Oopsmate.HISTORY_FILE = original_history_file

##Running all tests together.
def run_tests():
    clean_test_files()
    test_rescue_message_to_line()
    test_default_templates()
    test_generate_message_text()
    test_save_and_count_lines()
    test_find_most_common_from_history()
    clean_test_files()
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
