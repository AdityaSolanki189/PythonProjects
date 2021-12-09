from flask import Flask
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import jsonify

sid = SentimentIntensityAnalyzer()
app = Flask(name)

def analysis(input1): 
  output=sid.polarity_scores(input1)
  if output['compound']>0:
    return "positive",output
  elif output['compound']<0:
    return "negative",output
  else:
    return "neutral",output

@app.route("/")
def homepage():
    return "Api returns sentiment,compound,positive,negative,neutral"

@app.route('/<string:sentence>/')
def hello(sentence):
    analsed_sentence=analysis(sentence)
    return jsonify({"sentiment":analsed_sentence[0],"compound":analsed_sentence[1]['compound'],
    "positive":analsed_sentence[1]['pos'],"negative":analsed_sentence[1]['neg'],"neutral":analsed_sentence[1]['neu']})

if name == 'main':
    app.run()