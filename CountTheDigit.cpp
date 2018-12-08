#include <iostream>
#include <string>
#include <algorithm>
using namespace std; 

class CountDig{
public:
    static int nbDig(int n, int d);
};

int CountDig::nbDig(int n, int d){
    string strDigits;
    
    for (int k = 0; k <= n; ++k) {
      strDigits += to_string(k * k);
    }
  
    return count(strDigits.begin(), strDigits.end(), to_string(d)[0]);
}
