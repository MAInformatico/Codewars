function narcissistic(value) {
  const number = String(value).split('');
  let result = 0;

  for (i of number) {
    const aux = parseInt(i, 0);
    result += Math.pow(aux, number.length);
  }
  
  return result === value;
}
