from flask import jsonify

sample_sentences = ['Premiere Phrase', "ceci est la seconde phrase", "ho une troisieme", "petite 4eme au passage", "Puis une 5eme", "enfin une sixieme"]

ENGLISH = "eng"
FRENCH = "fr"
ESPAGNOL = "esp"
ARAB = "ara"

LANGUAGES = [ENGLISH, FRENCH, ESPAGNOL, ARAB]

sentence_like = {ENGLISH:{0:5, 5:2}, FRENCH:{1:5, 5:2}, ESPAGNOL:{3:5, 5:2}, ARAB:{4:5, 5:2}}



def LikeSentence(request):
    num_sentence = int(request.form.get('nb_sentence'))
    lang = request.form.get('lang')
    try:
        sentence_like[lang][num_sentence]+=1
    except KeyError:
        sentence_like[lang][num_sentence]=1
    print(sentence_like)

def UnlikeSentence(request):
    num_sentence = int(request.form.get('nb_sentence'))
    lang = request.form.get('lang')
    sentence_like[lang][num_sentence]-=1
    print(sentence_like)




# returns the most liked sentence for each language
#{
# 'liked_sentences':
# {
#  "language name" :
#  {
#      "sentence" : "the most liked sentence"
#      "nb_likes" : likes_nuber
#  }
# }
#}
def Mostly_liked_sentences():
    result = {}
    for language in LANGUAGES:
        sentence_key_memory = -1
        sentence_like_memory = -1
        print(sentence_like)
        for sentence_key in sentence_like[language].keys():
            if (sentence_like[language][sentence_key] > sentence_like_memory):
                sentence_like_memory = sentence_like[language][sentence_key]
                sentence_key_memory = sentence_key

        # end for
        result[language] = {"sentence": sample_sentences[sentence_key_memory], "nb_likes": sentence_like_memory}

    result = {'liked_sentences': result}
    print("end of confrence :", result)
    return jsonify(result)


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
