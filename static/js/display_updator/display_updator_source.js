// Show the most liked sentences
function showMostlyLikedSentences() {
  $.ajax({
    type:'GET',
    url:'/mostly_liked_sentences',
    data:{
      'nb_sentence':sentences.length
    },
    success:function(response)
    {
      console.log("rsp", response);
      const elt = document.getElementById('param-cell');
      const memory = elt.innerHTML;
      elt.innerHTML = "";
      let liked_sentences = response.liked_sentences;

      for (var i = 0; i < liked_sentences.length; i++) {
        if (!document.getElementById(getSentenceId(i))) {
          let current_liked_sentence = liked_sentences[i];
          let current_sentence = current_liked_sentence.sentence;
          let current_nb_likes = current_liked_sentence.nb_likes;
          elt.innerHTML += GenerateSentence(current_sentence,  i, getSentenceImgId(i, true), false, current_nb_likes);
        }
      }
      elt.innerHTML += memory;
    }
  });
}

// Function wiche permises to change the word cloud's language atomatically on each refreshing
async function AutoLanguageUpdator() {
      while (continueUpdate) {
        for (language in LANGAGES) {
          if( ! continueUpdate) break;
          selected_language = LANGAGES[language];
          display_update();
          await sleep(WAITING_TIME);
        }
      }
}

// Updates the display part
async function display_update () {
  //Ongoing on healthfull basis

  if (!updateUngoing || previous_display != selected_display) {
    updateUngoing = true;

    if(selected_display == WORD_CLOUD) {
      previous_display = WORD_CLOUD;
      wordCloud_update();
    }

   updateUngoing = false;
  }
}
