function toCamelCase(str){
  return str.replace(/[_-]([a-z])/ig, (_, i) => i.toUpperCase());
}
