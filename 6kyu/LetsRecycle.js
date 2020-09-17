function recycle(array) {
  var result = [];
  for(var i=0; i<4; i++) {
    result[i] = new Array(0);
  }
  for (let i = 0; i<array.length;i++){
    if(array[i].material === 'paper' || array[i].secondMaterial === 'paper') result[0].push(array[i].type);
    if(array[i].material === 'glass' || array[i].secondMaterial === 'glass') result[1].push(array[i].type);
    if(array[i].material === 'organic' || array[i].secondMaterial === 'organic') result[2].push(array[i].type);    
    if(array[i].material === 'plastic' || array[i].secondMaterial === 'plastic') result[3].push(array[i].type);    
  }
  return result;
}
