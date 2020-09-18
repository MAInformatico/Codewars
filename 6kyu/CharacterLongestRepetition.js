function longestRepetition(s) {
  let character='';
  let counter=1;
  let arr = [];
  for (let i=0;i<s.length;i++){
    if (s[i]===s[i+1]) counter++;
    
    else{
      if (arr.every(v=>v<counter)) character=s[i]+counter;
      
      arr.push(counter);
      counter=1;
    }
  }
  return !character?['',0]:[character.slice(0,1),character.slice(1)*1];
}
