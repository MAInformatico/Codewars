namespace Triangle
{
  bool isTriangle(double a, double b, double c)
  {
    if(a<=0 || b<=0 || c<=0 ||a==b==c) return false;
    if(a+b>c && a+c>b && b+c>a) return true;
    else
      return false;
  }
};
