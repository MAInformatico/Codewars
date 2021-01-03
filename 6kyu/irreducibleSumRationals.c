#include <stdlib.h>

long long gcd(long long a, long long b){ //Euclides algorithm
  long long common = b;
  while(a%b!=0){
    common = a%b;
    a = b;
    b = common;
  }
  return common;
}

// row: number of rows of lst
int* sumFracts(int lst[][2], int row) {
    int *result = (int*)calloc(2,sizeof(int));
    result[1] = 1;
    if (row == 0) return result;
    long long sumDenominators = 1;
    long long sumNumerators = 0;
    for(int i = 0; i<row;i++) sumDenominators*=lst[i][1];
    for(int i = 0; i<row;i++) sumNumerators+=sumDenominators*lst[i][0]/lst[i][1];
    long long commonDenominator = gcd(sumNumerators,sumDenominators);
    result[0] =sumNumerators/commonDenominator;
    result[1] =sumDenominators/commonDenominator;
    return result;
}
