function pyramid(n) {
  return Array.from({length:n},(x,i)=>Array(i+1).fill(1));
}
