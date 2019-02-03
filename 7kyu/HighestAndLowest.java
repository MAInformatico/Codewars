public class Kata {
  public static String HighAndLow(String numbers) {
    String[] parts= numbers.split(" ");
    int max=-1;
    int min=1;
    String result;
    String aux2;
    int l=parts.length;
    int[] aux= new int[l];
    for(int i=0;i<parts.length;i++){
      aux[i]= Integer.parseInt(parts[i]);
      if(max<aux[i]){
        max=aux[i];
      }
      if(min>aux[i]){
        min=aux[i];
      }
      if(parts.length==1){
        max=min=aux[i];
      }      
    }
    result= Integer.toString(max);
    aux2= Integer.toString(min);
    result+=" " + aux2;    
    return result;
  }
}
