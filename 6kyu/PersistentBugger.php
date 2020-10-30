function persistence(int $num): int {  
    $total = 1;
    $aux = str_split($num);
    $counter = 0;
  
    if (count($aux) > 1) {
        for ($i = 0; $i < count($aux); $i++) {
            $total *= $aux[$i];      
        }
        $counter++;
        if (strlen($total) > 1)  return $counter + persistence($total);
      return $counter;
    }
  return $counter;    
}
