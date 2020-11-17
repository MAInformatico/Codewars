  const spinWords = str => {
    const array = str.split(" ");
    const reversearray = array.map(word => {
       return word.length >= 5 ? word.split("").reverse().join("") : word;
    })
  return reversearray.join(" ");
}
