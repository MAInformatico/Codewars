const Calculator = function() {
  this.evaluate = string => {
    let str = string.split(" ");
    while(str.length > 1){
      const multDiv = str.findIndex(x => x === "*" || x === "/");
      const i = multDiv === -1 ? str.findIndex(y => y === "+" || y === "-") : multDiv;
      const x = Number(str[i - 1]);
      const y = Number(str[i + 1]);
      const calc = str[i] === "/" ? x / y : str[i] === "*" ? x * y : str[i] === "-" ? x - y : x + y;
      str.splice(i - 1, 3, calc);
    }
    return Number(str[0]);
  };
};
