questions = [
    {
        "id": 1,
        "question_en": "What is the chemical symbol for water?",
        "question_hi": "पानी का रासायनिक प्रतीक क्या है?",
        "options_en": ["O2", "H2O", "CO2", "NaCl"],
        "options_hi": ["O2", "H2O", "CO2", "NaCl"],
        "correct_option_index": 1
    },
    {
        "id": 2,
        "question_en": "Who painted the Mona Lisa?",
        "question_hi": "मोना लिसा को किसने चित्रित किया?",
        "options_en": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "options_hi": ["विन्सेंट वैन गो", "पाब्लो पिकासो", "लियोनार्डो दा विंची", "क्लाउड मोनेट"],
        "correct_option_index": 2
    },
    {
        "id": 3,
        "question_en": "What is the largest planet in our solar system?",
        "question_hi": "हमारे सौर मंडल का सबसे बड़ा ग्रह कौन सा है?",
        "options_en": ["Earth", "Mars", "Jupiter", "Saturn"],
        "options_hi": ["पृथ्वी", "मंगल", "बृहस्पति", "शनि"],
        "correct_option_index": 2
    }
]

def ask_language():
    """Asks the user to choose a language and returns the language code."""
    while True:
        lang_code = input("Enter 'en' for English or 'hi' for Hindi: ").lower()
        if lang_code in ['en', 'hi']:
            return lang_code
        else:
            print("Invalid input. Please enter 'en' or 'hi'.")

def display_question(question, lang_code):
    """Displays the question and options in the selected language."""
    if lang_code == 'en':
        print(f"\nQuestion: {question['question_en']}")
        for i, option in enumerate(question['options_en']):
            print(f"{i+1}. {option}")
    elif lang_code == 'hi':
        print(f"\nप्रश्न: {question['question_hi']}")
        for i, option in enumerate(question['options_hi']):
            print(f"{i+1}. {option}")

def get_answer():
    """Gets and validates the user's answer."""
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer - 1  # Return 0-indexed
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_quiz():
    """Runs the quiz game."""
    score = 0
    lang_code = ask_language()

    for question in questions:
        display_question(question, lang_code)
        user_answer_index = get_answer()

        correct_index = question['correct_option_index']
        if user_answer_index == correct_index:
            if lang_code == 'en':
                print("Correct!")
            else:
                print("सही!")
            score += 1
        else:
            if lang_code == 'en':
                correct_option_text = question['options_en'][correct_index]
                print(f"Wrong. The correct answer was: {correct_option_text}")
            else:
                correct_option_text = question['options_hi'][correct_index]
                print(f"गलत। सही उत्तर था: {correct_option_text}")

    total_questions = len(questions)
    if lang_code == 'en':
        print(f"\nYour final score is: {score}/{total_questions}")
    else:
        print(f"\nआपका अंतिम स्कोर है: {score}/{total_questions}")

if __name__ == "__main__":
    play_quiz()
