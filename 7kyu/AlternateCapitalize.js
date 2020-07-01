function capitalize(s){
  return [s.split("").map((aux, i) => i % 2 === 0 ? aux.toUpperCase() : aux).join(""),
          s.split("").map((aux, i) => i % 2 !== 0 ? aux.toUpperCase() : aux).join("")];
};
