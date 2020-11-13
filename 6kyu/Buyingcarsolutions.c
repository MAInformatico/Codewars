#include <stdlib.h>

int* nbMonths(int startPriceOld, int startPriceNew, int savingperMonth, double percentLossByMonth) {
  int *result = malloc(2 * sizeof(int));
  if(!result) return NULL;
  
  int i = 0;
  double oldcar = startPriceOld;
  double newcar = startPriceNew;
  int savings = 0;
  double loss = percentLossByMonth;
  while(1){
    double available = oldcar + savings;
    if (available >= newcar){
      result[0] = i;
      result[1] = round(available - newcar);
      return result;
    }
    oldcar *= (100.0 - loss) / 100.0;
    newcar *= (100.0 - loss) / 100.0;
    savings += savingperMonth;    
    if(i++ % 2 == 0) loss += 0.5;
  }  
}
