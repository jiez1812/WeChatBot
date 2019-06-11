from WeChatBot import bot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

corpus_train = ChatterBotCorpusTrainer(bot)

corpus_train.train("chatterbot.corpus.chinese")
corpus_train.train("chatterbot.corpus.chinese.greetings")
corpus_train.train("chatterbot.corpus.chinese.conversations")