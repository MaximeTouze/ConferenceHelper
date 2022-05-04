function getValFromFormName(name) {
  var e = document.getElementsByName(name)[0];
  return e.value;
}

function getValFromRoomForm () {
  return getValFromFormName("room");
}

function getValFromLangForm () {
  return getValFromFormName("lang");
}
