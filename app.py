from flask import Flask, render_template, request
import my_python.word_cloud_generation.word_cloud_generation as word_cloud_generation
import my_python.translation.translation as translation
from urllib.request import urlretrieve

app = Flask(__name__, template_folder='templates')
app.debug = True

## The app's html view ::

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/test')
def test():
    return render_template('test.html')


## The app's solution

@app.route("/update", methods=['POST'])
def update():

    print(request.form);
    text = request.form['text']
    language = request.form['lang']
    word_cloud_generation.getCloudFromTextAndLanguage(text, language)
    return render_template('record.html')


@app.route("/updateSound", methods=['POST'])
def updateSound():
    wav_url = request.form.get('url')
    print(wav_url)
    urlretrieve(wav_url)
    #word_cloud_generation.getCloudFromTextAndLanguage(text, language)
    return render_template('test.html')

@app.route("/translate", methods=['POST'])
def translate():
    #translation.translate_text("hi")
    print(request.form.get('text'))
    return render_template('record.html')
