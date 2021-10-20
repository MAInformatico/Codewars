public class Solution {
    public static String lcs(String x, String y) {
        if(x.length()<y.length()){
          String z = x;
          x = y;
          y = z;
        }
        String result = "";
        for(int i = 0; i<y.length(); i++){
          StringBuilder auxStr = new StringBuilder();
          int aux = x.indexOf(y.charAt(i));
          if(aux == -1){
            continue;
          }
          else{
            auxStr.append(y.charAt(i));
            x = x.substring(aux);
            for(int j = i+1; j<y.length(); j++){
              aux = x.indexOf(y.charAt(j));
              if(aux == -1){
                continue;
              }
              else{
                auxStr.append(y.charAt(j));
                x = x.substring(aux);
              }
            }            
          }                   
          if(auxStr.length()>result.length()){
            result = auxStr.toString();      
          }
    }
    return result;
    }
}
