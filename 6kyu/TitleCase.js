const capitalizeFirstLetter = word =>
  `${word.slice(0, 1).toUpperCase()}${word.slice(1).toLowerCase()}`

function titleCase(title, minorWords = '') {
  const lowercaseArray = minorWords.toLowerCase().split(' ')
  const result = title.split(' ').map((word, i) => {
      if (i === 0) return capitalizeFirstLetter(word)

      return lowercaseArray.includes(word.toLowerCase())
        ? word.toLowerCase()
        : capitalizeFirstLetter(word)
    })
    .join(' ')

  return result
}
