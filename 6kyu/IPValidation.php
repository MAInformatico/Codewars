function isValidIP(string $str): bool{
    if (filter_var($str, FILTER_VALIDATE_IP)) return true;
    else {
      return false;
    }
}
