function add(a, b) {
  const al = a.length
  const bl = b.length
  const ml = Math.max(al, bl)

  let carry = 0, sum = ''

  for (let i = 1; i <= ml; i++) {
    let A = +a.charAt(al - i)
    let B = +b.charAt(bl - i)

    let t = carry + A + B
    carry = t/10 |0
    t %= 10

    sum = (i === ml && carry)
      ? carry*10 + t + sum
      : t + sum
  }
