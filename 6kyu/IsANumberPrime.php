function is_prime(int $n): bool {
  if ($n < 2)  return false;  
  if ($n == 2)  return true;
  
  $MCD = sqrt($n) + 1;
  for ($i = 2; $i < $MCD; $i++) {
       if ($n % $i === 0)  return false;
    }
  return true;
}
