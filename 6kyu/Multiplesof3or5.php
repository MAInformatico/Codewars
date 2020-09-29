function solution($number){
  $found = 0;
  $i= 0;
  for ($i = 3; $i < $number; $i++ ) {
    if ( 0 === $i % 3 || 0 === $i % 5 ) {
      $found+=$i;
    }
  }
  return $found;
}
