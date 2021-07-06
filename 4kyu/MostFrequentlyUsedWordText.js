function topThreeWords(text) {
  const cleanText = text.replace(/[\.,-\/#!$%\^&\*;:{}=\-_`~()]/g,"").toLowerCase(),
  words = cleanText.match(/\S+/g) || [],
  counts = {};      
  let word, frequency;
  
  for(let i=0; i<words.length; i++ ) {
    if (words[i].match(/^[\\']+$/)){
        word = []; 
    }
    else {
      word = words[i];
      counts[word] = counts[word] || 0;
      counts[word]++;
    }
  }
  
  frequency = Object.keys(counts);

  return frequency.sort(function (x,y) { return counts[y] - counts[x];}).slice(0, 3);    
}
