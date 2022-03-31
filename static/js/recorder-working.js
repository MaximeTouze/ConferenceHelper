let isDisplayModOn = false;
let id_conf = 0;

const DEFAULT_DISPLAY_MOD_ON_VIEW = "Ceci est une premiere phrase de la transcription";

function StartConfrence () {
  console.log("starting confrence");
  id_conf ++;
  //setup micro
  console.warn("méthode mockée :: StartConfrence :: Micro setup");
  //changer l affichage
  ConferenceDisplayModOn();
}

function ConferenceDisplayModOn () {
  // Setup for view updating
  isDisplayModOn = true;
  continueUpdate = true;
  var elt = document.getElementById('param-cell');
  elt.innerHTML = ' <div id="text-lines"> Here some transcription sentences </div> <button type="button" name="to_confrence" onclick="EndConfrence();">End confrence</button>';
  AutoLanguageUpdator();
}

function EndConfrence () {
  // Microhone stops
  //...
  // Updating the viewing
  var elt = document.getElementById('param-cell');
  elt.innerHTML ='';
  showMostlyLikedSentences();
  elt.innerHTML += '<div id="text-lines"> Here some liked transcription sentences </div> <button type="button" name="to_confrence" onclick="SetupConfrence();">Set up next confrence</button>';
}

function SetupConfrence () {
  isDisplayModOn = false;
  continueUpdate = false;
  var elt = document.getElementById('grid-container');
  elt.innerHTML = ' <div class="grid-column-presenting"> <div id = "displayPanel" class="cell basic_color_cell display"> Display part </div> <div id="param-cell" class="cell basic_color_cell"> Spoken language slection <select name="lang"> <option valeur="eng">eng</option> <option valeur="fr">fr</option> <option valeur="ara">ara</option <option valeur="esp">esp</option> </select> Room slection <select name="romm"> <option valeur="1">1</option> <option valeur="2">2</option> <option valeur="3">3</option> </select> <button type="button" name="to_confrence" onclick="StartConfrence();">Start confrence</button> </div> </div> ';

}
