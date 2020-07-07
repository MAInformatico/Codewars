function going(n) {
    let result = 1, factorial = 1;
  for (let i = n; i > 1; i--) {
    factorial /= i;
    result += factorial;
  }
  return parseFloat(result.toString().substring(0, 8));
}
