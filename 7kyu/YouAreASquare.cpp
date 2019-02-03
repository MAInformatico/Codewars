#include<cmath>
using namespace std;

bool is_square(int n){  
  double ent, v=sqrt(n);
  double dec=modf(v,&ent);
  return dec==0 ? true : false;
}
