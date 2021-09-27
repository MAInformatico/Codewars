var largestDifference = function(data) {
  const arrayLen = data.length
  let difference = 0
  for (let i=0; i<arrayLen; i++){
    for (let j=i+1; j<arrayLen; j++){
      data[i]<=data[j] ? (j-i) > difference ? difference = j-i : undefined : undefined
    }
  }
  return difference;
};
