function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
}

let compteur = 0;

async function display_update () {
  compteur++;
  imgName = selected_display + '.' + selected_language + '.' + IMG_TYPE;
  document.getElementById('displayPanel').innerHTML = GenerateExposedImg(imgName + "?" + compteur);
}

async function Updator() {
      while (true) {
        console.log("called");
        display_update();
        await sleep(3000);
      }
}

Updator();
