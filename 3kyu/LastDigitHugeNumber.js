function trueModule(a, n, m) {
    return Math.round( (a % m) * Math.pow( (a % m), (n + 3) % 4 ) ) % m;
}

function lastDigit(as){
    if (as.length == 0) return 1;
    let isZero = false;
    let biggerThan2 = false;
    let mod4 = 1;
    for (let i = as.length - 1; i > 0; --i) {
        if (isZero) {
            mod4 = 1;
            isZero = false;
            biggerThan2 = false;
        } else {
            mod4 =(biggerThan2 && (as[i] % 4 === 2)) ? 0 : trueModule(as[i], mod4, 4);
            isZero = as[i] === 0;
            biggerThan2 = !isZero && !(as[i] === 1);
        }
    }
  
    return isZero ? 1 : trueModule(as[0], mod4, 10);
