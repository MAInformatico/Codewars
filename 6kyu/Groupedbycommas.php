function groupByCommas($n) {
  $result = $n;
  return number_format($n, $decimals = 0 , $dec_point = '.' , $thousands_sep = ',' );
}
