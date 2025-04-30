import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!",]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot. You can call me Chatty.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thanks for asking!",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!",]
    ],
]

def simple_chatbot():
    print("Hi, I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    simple_chatbot()
