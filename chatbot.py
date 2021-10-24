from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(name='Gop', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.TimeLogicAdapter',
                                 'chatterbot.logic.BestMatch',
                                 {'import_path': 'chatterbot.logic.BestMatch',
                                  'default_response': 'I am sorry, but I do not understand. I am still learning.',
                                  'maximum_similarity_threshold': 0.90
                                 }],
                 storage_adapter="chatterbot.storage.SQLStorageAdapter",
                 database="botData.sqlite3")

greetings     = open('/Users/gop/DataLab/PortfolioProject/Chatbot/ChatBot_Flask/training_data/greetings.txt').read().splitlines()
career_talk   = open('/Users/gop/DataLab/PortfolioProject/Chatbot/ChatBot_Flask/training_data/career.txt').read().splitlines()
about_bot     = open('/Users/gop/DataLab/PortfolioProject/Chatbot/ChatBot_Flask/training_data/about_bot.txt').read().splitlines()
training_data = greetings + career_talk + about_bot

trainer = ListTrainer(chatbot)
trainer.train(training_data) 

#list_trainer = ListTrainer(chatbot)
#for item in (chit_chat, career_chat):
    #list_trainer.train(item)

#from chatterbot.trainers import ChatterBotCorpusTrainer
#corpus_trainer = ChatterBotCorpusTrainer(chatbot)
#corpus_trainer.train('chatterbot.corpus.english.emotion')
                   
                   