#include <vector>

using namespace std; 

int findSmallest(vector <int> list)
{
  int min=10000000;
   for(int i=0;i<list.size();i++){
     if(min>list[i]) min=list[i];
   }
  return min;
}
