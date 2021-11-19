# using flask as backend 
from flask import Flask, render_template, request
# using autocorrect module to get correct spelling  
from autocorrect import Speller

# setting the default language as english 
spell = Speller(lang='en')
# define flask 
app = Flask(__name__)

# home page 
@app.route('/')
def show_home():
    return render_template('index.html')

# to get the correct spelling using autocorrect 
@app.route('/get')
def show_result():
    userText = request.args.get('msg')
    correct = spell(userText)
    return str(correct)

if __name__ == '__main__':
    app.run(debug=True)