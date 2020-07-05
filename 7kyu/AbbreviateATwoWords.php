function abbrevName($name){
  $aux = explode(" ", $name);
  $result = strtoupper($aux[0][0]).".".strtoupper($aux[1][0]);
  return $result;
}
