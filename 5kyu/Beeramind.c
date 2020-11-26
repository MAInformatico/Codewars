#include <math.h>
// Returns number of complete beeramid levels
int beeramid(double bonus, double price) {
  double maxNumOfCans = bonus/price;
  int level = 0;
  double canSum = 0;
  if (bonus <= 0) return 0;
  while (canSum <= maxNumOfCans) {
     ++level;
     canSum += pow(level,2);     
  }
  return --level;  
}
