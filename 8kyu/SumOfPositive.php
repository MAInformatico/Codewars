function positive_sum($arr) {
 $longitud = count($arr);
  for($i=0; $i<$longitud; $i++){
    if($arr[$i]>0){
	    $total+=$arr[$i];
    }  
  }
  return $total;
}
