// Images extentions
const IMG_TYPE = 'png';
// Languages list
const LANGUAGES = ["eng", "fr", "esp", "ara"];
// Time before img update (ms)
const WAITING_TIME = 10000;
// Number max of sentences
const MAX_SENTENCES = 3;

//// Displays ::
const WORD_CLOUD = "word_cloud";
const SENTENCES = "sentences";

// The current language to show
let selected_language = "eng";
// the current display to show
let selected_display = WORD_CLOUD;

// the countor wich permises the display update (for pictures)
let compteur = 0;
// A boolean which permise to continue the update of the display
let continueUpdate = true;
