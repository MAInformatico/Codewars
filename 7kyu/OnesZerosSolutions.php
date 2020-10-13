function binaryArrayToNumber($arr) {
  $num = implode("','",$arr);
  $num.str_replace (",","",$arr);
  return bindec($num);
}
