from rasa.nlu.model import Interpreter

# Load trained model
interpreter = Interpreter.load("./models/nlu")

def process_text(text):
    result = interpreter.parse(text)
    intent = result['intent']['name']
    entities = result['entities']
    
    print(f"Intent: {intent}")
    print(f"Entities: {entities}")
    
    # Add your response logic here based on intent and entities
    if intent == "greet":
        return "Hello there! How can I help you?"
    elif intent == "goodbye":
        return "Goodbye! Have a nice day!"
    else:
        return "I'm not sure I understand. Can you rephrase that?"

# Test
print(process_text("Hello there"))
print(process_text("I want to book a flight to Paris"))
