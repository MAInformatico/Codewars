#include<cmath>

bool is_square(long int n){  
  double ent, v=sqrt(n);
  double dec=modf(v,&ent);
  return dec==0 ? true : false;
}

long int findNextSquare(long int sq) {
 bool ps=is_square(sq);
 if(ps==false) return -1;
 else{
   int v=sqrt(sq);
   v++;
   return pow(v,2);
 }
}
