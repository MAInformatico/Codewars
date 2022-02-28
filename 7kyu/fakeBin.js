function fakeBin(x){
  var result = '';
  for(var i = 0; i < x.length; i++){
    if(x[i] < '5') result += '0';
    else if(x[i] >= '5')result += '1';
  }
  return result;
}
