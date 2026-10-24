# 🤖 Rule-Based AI Chatbot

A rule-based chatbot built as **Project 1** of the DecodeLabs AI Industrial Training Kit (Batch 2026).
It uses pure control flow and logic (no machine learning) to respond to predefined user inputs.

## 🔗 Live Demo
**Try it here:** https://YOUR_USERNAME.github.io/rule-based-ai-chatbot/

## ✨ Features
- Continuous loop that runs until the user types `bye`, `exit` or `quit`
- Input sanitization (lowercase, extra spaces, punctuation)
- Dictionary knowledge base with 50+ intents (greetings, AI/tech facts, jokes, small talk)
- Fallback reply for unknown inputs
- Two versions: Python terminal bot and web chat UI

## 🧠 How it works (IPO model)
| Phase | What happens |
|-------|--------------|
| **Input** | Raw text is cleaned with `.lower()`, `.strip()` and punctuation removal |
| **Process** | Exit words are checked, then the dictionary is searched (`.get()`) |
| **Output** | Matching reply, or a fallback message, is printed |

## ▶️ Run the Python version
```bash
python chatbot.py
```

## 💬 Example
```
You: Hello!
DecodeBot: Hi there! How can I help you today?
You: what is ai
DecodeBot: AI (Artificial Intelligence) is when machines do tasks that normally need human intelligence.
You: pizza
DecodeBot: Sorry, I do not understand. Type 'help' to see what I know.
You: bye
DecodeBot: Goodbye! Have a great day!
```

## 📁 Files
- `chatbot.py` – terminal chatbot (Python)
- `index.html` – web version (live demo)

## 🛠 Skills used
Python, control flow (`while`, `if/else`, `break`), dictionaries, string handling, JavaScript basics.

## 🚀 Future improvements
Keyword matching, nested conditions, and semantic (vector) matching in Project 2.

---
Built during the DecodeLabs AI Internship.
