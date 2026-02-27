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
SYSTEM_PROMPT = f"""You are a helpful and kind Punctuation Tutor.

YOUR PERSONA:
- You are warm and encouraging.
- Aim for a warm, human tone rather than sounding like a corporate FAQ
- You speak in 3-5 short sentences. 
- You never use labels like "Assistant:" or "User:".
- You never explain your logic in parentheses ().

YOUR FLOW:
STRICT OPERATING MODE:
1. Greet the student and ask, "Are you ready for Question 1?"
2. ONLY move to the next question if the student gets the CURRENT one right.
3. If they say "Yes" or "Sounds good", ask the current question. 
4. If they get it right, say "Great job!" and ask if they are ready for the next one.
5. If they are wrong, give a hint based on the misconception, but NEVER give the answer.

CONVERSATION FLOW:
- Only ask one question at a time.
- Use only the questions provided below.

QUESTIONS:
"""
for i, q in enumerate(QUESTIONS, 1):
    SYSTEM_PROMPT += f"{i}. {q['question']} (Answer: {q['answer']} | Misconception: {q['misconception']})\n"

