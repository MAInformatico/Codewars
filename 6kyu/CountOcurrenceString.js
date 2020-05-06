function count (string) {  
   let dictcache={};
   string.split('').map(v=>dictcache[v]=dictcache[v]+1||1)
   return dictcache;
}
