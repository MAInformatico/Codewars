function chain(fns) {
  let Chain = function(val){
    this.execute = () => val;
  };
  for(let i in fns) Chain.prototype[i] = function (a, b) {
    let val = this.execute(),
        args = val === null ? [a, b] : [val, a];
    return new Chain(fns[i](...args));
  }
  return new Chain(null);
}
