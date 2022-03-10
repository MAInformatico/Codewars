package kata

func Grow(arr []int) int{
  result := 1
  for i := range arr {
    result *= arr[i]
  }
  return result
}
