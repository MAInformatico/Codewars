#include <vector>
using namespace std;
vector<long long> pascalsTriangle(int n){
  vector<long long> result;
  long long c;
  for(long long i=0;i<n;i++){
        for(long long j=0;j<=i;j++){
            if (j==0||i==0){
                c=1;
                result.push_back(c);
            }
            else{
               c=c*(i-j+1)/j;
              result.push_back(c);
            }
        }
    }
  return result;
}
