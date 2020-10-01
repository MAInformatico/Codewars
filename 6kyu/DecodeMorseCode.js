decodeMorse = function(morseCode){
  morseCode = morseCode.trim()
    let aux = morseCode.split('   ')
    let result = aux.map(word => word.split(' ').map(ch => MORSE_CODE[ch]))
    return result.map(word => word.join('')).join(' ')
}
