function parse($data) {
  $result = [];
  $value = 0;
  for($i = 0; $i<strlen($data);$i++){
    if($data[$i]=="i") $value++;
    if($data[$i]=="d") $value--;
    if($data[$i]=="s") $value=pow($value,2);
    if($data[$i]=="o") array_push($result,$value);
  }  
  return $result;
}
