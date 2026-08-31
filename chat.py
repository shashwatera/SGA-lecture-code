from nltk.chat.util import Chat, reflections

pairs = [
    [r"hello|hi|hey|what's up|yo", ["Hello, how are you today?"]],
    [r"(.*) pizza(.*)", ["Pizza costs $2."]],
    [r"(.*) time(.*)", ["The canteen is oepn 8AM to 6PM."]],
    [r"(.*) menu (.*)", ["Today's menu is Pizza and coffee."]],
    [r"(.*)", ["Sorry, I didn't understand."]]
]
custom_reflection = reflections.copy()
custom_reflection.update({
    "we": "you all",
    "ours": "yours",
    "us": "you",
    "are you": "am I",
    "can I": "can you",
    "will you": "will I"
})

chat = Chat(pairs, custom_reflection)
chat.converse()
