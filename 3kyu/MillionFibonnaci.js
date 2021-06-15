//https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4
function fib(n) {
  if (n == 0|| n == 1){
    return BigInt(n);
  }
  else if (n >= 2 && n % 2 == 0){
    let x = n / 2;
    let fx = fib(x);
    return (2n * fib(x-1) + fx) * fx;
  }
  else if (n >= 2){
    let x = (n+1) / 2;
    let fx1 = fib(x - 1);
    let fx2 = fib(x);
    return fx2*fx2 + fx1*fx1;
  }
  else{
    a = 0n;
    b = 1n;
    for(let i = 0; i > n ; i--){
      [a,b] = [b - a, a];
    }
    return a;
  }     
}
