# Import necessary modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create chatbot instance
chatbot = ChatBot('corona bot')

# Train using built-in English corpus (greetings & conversations)
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

# Train with small custom data
custom_trainer = ListTrainer(chatbot)
custom_trainer.train([
    "What is your number?",
    "Sorry, I can't share personal information.",
    "Who are you?",
    "I am Corona Bot, your friendly assistant."
])

# Get responses from the bot
response = chatbot.get_response('What is your Number')
print(response)

response = chatbot.get_response('Who are you?')
print(response)
