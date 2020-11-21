let validISBN10 = function(isbn) {
    if(!/[0-9]{9}[0-9X]/.test(isbn)) { return false; }
    isbn = isbn.split("").map((v,iter) => ((v==="X") ? 10 : v) *(iter+1));
    return isbn.reduce((x,y)=>x+y) % 11 === 0;
}
