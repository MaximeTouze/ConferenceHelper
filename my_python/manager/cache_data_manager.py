# Manage the datas in cache


from my_python.const.lang_const import *

sample_sentences = ['Premiere Phrase', "ceci est la seconde phrase", "ho une troisieme", "petite 4eme au passage", "Puis une 5eme", "enfin une sixieme"]

displayed_sentences = {}

audio_memory = {}

sentences_rank = {}

sentences_limit = 5

audio_limit = 2

###
# Init

# Init the room
def initDisplayed_sentences_room(room):
    displayed_sentences[room] = {}
    sentences_rank[room] = -1
    for language in LANGUAGES:
        displayed_sentences[room][language] = []
    return

# Reset the room
def resetDisplayed_sentences_room(room):
    return initDisplayed_sentences_room(room)


def initAudio_memory():
    audio_memory = {}
    return

def resetAudio_memory_room(room):
    audio_memory[room] = []
    return

def resetCache_room(room):
    resetAudio_memory_room(room)
    resetDisplayed_sentences_room(room)

###
# Getters

# Returns all displayed sentences
def getDisplayed_sentences():
    return displayed_sentences

# Returns all displayed sentences of the room
def getDisplayed_sentences_room(room):
    return getDisplayed_sentences()[room]

# Returns all the displayed sentences of the room in the language
def getDisplayed_sentences_room_language(room, language):
    return getDisplayed_sentences_room(room)[language]

def getDisplayed_sentences_room_language_from(room, language, from_sent):
    # If customer have all or any sentence of the list, return the list
    if (sentences_rank[room] - form >= sentences_limit || sentences_rank[room] - form < 0):
        return displayed_sentences[room][language]

    # If customer already has some sentences of the list, return the rest of the list
    else:
        return displayed_sentences[room][language][sentences_rank[room] - from_sent:]


def getSound_memory():
    return audio_memory

def getSound_memory_room(room):
    return getSound_memory()[room]





###
# Setters

# Add [sentences] to the romm in the language displayed sentences list, returns the new list
def addDisplayed_sentences_room_language(room, language, sentences):
    sentences_rank[room] = sentences_rank[room] + len(sentences)
    displayed_sentences[room][language] = displayed_sentences[room][language][len(sentences)-1:] + sentences
    if (len(displayed_sentences[room][language]) > sentences_limit):
        displayed_sentences[room][language] = displayed_sentences[room][language][-sentences_limit:]
    return


def addSoundMemory(room, audioBuffer):
    # Prepare the buffer
    audioBuffer = re.sub(r'"\d*":', '', audioBuffer)
    #print(audioBuffer)
    buffer = audioBuffer.split(',')[2:-2]

    # keep in memory the new datas
    audio_memory.append(buffer)
    return

def removeExcess(room):
    if (len(audio_memory) > audio_limit):
        audio_memory[room] = getSound_memory_room(room)[(len(audio_memory)-audio_limit):]
    return
