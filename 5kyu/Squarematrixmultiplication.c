#include <stdio.h>
#include <stdlib.h>

int **matrix_multiplication(int **a, int **b, int n) {
  // TODO: Return the result of A × B in the form of an n × n matrix
  // NOTE: Please use dynamic memory allocation to construct your
  // matrix as the test cases will `free` the memory from your
  // returned result afterwards
  int **result;
  result = (int **)malloc (n*sizeof(int *));  
  for (int i=0;i<n;i++)
  result[i] = (int *) malloc (n*sizeof(int));
  
  int i, j, k;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            result[i][j] = 0;
            for (k = 0; k < n; k++)
                result[i][j] += a[i][k] * b[k][j];
        }
    }
  return result;   
}
