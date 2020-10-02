function mxdiflg($a1, $a2) {
    if (empty($a1) || empty($a2)) { return -1; }
  
    $Mapa1 = array_map('strlen', $a1);  
    $Mapa2 = array_map('strlen', $a2);        
    return max(abs(min($Mapa2) - max($Mapa1)), abs(max($Mapa2)-min($Mapa1)));
}
