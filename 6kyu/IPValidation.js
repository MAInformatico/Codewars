function isValidIP(str) {
  var aux = str.split('.');
  if(aux.length == 4) {
    return validLen = aux.filter(function(v) {
      return v !== (+v).toString() ? false : v>=0 && v<=255 ? true : false;
    }).length == aux.length;
  }
  return false;
}
