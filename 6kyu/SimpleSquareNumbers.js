function solve(n){
  let result = 1;
  while (result < n) {
    if ((Math.sqrt(((result * result) + n)) % 1) === 0)
      return result * result;
    result++;
  }
  return -1
  }
