
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 
app = Flask(__name__)
 
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
 
@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/login.html")
def login():
	return render_template("login.html")

@app.route("/signup.html")
def signup():
	return render_template("signup.html")

 
@app.route("/get")
def getBotResponse():
    userText = request.args.get('msg')
    print("hai")
    return str(english_bot.get_response(userText))


 
if __name__ == "__main__":
    app.run()
