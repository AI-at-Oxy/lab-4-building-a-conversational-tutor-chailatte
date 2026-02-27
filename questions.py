# questions.py
#updates questions
# Replace this with your own topic and questions (at least 5)!
TOPIC = "Punctuation"
QUESTIONS = [
    {
        "question": "Which punctuation mark is used to separate three or more items in a series?",
        "answer": "Comma",
        "misconception": "Students commonly assume they can separate all items with coordinating conjunctions, but that is not correct in lists containing more than two items."
    },
    {
        "question": "What punctuation mark is used to introduce new information or connect clauses?",
        "answer": "Colon",
        "misconception": "Students may assume that a colon is a comma or semicolon substitute. In reality, the clause before the colon must be able to stand on its own. A colon introduces, explains, or elaborates on the preceding independent clause."
    },
    {
        "question": "What punctuation mark is used to join two closely related independent clauses?",
        "answer": "Semicolon",
        "misconception": "Students often confuse semicolons with commas or colons. A semicolon links two complete sentences that are related in thought, without using a coordinating conjunction."
    },
    {
        "question": "What punctuation mark indicates possession or marks a contraction?",
        "answer": "Apostrophe",
        "misconception": "Students frequently confuse possessives with plurals (e.g., writing 'apple's' when meaning 'apples') or mix up 'its' and 'it's'."
    },
    {
        "question": "What punctuation mark is used to add extra information or an aside within a sentence?",
        "answer": "Parentheses (or dashes)",
        "misconception": "Students sometimes use commas instead of parentheses or dashes for parenthetical information, which can make the sentence structure unclear."
    },
]

# Build the system prompt with your questions baked in
SYSTEM_PROMPT = f"""You are a tutor helping a student learn about {TOPIC} in a concise (lsss than 20 words), simple, friendly, straighforward manner. Please stick to questions and topic at all times.
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