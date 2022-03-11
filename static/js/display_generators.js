const GenerateImg = function (path, alt, style="") {
  return "<img style='" + style + "' src=\"" + path + "\" alt='" + alt + "'>";
}

const GenerateExposedImg = function (name) {
  return GenerateImg("../static/exposed/" + name, name, "weight:100%; height:100%");
}
