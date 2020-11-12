#include <stddef.h>

size_t get_count(const char *s)
{
    int result = 0;
    for (int i = 0; s[i] != '\0'; i++) {   
        char ch = s[i];   
        if (ch == 'a' || ch == 'e'
            || ch == 'i' || ch == 'o'
            || ch == 'u' || ch == 'A'
            || ch == 'E' || ch == 'I'
            || ch == 'O' || ch == 'U') 
            result++;
      }
    return result;
}
