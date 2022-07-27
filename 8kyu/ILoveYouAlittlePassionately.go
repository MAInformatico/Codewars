package kata

func HowMuchILoveYou(i int) string {
  if i%6 == 1 {
    return "I love you"
  }else if i%6 == 2 {
    return "a little"
  }else if i%6 ==3 {
    return "a lot"
  }else if i%6 ==4 {
    return "passionately"
  }else if i%6 == 5 {
    return "madly"
  }else{
    return "not at all"
  }
}
