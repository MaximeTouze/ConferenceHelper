
from flask import Flask, render_template, request, jsonify
import my_python.word_cloud_generation.word_cloud_generation as word_cloud_generation
import my_python.translation.translation as translation
import my_python.transcription.transcription as transcription
from urllib.request import urlretrieve
import wave, struct
import json
import js2py
import re
import os as os

import my_python.api.likeSystem as likeSystem

sample_sentences = ['Premiere Phrase', "ceci est la seconde phrase", "ho une troisieme", "petite 4eme au passage", "Puis une 5eme", "enfin une sixieme"]
sentence_like = {0:5, 1:2}
app = Flask(__name__, template_folder='templates')
app.debug = True

audio_memory = []

#app.run(ssl_context="adhoc")

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

@app.route('/recorderLook')
def recorderLook():
    return render_template('RecorderFrontTesting.html')


## The app's solution

@app.route("/update", methods=['POST'])
def update():
    text = request.form['text']
    language = request.form['lang']
    word_cloud_generation.getCloudFromTextAndLanguage(text, language)
    return render_template('record.html')

@app.route("/updateSound2", methods=['POST'])
def updateSound2():
    #print('called', request.form)
    audioBuffer = request.form.get('audioBuffer')

    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")

    #print(audioBuffer)
    # Prepare wave file
    file_path = "current.wav"
    file = wave.open(file_path, "wb")
    file.setnchannels(1)
    sampleRate = 44100.0*2 # hertz
    file.setsampwidth(2)
    file.setframerate(sampleRate)
    try:
        print(";;;", audio_memory[0])
        print (";;;;", audio_memory[0][0])
    except:
        pass
    # Create the wave with the past memory
    for sound_part in audio_memory:
        for item in sound_part:
            file.writeframesraw( struct.pack('<h', int(item)) )

    # Prepare the buffer
    audioBuffer = re.sub(r'"\d*":', '', audioBuffer)
    #print(audioBuffer)
    buffer = audioBuffer.split(',')[2:-2]
    memory = []
    buffer = Clear(buffer)
    for sample in buffer:
        data = struct.pack('<h', int(sample))
        memory.append(sample)
        file.writeframesraw( struct.pack('<h', int(sample)) )

    # keep in memory the new datas
    audio_memory.append(buffer)

    print('============END===========')
    # Don t forgot to close
    file.close()
    #res_transcription = transcription.my_transcription(file_path)
    #print(res_transcription)
    #word_cloud_generation.getCloudFromTextAndLanguage(text, language)
    return render_template('test.html')



@app.route("/translate", methods=['POST'])
def translate():
    #translation.translate_text("hi")
    print(request.form.get('text'))
    return render_template('record.html')

@app.route("/sentences", methods=['GET'])
def sentences():
    num_sentence = int(request.args.get('nb_sentence'))
    if(num_sentence>=len(sample_sentences)):
        return jsonify({'sentences': []})
    return jsonify({'sentences': [sample_sentences[num_sentence]]})

@app.route("/likeSentence", methods=['POST'])
def LikeSentence():
    likeSystem.LikeSentence(request)
    return render_template('view.html')

@app.route("/UnlikeSentence", methods=['POST'])
def UnlikeSentence():
    likeSystem.UnlikeSentence(request)
    return render_template('view.html')

@app.route("/mostly_liked_sentences", methods=['GET'])
def Mostly_liked_sentences():
    return likeSystem.Mostly_liked_sentences()


def Clear(list):
    return [x for x in list if x != 0]

if __name__== '__main__':
    app.run()
