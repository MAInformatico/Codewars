#include <stdbool.h>

bool validParentheses(const char *str_in) {
  int n = 0;
  for (int i = 0; str_in[i] != '\0'; i++) {
    if (str_in[i] == '(') n++;
    if (str_in[i] == ')') n--;
    if (n < 0) return false;
  }  
  return n == 0;
}
