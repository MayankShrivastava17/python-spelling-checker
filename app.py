from flask import Flask, render_template, request
from autocorrect import Speller

spell = Speller(lang='en')
app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('index.html')

@app.route('/get')
def show_result():
    userText = request.args.get('msg')
    correct = spell(userText)
    return str(correct)

if __name__ == '__main__':
    app.run(debug=True)
