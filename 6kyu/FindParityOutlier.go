package kata

func FindOutlier(integers []int) int {
  var aux = map[string][]int{
    "odd": []int{},
    "even": []int{},
  }
  for _, i := range integers {
    if i % 2 == 0 {
      aux["even"] = append(aux["even"], i)
    } else {
      aux["odd"] = append(aux["odd"], i)
    }
  }
  if len(aux["even"]) == 1 {
    return aux["even"][0]
  } 
  return aux["odd"][0]
}
