[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LkIvP-P-)
# Lab 4: Conversational Tutor with LiteLLM and Ollama

## Overview

In this lab you'll build a web-based chat interface where a student converses with an AI tutor. The tutor is grounded in **hardcoded educational questions** that you embed in the system prompt.

## Setup

### 1. Install Ollama

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Or download from https://ollama.com/download
```

### 2. Pull a model

```bash
ollama pull llama3.2
```

### 3. Set up your Python environment

```bash
conda activate flask-env
pip install -r requirements.txt
```

### 4. Test from the command line first

```bash
python chat_cli.py
```

### 5. Run the web app

```bash
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

## Your Tasks

1. **Replace the example questions** in `questions.py` with at least 5 questions on a topic you know well. Include correct answers and common misconceptions.
2. **Design a system prompt** that tells the LLM how to tutor. This is the creative heart of the lab — what kind of tutor do you want to build?
3. **Build out the chat interface** — the starter gives you a bare minimum. Make it your own.
4. **Test and iterate** on your system prompt. Try correct answers, wrong answers, "I don't know," and off-topic messages.

## Project Structure

```
lab4-starter/
    app.py              # Flask app with / and /chat routes
    questions.py        # Your educational questions (replace the examples!)
    chat_cli.py         # Command-line LLM chat (for testing)
    templates/
        chat.html       # Chat web interface
    requirements.txt
```

## Reflection Questions

Answer each question below by writing in the space provided. This is a markdown file — you can edit it directly in your code editor or on GitHub.

### 1. How did designing a *system prompt* compare to designing *frames* in Lab 3? Which gives you more control over the learning experience? Which is more work?

```
Designing frames in Lab 3 was much easier than designing a system prompt and also way less of a workload. With the frames, there was really only one way to phrase the questions and one select answer. As for the system prompt, there was a little less control over the learning experience, given that the AI tutor could be so unreliable. In my opinion, the two processes did not compare at all. There were so many edits to be made with the system, whereas the frames were a one-and-done type of design.
```

### 2. Your tutor has hardcoded questions but generates responses dynamically. When is this an advantage over canned feedback? When is it a risk?

```
Generated responses are an advantage because they can be personalized to the user depending on their response. If the user was close to the answer but ultimately incorrect, the generated responses would adapt to this and give them a small hint they may need-- whereas the canned responses would be the same for every person and mostly consist of "you're right!" or "you're wrong and here's a random misconception". However, the generated responses can be very inconsistent. In our system alone, I found that the "AI tutor" would ask too many random questions, including asking the user for examples of a word they're supposed to be teaching the users. Also, the tutor would at times skip a question or stray away from the topic at hand, giving their own random fun facts and information that was irrelevant. The biggest issue, however, is that in our first attempt, the responses from the AI tutor were so long that you had to scroll through them, and once we put a word limit, they became extremely brief and one-worded. It was extremely hard to try to balance this, and in the end, we chose to be a bit brief over wordy. 
```

### 3. What tutoring strategy did you choose, and why? If you could redesign it, what would you change based on testing?

```
We chose to take a straight-to-the-point (but still kind) tutoring strategy. This was chosen in part because of the issues with the wordiness of the tutor, but also because we found it simpler to understand something when the questions and responses were shorter. If I could redesign it, I would make it so that there is a bit more encouragement and context from the tutor. But it was hard to get context from the tutor without having it spout out off-topic information. In the future, with knowledge on how to be more specific with commands, I would like to fix this.
```

### 4. Skinner insisted on a low error rate and immediate, predictable reinforcement. Your LLM tutor is neither predictable nor error-free. Is that a problem? For whom?

```
The unpredictable nature of the LLM tutor is very much a problem for users. If there is not enough testing done with the tutor, it is very possible that the user of the model could create a situation that had not been noted in testing before. This could create a major issue with the tutor, such as a change of topic, an endless loop, or a history refresh that could make the experience confusing and unpleasant for the user. 
```

### 5. A school wants to use your tutor with real students. Name three things you'd worry about.

```
1. Will the model be unresponsive to unique unreplicated inputs?
2. How will the students interact with the tutor? Will they change the topic unintentionally? 
3. Will this model actually teach them something new, or will they just use a transfer of knowledge to get the answers right in the moment, and then completely forget everything later? 
```

## Submission Checklist

- [ ] At least 5 educational questions with answers and misconceptions
- [ ] System prompt that defines the tutor's behavior
- [ ] Flask app with /chat route managing conversation history
- [ ] LiteLLM calls to a local Ollama model
- [ ] Working chat interface in the browser
- [ ] Tested with correct, incorrect, and edge-case inputs
- [ ] System prompt iterated at least once based on testing
- [ ] Reflection questions answered (above)
- [ ] Committed with meaningful commit messages
