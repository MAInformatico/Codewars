function convertIP(ip) {
  return ip.split('.').reduce((sum, x)=> sum << 8 | x, 0) >>> 0;
}

function ipsBetween(start, end){
  return convertIP(end)-convertIP(start);
}
