function square_sum($numbers) : int {
  for($i=0;$i<count($numbers);$i++){
    $numbers[$i]= pow($numbers[$i],2);
  }
  $result = array_sum($numbers);
  return $result;
}
