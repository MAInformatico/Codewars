function findOdd(A) {
  let result;
  const dictObject = {};
  
  A.forEach((iterator)=>{
    if (dictObject[iterator]){
      dictObject[iterator]++;
    }
    else{
      dictObject[iterator] = 1;
    }
    });
    
  for(let num in dictObject){
    if(dictObject[num] % 2 != 0){
      result = num;
    }
  }
    
  return Number(result); //convert a js variable to number
}
