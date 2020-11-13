#include <string.h>

double arithmetic(double a, double b, char* operator) {
  float result = 0;
  if(strcmp(operator, "add") == 0 ) result = a + b;
  if(strcmp(operator,"subtract") == 0) result = a - b;
  if(strcmp(operator, "multiply") == 0) result = a * b;
  if(strcmp(operator, "divide") == 0) result = a / b;
  return result;
}
