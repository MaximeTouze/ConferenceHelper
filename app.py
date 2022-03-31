from flask import Flask, render_template, request, jsonify
import my_python.word_cloud_generation.word_cloud_generation as word_cloud_generation
import my_python.translation.translation as translation
import my_python.transcription.transcription as transcription
from urllib.request import urlretrieve
import wave, struct
import json
import js2py
import re

sample_sentences = ['Premiere Phrase', "ceci est la seconde phrase", "ho une troisieme", "petite 4eme au passage", "Puis une 5eme", "enfin une sixieme"]
sentence_like = {0:5, 1:2}
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


@app.route("/updateSound", methods=['POST'])
def updateSound():
    wav_url = request.form.get('url')
    print(wav_url)
    #urlretrieve(wav_url)
    #word_cloud_generation.getCloudFromTextAndLanguage(text, language)
    return render_template('test.html')

@app.route("/updateSound2", methods=['POST'])
def updateSound2():
    audioBuffer = request.form.get('audioBuffer')
    #print(audioBuffer)
    file_path = "current.wav"
    file = wave.open(file_path, "wb")
    file.setnchannels(1)
    sampleRate = 44100.0*2 # hertz
    file.setsampwidth(2)
    file.setframerate(sampleRate)

    audioBuffer = re.sub(r'"\d*":', '', audioBuffer)
    buffer = audioBuffer.split(',')[2:-2]
    for sample in buffer:
        data = struct.pack('<h', int(sample))
        file.writeframesraw( data )
    file.close()
    res_transcription = transcription.my_transcription(file_path)
    print(res_transcription)
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
def likeSentence():
    num_sentence = int(request.form.get('nb_sentence'))
    try:
        sentence_like[num_sentence]+=1
    except KeyError:
        sentence_like[num_sentence]=1
    print(sentence_like)
    return render_template('record.html')

@app.route("/UnlikeSentence", methods=['POST'])
def UnlikeSentence():
    num_sentence = int(request.form.get('nb_sentence'))
    sentence_like[num_sentence]-=1
    print(sentence_like)
    return render_template('record.html')

@app.route("/mostly_liked_sentences", methods=['GET'])
def Mostly_liked_sentences():
    sentences_rank_result = [0,0,0]
    # number of likes
    sentences_count_result = [0,0,0]

    #For on liked sentences only
    for rank in sentence_like.keys():
        # For on the ranks of the memory
        for count_result_rank in range(len(sentences_count_result)-1, -1, -1):
            if (sentence_like[rank] > sentences_count_result[count_result_rank]):
                (sentences_rank_result, sentences_count_result) = MoveDownValues(sentences_rank_result, sentences_count_result, count_result_rank)
                #Set up the new values
                sentences_count_result[count_result_rank] = sentence_like[rank]
                sentences_rank_result[count_result_rank] = rank
                break

    #Once sentences_rank_result & sentences_count_result have the good values ::
    #For each sentence add to result a dictionary as :
    # {
    #  "sentence" : "the liked sentence"
    #  "nb_likes" : likes_nuber
    # }
    result = [{"sentence": sample_sentences[sentences_rank_result[rank]], "nb_likes":sentences_count_result[rank]} for rank in range(0, len(sentences_count_result))]
    return jsonify({'liked_sentences': result})


# Place the tab rank value to the tab rank-1
# WARN Does not change the given rank value, you have to do it
def MoveDownValues(sentences_rank_result, sentences_count_result, count_result_rank):
    if (count_result_rank < 1):
        return (sentences_rank_result, sentences_count_result)
    else :
        (new_sentences_rank_result, new_sentences_count_result) = MoveDownValues(sentences_rank_result, sentences_count_result, count_result_rank-1)
        new_sentences_rank_result[count_result_rank-1] = new_sentences_rank_result[count_result_rank]
        new_sentences_count_result[count_result_rank-1] = new_sentences_count_result[count_result_rank]
        return (new_sentences_rank_result, new_sentences_count_result)
