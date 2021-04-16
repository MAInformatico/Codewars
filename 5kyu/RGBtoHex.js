function rgb(r, g, b){
  const toHex = function(color) {
    if(color < 0) {
      return '00';
    }
    if(color > 255) {
      return 'FF';
    }
    return (color > 15 ? color.toString(16) : '0' + color.toString(16)).toUpperCase();
  }
  return toHex(r) + toHex(g) + toHex(b); 
}
