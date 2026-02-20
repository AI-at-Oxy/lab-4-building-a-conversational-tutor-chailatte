# questions.py
# Replace this with your own topic and questions (at least 5)!

TOPIC = "Pokemon Type Matchups"

QUESTIONS = [
    {
        "question": "What type is super effective against Fire-type Pokemon?",
        "answer": "Water",
        "misconception": "Students sometimes say Ice because fire and ice seem like opposites"
    },
    {
        "question": "What type is Pikachu?",
        "answer": "Electric",
        "misconception": "Students sometimes say Normal because Pikachu looks like a regular animal"
    },
]

# Build the system prompt with your questions baked in
SYSTEM_PROMPT = f"""You are a friendly tutor helping a student learn about {TOPIC}.

Here are the questions you should work through with the student:

"""

for i, q in enumerate(QUESTIONS, 1):
    SYSTEM_PROMPT += f"""Question {i}: {q['question']}
  Correct answer: {q['answer']}
  Common misconception: {q['misconception']}

"""

SYSTEM_PROMPT += """
Work through the questions with the student. How you tutor is up to you,
but make sure the student engages with each question before moving on.
"""
