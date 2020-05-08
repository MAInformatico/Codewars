//Based on GeekforGeeks references
var Zero = "0".charCodeAt(0);

var findModulo = function(base, exponent) {
  var module = 0;
  for (var i in exponent) {
    module = (module * 10 + exponent.charCodeAt(i) - Zero) % base;
  }
  return module;
}

var lastDigit = function(str1, str2){

  if (str1.length === 1 && str2.length === 1 && str1 === "0" && str2 === "0") {
    return 0;
  }
  
  if (str2.length === 1 && str2 === "0") {
    return 1;
  }
  
  if (str1.length === 1 && str1 === "0") {
    return 0;
  }

  var exponent = findModulo(4, str2);
  if (exponent === 0) {
    exponent = 4;
  }

  var result = Math.pow(str1[str1.length - 1].charCodeAt(0) - Zero, exponent);
  
  // Return last digit of result
  return result % 10;
}
