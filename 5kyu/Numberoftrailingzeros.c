long zeros(long n) {
  long result = 0;
  for (long power = 5; n/power; power *= 5)
    result += n/power;
  return result;
}
