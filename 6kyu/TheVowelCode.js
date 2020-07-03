function encode(string) {
  return (string.replace(/[aeiou]/g, function (i) { return '_aeiou'.indexOf(i) }));
}

function decode(str) {
 return (str.replace(/[1-5]/g, function (i) { return '_aeiou'.charAt(i) }));
}
