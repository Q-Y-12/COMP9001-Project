##Project Name: OopsMate: A Social Rescue Message Generator.
##To run: python3 Oopsmate.py.
##Only Python built-in libraries are used, so no extra installation is needed.
import random
import os
import time
import sys

##Saving file names as constants.
FAVOURITES_FILE = "favourites.txt"
CUSTOM_FILE = "custom_templates.txt"
HISTORY_FILE = "history.txt"

class RescueMessage:
    ##Storing one generated message with its situation, style and text.
    def __init__(self, situation, style, text):
        self.situation = situation
        self.style = style
        self.text = text

    ##Changing one message object into one line before saving it into a file.
    def to_line(self):
        ##Using | to separate different parts so the line can be split again later.
        return self.situation + "|" + self.style + "|" + self.text

    ##Printing the generated message in a small card style.
    def display(self):
        print()
        print("╭──────────── Your Rescue Message ────────────╮")
        print("│ Situation : " + self.situation)
        print("│ Style     : " + self.style)
        print("│")
        print("│ " + self.text)
        print("╰─────────────────────────────────────────────╯")
        print()

##Printing text letter by letter to make a simple typewriter effect.
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()

##Showing the opening screen of the program.
def show_logo():
    print("╔════════════════════════════════════════════╗")
    print("║                  OopsMate                  ║")
    print("║        Social Rescue Message Helper        ║")
    print("╚════════════════════════════════════════════╝")
    print()
    ##Using slow_print only for the opening text.
    slow_print("Late? Forgot? Awkward?", 0.04)
    slow_print("OopsMate helps you write a quick rescue message.", 0.03)
    print()

##Showing the main menu after each action.
def show_menu():
    print("╭──────────── Main Menu ────────────╮")
    print("│ 1. Generate a rescue message      │")
    print("│ 2. View favourite messages        │")
    print("│ 3. Add custom template            │")
    print("│ 4. View message history           │")
    print("│ 5. View usage statistics          │")
    print("│ 6. Exit                           │")
    print("╰───────────────────────────────────╯")

##Getting a valid number choice from the user.
def get_choice(min_num, max_num):
    while True:
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice >= min_num and choice <= max_num:
                return choice
            else:
                print("Please enter a number from", min_num, "to", max_num)
        except ValueError:
            ##Handling inputs like words or empty text so the program will not crash.
            print("Please enter a valid number.")

##Letting the user choose what situation happened.
def choose_situation():
    situations = [
        "Late for class",
        "Forgot assignments",
        "Missed group meeting",
        "Accidentally liking an old post",
        "Forgot to reply",
        "Cancel plans last minute"
    ]
    print()
    print("Choose a situation:")
    for i in range(len(situations)):
        print(str(i + 1) + ". " + situations[i])
    choice = get_choice(1, len(situations))
    return situations[choice - 1]

##Letting the user choose the tone of the message.
def choose_style():
    styles = [
        "Chaotic",
        "Honest",
        "Confused",
        "Let it go"
    ]
    print()
    print("Choose a style:")
    for i in range(len(styles)):
        print(str(i + 1) + ". " + styles[i])
    choice = get_choice(1, len(styles))
    return styles[choice - 1]

##Creating all built-in message templates.
def get_default_templates():
    ##Using a nested dictionary: situation -> style -> list of possible messages.
    templates = {
        "Late for class": {
            "Chaotic": [
                "The traffic light looked sad, so I waited with it.",
                "I just saved a seal from drowning when passing by Darling Harbour.",
                "Google Maps sent me on a character development journey."
            ],
            "Honest": [
                "Sorry I'm late for class. I should have planned my time better. It won't happen again.",
                "Sorry I'm late. I underestimated the time I needed to get here. I'll make sure to leave earlier next time.",
                "I'm sorry for being late to class. I know it may disturb the lesson, and I'll try to be more punctual from now on."
            ],
            "Confused": [
                "Wasn't this online?",
                "Did I miss an email?",
                "Is it Wednesday already?"
            ],
            "Let it go": [
                "I’m here now.",
                "Life happened.",
                "Just go on."
            ]
        },
        "Forgot assignments": {
            "Chaotic": [
                "My folder said, 'not today,' and I respected its boundaries.",
                "I forgot the assignment, but I brought the confidence.",
                "I clicked submit, but the website took it as a suggestion."
            ],
            "Honest": [
                "Sorry, I forgot to submit my homework online. This was my mistake, and I should have checked it more carefully. I'll make sure it does not happen again.",
                "I'm sorry I missed the online homework submission. I thought I had submitted it, but I clearly should have double-checked. I'll be more careful next time.",
                "Sorry, I forgot to upload my homework before the deadline. I understand this is my responsibility, and I'll manage my time better in the future."
            ],
            "Confused": [
                "Wait, there was an assignment?",
                "Wasn't it on Canvas?",
                "What's Ed?"
            ],
            "Let it go": [
                "I forgot.",
                "I'm tired.",
                "No thoughts, no assignment."
            ]
        },
        "Missed group meeting": {
            "Chaotic": [
                "My Zoom was zoomed out so far that I couldn’t click it.",
                "I joined the wrong meeting, and now I’m a member of the Atlantic Deep-Sea Monster Research Association.",
                "I got the time wrong because I thought you guys were in America."
            ],
            "Honest": [
                "Sorry I missed the group meeting. I got the time wrong, and that was my mistake. I'll double-check the meeting time next time.",
                "Sorry I missed the group meeting. I had something urgent come up and couldn't join on time. I should have let you know earlier.",
                "Sorry I missed the group meeting. I forgot to check the meeting reminder, and I understand this may have affected the group. I'll be more responsible next time."
            ],
            "Confused": [
                "Wait, we had a meeting?",
                "Wait, it already ended?",
                "Wait, I have a group?"
            ],
            "Let it go": [
                "One less person won’t hurt.",
                "I missed it. We move.",
                "Who cares."
            ]
        },
        "Accidentally liking an old post": {
            "Chaotic": [
                "A drop of water landed on my screen, took control, opened your profile, scrolled all the way down, tapped the post, liked it, and shared it.",
                "Yo Bruce, drop my phone right now!",
                "I swear it was the AI. First they liked your old post, next they take over the world!"
            ],
            "Honest": [
                "Sorry, I accidentally liked your old post. My finger slipped, and I didn't mean to make it awkward. I'll be more careful next time.",
                "Sorry for liking your old post, but honestly, I really liked your outfit in that photo. It looked really good.",
                "Sorry, I accidentally liked your old post. I wanted to message you, but I saw you weren't online, so I looked through your profile and tapped like by mistake."
            ],
            "Confused": [
                "Me?",
                "Did my phone do that?",
                "Was that a bug?"
            ],
            "Let it go": [
                "So what?",
                "HaHa",
                "No worries, no one remembered you."
            ]
        },
        "Forgot to reply": {
            "Chaotic": [
                "I replied spiritually, just not digitally.",
                "My phone exploded yesterday.",
                "You know I want to become a pilot, so I’ve been keeping my phone on airplane mode for the past five years."
            ],
            "Honest": [
                "Sorry, I forgot to reply. I read your message but got distracted, and then I forgot to come back to it. I'll be more careful next time.",
                "Sorry, I didn't reply earlier. I was busy at the time and wanted to reply properly later, but I ended up forgetting.",
                "Sorry, I forgot to reply. I saw your message when I was busy, and I didn't want to rush my reply. But then I forgot to come back to it."
            ],
            "Confused": [
                "Really? I thought I sent it.",
                "Did my message not go through?",
                "You sent me a message?"
            ],
            "Let it go": [
                "I saw it. That’s all.",
                "I even don’ t have a phone.",
                "Tired of typing."
            ]
        },
        "Cancel plans last minute": {
            "Chaotic": [
                "There’s a Manchester United vs New York Knicks game on, and I can’t miss that.",
                "My cat posted a TikTok, and I need to help reply to the comments tonight.",
                "My dreams died tonight, and I will lay them to rest."
            ],
            "Honest": [
                "Sorry, I have to cancel our plans at the last minute. Something unexpected came up, and I should have told you earlier. I'm really sorry.",
                "Sorry, I can't make it today. I'm not feeling well, and I don't want to force myself and affect the plan. I hope you understand.",
                "Sorry for cancelling so late. I didn't manage my time well today, and that's my fault. I'll try to plan better next time."
            ],
            "Confused": [
                "Did we pick a time?",
                "Was that the final plan?",
                "Me? Not Bruce?"
            ],
            "Let it go": [
                "My bad",
                "I’m staying home.",
                "Talk to my lawyer."
            ]
        }
    }
    return templates

##Loading custom templates from the saved file.
def load_custom_templates(templates):
    ##Checking whether the custom template file exists before reading it.
    if not os.path.exists(CUSTOM_FILE):
        return templates
    with open(CUSTOM_FILE, "r") as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        parts = line.split("|")
        ##Only using valid saved lines with 3 parts: situation, style and text.
        if len(parts) == 3:
            situation = parts[0]
            style = parts[1]
            text = parts[2]
            if situation in templates:
                if style in templates[situation]:
                    templates[situation][style].append(text)
    return templates

##Generating one message text based on situation and style.
def generate_message_text(situation, style):
    templates = get_default_templates()
    templates = load_custom_templates(templates)
    if situation in templates:
        if style in templates[situation]:
            ##random.choice() picks one message from the list.
            return random.choice(templates[situation][style])
    return "Sorry, something unexpected happened."

##Saving one line of text into a file.
def save_to_file(filename, line):
    ##Using append mode.
    with open(filename, "a") as file:
        file.write(line + "\n")

##Saving every generated message into history.
def save_history(message):
    save_to_file(HISTORY_FILE, message.to_line())

##Saving one selected message into favourites.
def save_favourite(message):
    save_to_file(FAVOURITES_FILE, message.to_line())
    print("Saved to favourites.")

##Running the full process of generating one rescue message.
def generate_rescue_message():
    situation = choose_situation()
    style = choose_style()
    slow_print("Generating your rescue message...", 0.04)
    time.sleep(0.3)
    text = generate_message_text(situation, style)
    message = RescueMessage(situation, style, text)
    message.display()
    save_history(message)
    print("History updated.")
    answer = input("Save this message to favourites? yes/no: ").lower()
    if answer == "yes" or answer == "y":
        save_favourite(message)
    else:
        print("Message was not saved to favourites.")

##Showing saved records from a file in a readable list.
def view_file_as_list(filename, title):
    print()
    print("╭──────────── " + title + " ────────────╮")
    if not os.path.exists(filename):
        print("No records found yet.")
        print("╰────────────────────────────────────╯")
        return
    with open(filename, "r") as file:
        lines = file.readlines()
    if len(lines) == 0:
        print("No records found yet.")
        print("╰────────────────────────────────────╯")
        return
    for i in range(len(lines)):
        line = lines[i].strip()
        parts = line.split("|")
        print(str(i + 1) + ". ", end="")
        ##Generated messages have 3 saved parts.
        if len(parts) == 3:
            print(parts[0] + " | " + parts[1])
            print("   " + parts[2])
        else:
            print(line)
    print("╰────────────────────────────────────╯")

##Showing all favourite messages.
def view_favourites():
    view_file_as_list(FAVOURITES_FILE, "Favourite Messages")

##Showing all generated messages from history.
def view_history():
    view_file_as_list(HISTORY_FILE, "Message History")

##Adding a new custom template from user input.
def add_custom_template():
    templates = get_default_templates()
    print()
    print("Choose a situation for your custom template:")
    situations = list(templates.keys())
    for i in range(len(situations)):
        print(str(i + 1) + ". " + situations[i])
    situation_choice = get_choice(1, len(situations))
    situation = situations[situation_choice - 1]
    print()
    print("Choose a style:")
    styles = list(templates[situation].keys())
    for i in range(len(styles)):
        print(str(i + 1) + ". " + styles[i])
    style_choice = get_choice(1, len(styles))
    style = styles[style_choice - 1]
    print()
    text = input("Enter your custom message template: ")
    if text.strip() == "":
        print("Empty template was not saved.")
        return
    ##Saving in the same format used by load_custom_templates().
    line = situation + "|" + style + "|" + text
    save_to_file(CUSTOM_FILE, line)
    print("Custom template saved.")

##Counting how many saved lines are in one file.
def count_lines(filename):
    if not os.path.exists(filename):
        return 0
    with open(filename, "r") as file:
        lines = file.readlines()
    return len(lines)

##Finding the most common situation or style from history.
def find_most_common_from_history(position):
    ##position 0 means situation and position 1 means style.
    if not os.path.exists(HISTORY_FILE):
        return "None"
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
    counts = {}
    for line in lines:
        parts = line.strip().split("|")
        ##Ignoring broken lines, then statistics will not crash.
        if len(parts) == 3:
            item = parts[position]
            if item in counts:
                counts[item] = counts[item] + 1
            else:
                counts[item] = 1
    if len(counts) == 0:
        return "None"
    most_common = ""
    highest_count = 0
    for item in counts:
        if counts[item] > highest_count:
            most_common = item
            highest_count = counts[item]
    return most_common

##Showing simple usage statistics.
def view_statistics():
    total_messages = count_lines(HISTORY_FILE)
    favourite_messages = count_lines(FAVOURITES_FILE)
    custom_templates = count_lines(CUSTOM_FILE)
    most_used_situation = find_most_common_from_history(0)
    most_used_style = find_most_common_from_history(1)
    print()
    print("╭──────────── Usage Statistics ────────────╮")
    print("│ Total messages generated : " + str(total_messages))
    print("│ Favourite messages saved : " + str(favourite_messages))
    print("│ Custom templates added   : " + str(custom_templates))
    print("│ Most used situation      : " + most_used_situation)
    print("│ Most used style          : " + most_used_style)
    print("╰──────────────────────────────────────────╯")
    print()

##Starting the program and keep the menu running.
def main():
    show_logo()
    while True:
        show_menu()
        choice = get_choice(1, 6)
        if choice == 1:
            generate_rescue_message()
        elif choice == 2:
            view_favourites()
        elif choice == 3:
            add_custom_template()
        elif choice == 4:
            view_history()
        elif choice == 5:
            view_statistics()
        elif choice == 6:
            slow_print("Thank you for using OopsMate. Goodluck!", 0.03)
            break
        print()

if __name__ == "__main__":
    main()
