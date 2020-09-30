function createPhoneNumber(numbers){
 var result = "(xxx) xxx-xxxx";  
  for(var i = 0; i < numbers.length; i++) result = result.replace('x', numbers[i]);  
  return result; 
}
