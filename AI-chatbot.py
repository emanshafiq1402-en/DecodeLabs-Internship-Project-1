"""
Project 1: Rule-Based AI Chatbot (DecodeLabs)
Concepts: input loop, sanitization, dictionary knowledge base,
          fallback response, clean exit.
"""

# KNOWLEDGE BASE: dictionary of intents (key = what user says, value = reply)
responses = {
    # Greetings
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What's up?",
    "good morning": "Good morning! Hope you have a productive day.",
    "good afternoon": "Good afternoon! How's your day going?",
    "good evening": "Good evening! How was your day?",
    "good night": "Good night! Sleep well.",
    "whats up": "Just waiting to chat with you!",
    "sup": "All good here! What about you?",

    # About the bot
    "how are you": "I'm just a bot, but I'm running perfectly!",
    "what is your name": "I'm DecodeBot, your first rule-based chatbot.",
    "who are you": "I'm DecodeBot, a rule-based AI chatbot.",
    "who made you": "I was built by an AI intern at DecodeLabs.",
    "are you human": "Nope, I'm a program made of if-else logic and a dictionary.",
    "are you a robot": "Yes, a simple rule-based one!",
    "how old are you": "I was created today, so I'm brand new!",
    "where do you live": "Inside your computer, in a Python file.",
    "what can you do": "I can chat about basic things. Type 'help' to see examples.",
    "help": "Try: hello, how are you, what is your name, joke, fun fact, motivate me, what is ai, what is python, thanks, or bye.",

    # AI and tech knowledge
    "what is ai": "AI (Artificial Intelligence) is when machines do tasks that normally need human intelligence.",
    "what is python": "Python is a beginner-friendly programming language used a lot in AI.",
    "what is a chatbot": "A chatbot is a program that talks with users through text or voice.",
    "what is machine learning": "Machine learning is when computers learn patterns from data instead of fixed rules.",
    "what is rule based": "Rule-based means the bot follows fixed if-else rules written by a programmer.",
    "what is a dictionary": "In Python, a dictionary stores key-value pairs, like 'hello': 'Hi there!'.",
    "what is a loop": "A loop repeats code again and again until a condition stops it.",
    "what is github": "GitHub is a website where developers store and share their code.",
    "what is decodelabs": "DecodeLabs is the platform where I was built as an internship project.",

    # Fun
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "another joke": "Why did the developer go broke? Because he used up all his cache!",
    "fun fact": "The first computer bug was a real moth found inside a computer in 1947.",
    "motivate me": "Every expert was once a beginner. Keep building!",
    "tell me something": "Python is named after Monty Python, not the snake!",
    "i am bored": "Let's fix that! Ask me for a joke or a fun fact.",
    "i am sad": "I'm sorry to hear that. Take a deep breath, things will get better.",
    "i am happy": "That's awesome! Keep smiling!",
    "i love you": "Aww, thank you! I'm just a bot, but you're great.",
    "i am hungry": "Go grab a snack, then come back and code more!",

    # Polite replies
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "ok": "Alright!",
    "okay": "Cool!",
    "nice": "Glad you like it!",
    "cool": "Thanks!",
    "sorry": "No problem at all!",
    "yes": "Great!",
    "no": "Okay, no worries.",
    "lol": "Haha, glad you're having fun!",
}

# Words that stop the bot
EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye", "see you", "stop"}


def sanitize(text):
    """Phase 1: clean raw input -> lowercase, no extra spaces, no punctuation."""
    text = text.lower().strip()
    for ch in "!?.,'":
        text = text.replace(ch, "")
    return " ".join(text.split())  # fixes double spaces inside the sentence


def main():
    print("DecodeBot: Hello! Type 'help' to see what I can do. Type 'bye' to exit.")

    # THE HEARTBEAT: continuous loop
    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize(raw_input_text)

        # Ignore empty input
        if clean_input == "":
            print("DecodeBot: Please type something.")
            continue

        # EXIT STRATEGY
        if clean_input in EXIT_COMMANDS:
            print("DecodeBot: Goodbye! Have a great day!")
            break

        # LOOKUP + FALLBACK in one step using .get()
        reply = responses.get(clean_input, "Sorry, I do not understand. Type 'help' to see what I know.")
        print("DecodeBot:", reply)


if __name__ == "__main__":
    main()