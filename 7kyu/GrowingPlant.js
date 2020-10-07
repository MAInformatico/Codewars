function growingPlant(upSpeed, downSpeed, desiredHeight) {
  let current=0;
  for(var i=1;;i++){
    current+=upSpeed;
    if(current>=desiredHeight) break;
    else{
      current-=downSpeed;
    }
  }  
  return i;  
}
