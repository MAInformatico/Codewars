function sum(array $a): float {
  $result=0;
  if (sizeof($a) != 0){
    for($i=0;$i<sizeof($a);$i++){
      $result+=$a[$i];
    }
  }
  return $result;
}
