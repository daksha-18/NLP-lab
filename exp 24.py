def recognize_dialog_act(sentence):
    sentence = sentence.lower()
    
    if sentence.endswith("?"):
        return "Question"
    elif any(word in sentence for word in ["hello", "hi", "hey"]):
        return "Greeting"
    elif any(word in sentence for word in ["thanks", "thank you"]):
        return "Thanking"
    elif any(word in sentence for word in ["please", "could you", "would you"]):
        return "Request"
    else:
        return "Statement"


conversation = [
    "Hello!",
    "How are you?",
    "Please send the report.",
    "I completed the task.",
    "Thank you!"
]

for sentence in conversation:
    print(f"{sentence} → {recognize_dialog_act(sentence)}")
