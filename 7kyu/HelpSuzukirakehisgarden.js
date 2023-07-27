function rakeGarden(garden) {
  var result= garden.split(' ').map(value=>value=='rock'?'rock':'gravel').join(' ');  
  
  return result;
}
