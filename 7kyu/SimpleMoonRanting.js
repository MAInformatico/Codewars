function moonRating(rating) {
  let v=Math.round(rating);
  let result = ['xxxxx','cxxxx','oxxxx','ocxxx','ooxxx','oocxx','oooxx','ooocx','oooox','ooooc','ooooo'];
  return result[v];  
}
