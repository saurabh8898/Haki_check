from questions import questions

def ask_question(question, options):
    print(question)
    for option in options:
        print(f"{option['value']}: {option['text']}")
    answer = input("Enter your choice: ").lower()
    while answer not in [option['value'] for option in options]:
        answer = input("Invalid choice. Enter again: ").lower()
    return answer

def determine_haki_type(answers):
    # Count the frequency of each answer
    frequency = {key: answers.count(key) for key in set(answers)}

    # Determine the Haki type based on the most frequent answer
    haki_map = {
        "a": "Conqueror's Haki",
        "b": "Observation Haki",
        "c": "Armament Haki",
        "d": "Observation Haki",
        "e": "Conqueror's Haki",
        "f": "Observation Haki",
        "g": "Armament Haki"
    }

    # Find the most frequent answer(s)
    max_freq = max(frequency.values())
    most_common_answers = [key for key, value in frequency.items() if value == max_freq]

    # If there's a tie, we'll just pick the first one (or handle ties differently if needed)
    dominant_answer = most_common_answers[0]
    return haki_map[dominant_answer]

def main():
    print("Welcome to the Haki Quiz!")
    answers = []
    for question_data in questions:
        answer = ask_question(question_data["question"], question_data["options"])
        answers.append(answer)

    haki_type = determine_haki_type(answers)
    print("\nYour dominant Haki type is:", haki_type)

if __name__ == "__main__":
    main()
