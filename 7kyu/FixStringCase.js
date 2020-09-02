function solve(s){
    let upperL=s.split('').filter(v=>v.match(/[A-Z]/)).length
    let lowerL=s.split('').filter(v=>v.match(/[a-z]/)).length
    return lowerL>=upperL?s.toLowerCase():s.toUpperCase();
}
