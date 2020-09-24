function removeZeros(array) {
  // Sort "array" so that all elements with the value of zero are moved to the
  // end of the array, while the other elements maintain order.
  // [0, 1, 2, 0, 3] --> [1, 2, 3, 0, 0]
  // Zero elements also maintain order in which they occurred.
  // [0, "0", 1, 2, 3] --> [1, 2, 3, 0, "0"]
  
  // Do not use any temporary arrays or objects. Additionally, you're not able
  // to use any Array or Object prototype methods such as .shift(), .push(), etc
  
  // the correctly sorted array should be returned.
  for(var i = array.length; i >= 0; i--) {
    array = swap(i, array);
  }
  
  // the correctly sorted array should be returned.
  return array;
}

function isNull(value) {
   return value === 0 || value === '0';
}

function swap(i, array) {
  var Limit = array.length - 1;
  
  if(!isNull(array[i])) return array;
  
  while(i < Limit) {
    if(isNull(array[i + 1])) break;
    else {
      var aux = array[i];
      array[i] = array[++i];
      array[i] = aux;
    }
  }

  return array;
}
