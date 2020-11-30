typedef unsigned long long ull;
ull perimeter(int n) {
  ull result = 0;
  ull t1 = 0;
  ull t2 = 1;
  ull nextTerm = 0;
  for (int i = 1; i <= n+2; ++i) {         //Fibonacci
        result = result + t1;
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
  }
  return result*4.0;
}
