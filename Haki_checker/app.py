from flask import Flask, request, render_template_string
import os
import time
import platform
from questions import questions

auro_or_haki = {
    'Conquerers_Haki(Red)': ['Bravery', 'Passion', 'Determination', 'Strength', 'Courage'],
    'Observation_Haki(Blue)': ['Calmness', 'Wisdom', 'Intelligence', 'Serenity', 'Trustworthiness'],
    'Armament_Haki(Green)': ['Growth', 'Harmony', 'Balance', 'Empathy', 'Healing'],
    'Brightheart Haki (Yellow)': ['Optimism', 'Joy', 'Creativity', 'Enthusiasm', 'Charisma'],
    'Supreme_King Haki(Purple)': ['Intuition', 'Spirituality', 'Mystery', 'Imagination', 'Ambition'],
    'Abyssal Haki (Black)': ['Power', 'Control', 'Mystery', 'Ambition', 'Discipline'],
    'Divine Purity Haki (White)': ['Purity', 'Clarity', 'Peacefulness', 'Honesty', 'Integrity']
}

# Initialize color values
red, blue, green, yellow, black, purple, white = 0, 0, 0, 0, 0, 0, 0

def clear_screen():
    """Clear the screen based on the operating system."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def time_delay(seconds):
    """Pause the program for a specified number of seconds."""
    time.sleep(seconds)

def ask_question(question, options):
    """Ask a question, print options, and increment color values based on user input."""
    global red, blue, green, yellow, black, purple, white
    print(question)
    for option in options:
        print(option)
    answer = input("Choose an option (A, B, C, D, E, F, G): ").lower()
    
    if answer == "a":
        red += 1
    elif answer == "b":
        blue += 1
    elif answer == "c":
        green += 1
    elif answer == "d":
        yellow += 1
    elif answer == "e":
        black += 1
    elif answer == "f":
        purple += 1
    elif answer == "g":
        white += 1
    else:
        print("Invalid choice")

def determine_haki():
    """Determine and print the Haki based on color values."""
    if red >= 5:
        print("Color of a Conquerors Haki which is Red")
        print(f"You have the following traits: {', '.join(auro_or_haki['Conquerers_Haki(Red)'])}")
    elif blue >= 5:
        print("Color of an Observation Haki which is Blue")
        print(f"You have the following traits: {', '.join(auro_or_haki['Observation_Haki(Blue)'])}")
    elif green >= 5:
        print("Color of an Armament Haki which is Green")
        print(f"You have the following traits: {', '.join(auro_or_haki['Armament_Haki(Green)'])}")
    elif yellow >= 5:
        print("Color of a Brightheart Haki which is Yellow")
        print(f"You have the following traits: {', '.join(auro_or_haki['Brightheart Haki (Yellow)'])}")
    elif purple >= 5:
        print("Color of a Supreme King Haki which is Purple")
        print(f"You have the following traits: {', '.join(auro_or_haki['Supreme_King Haki(Purple)'])}")
    elif black >= 5:
        print("Color of an Abyssal Haki which is Black")
        print(f"You have the following traits: {', '.join(auro_or_haki['Abyssal Haki (Black)'])}")
    elif white >= 5:
        print("Color of a Divine Purity Haki which is White")
        print(f"You have the following traits: {', '.join(auro_or_haki['Divine Purity Haki (White)'])}")
    else:
        print("No Haki Developed yet work harder!")

# Main loop to ask questions until a color value reaches 5
while all(v < 5 for v in [red, blue, green, yellow, black, purple, white]):
    for q in questions:
        ask_question(q["question"], q["options"])
        clear_screen()
        if any(v >= 5 for v in [red, blue, green, yellow, black, purple, white]):
            break

# Determine and print the Haki
determine_haki()