function descendingOrder(n){
  if(n.length === 0) return n;
  else{
    n = n.toString();
    n = n.split('');
    n = n.sort();
    n = n.reverse();
    n = n.join('');
    n = Number(n);
  }
  return n;
}
