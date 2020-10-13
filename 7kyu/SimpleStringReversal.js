function solve(str){
   const result = [...str.split(` `).join(``)];
  return str.replace(/\S/g, i => result.pop());
}
