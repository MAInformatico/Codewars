package kata

func HasUniqueChar (str string) bool {
  
  var local = map[rune]bool{}
	
  for _, i := range str {
		local[i] = true
	}
  
	return len(local) == len(str)
}
