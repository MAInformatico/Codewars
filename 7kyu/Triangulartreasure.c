int triangular(int n) {
  int result = 0;
  if (n>0){
    result = n*(n+1)/2;
  }
  else{
    result = 0;
  }
  return result;
}
