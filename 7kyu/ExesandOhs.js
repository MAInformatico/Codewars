function XO(str) {
  let result = false;
  let X = 0;
  let O = 0;
    for (var i = 0; i < str.length; i++) {
      if (str[i] === 'x' || str[i] === 'X') X++;
      if (str[i] === 'o' || str[i] === 'O') O++;      
    }
  if (X===O) result=true;
  return result;
}
