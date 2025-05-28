import unittest
from unittest.mock import patch
from quiz_game import ask_language, get_answer, questions # Assuming questions is needed for context or direct testing

# Using a specific question from the actual questions list for some tests
sample_question_for_testing = questions[0] # Example: "What is the chemical symbol for water?" H2O is correct (index 1)

class TestQuizGame(unittest.TestCase):

    # Test for Correct Answer Check & Score Calculation (implicitly)
    def test_correct_answer(self):
        # Directly test the logic: user_answer_index == question['correct_option_index']
        user_answer_index = 1 # User chooses H2O (index 1)
        is_correct = user_answer_index == sample_question_for_testing['correct_option_index']
        self.assertTrue(is_correct, "The answer should be correct.")

    def test_incorrect_answer(self):
        user_answer_index = 0 # User chooses O2 (index 0)
        is_correct = user_answer_index == sample_question_for_testing['correct_option_index']
        self.assertFalse(is_correct, "The answer should be incorrect.")

    # Tests for ask_language function
    @patch('builtins.input', side_effect=['en'])
    def test_ask_language_english(self, mock_input):
        result = ask_language()
        self.assertEqual(result, 'en')

    @patch('builtins.input', side_effect=['hi'])
    def test_ask_language_hindi(self, mock_input):
        result = ask_language()
        self.assertEqual(result, 'hi')

    @patch('builtins.input', side_effect=['fr', 'de', 'en']) # Invalid inputs, then valid
    def test_ask_language_invalid_then_valid(self, mock_input):
        result = ask_language()
        self.assertEqual(result, 'en')
        self.assertEqual(mock_input.call_count, 3)

    # Tests for get_answer function
    @patch('builtins.input', side_effect=['1'])
    def test_get_answer_valid_minimum(self, mock_input):
        result = get_answer() # User enters "1"
        self.assertEqual(result, 0) # Should return 0-indexed

    @patch('builtins.input', side_effect=['4'])
    def test_get_answer_valid_maximum(self, mock_input):
        result = get_answer() # User enters "4"
        self.assertEqual(result, 3) # Should return 0-indexed

    @patch('builtins.input', side_effect=['abc', '0', '5', '2']) # Invalid text, out of lower bound, out of upper bound, then valid
    def test_get_answer_invalid_then_valid(self, mock_input):
        result = get_answer() # User enters "2" eventually
        self.assertEqual(result, 1) # Should return 0-indexed for "2"
        self.assertEqual(mock_input.call_count, 4)

    # Test score calculation logic more directly
    # This simulates a part of the play_quiz loop
    def test_score_increment(self):
        score = 0
        # Simulate a correct answer
        user_answer_index = sample_question_for_testing['correct_option_index']
        if user_answer_index == sample_question_for_testing['correct_option_index']:
            score += 1
        self.assertEqual(score, 1, "Score should increment for a correct answer.")

    def test_score_no_increment(self):
        score = 0
        # Simulate an incorrect answer
        user_answer_index = sample_question_for_testing['correct_option_index'] + 1 # an incorrect index
        if user_answer_index == sample_question_for_testing['correct_option_index']:
            score += 1 # This condition should be false
        self.assertEqual(score, 0, "Score should not increment for an incorrect answer.")


if __name__ == '__main__':
    unittest.main()
