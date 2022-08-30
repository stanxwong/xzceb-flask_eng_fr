from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(english_text):
    """
    high level support for doing this and that.
    """
    french_text = language_translator.translate(\
    text=english_text,
    model_id='en-fr').get_result()
    return french_text

@app.route("/frenchToEnglish")
 def french_to_english(french_Text):
    """
    high level support for doing this and that.
    """
    english_text = language_translator.translate(\
    text=french_text,
    model_id='en-fr').get_result()
    return english_text   

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
