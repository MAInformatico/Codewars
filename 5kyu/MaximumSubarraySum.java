public class Max {
  public static int sequence(int[] arr) {
    int max_so_far = 0, max_ending_here = 0; 
   for (int i = 0; i < arr.length; i++) { 
       max_ending_here = max_ending_here + arr[i]; 
       if (max_ending_here < 0) 
           max_ending_here = 0;   
       else if (max_so_far < max_ending_here) 
           max_so_far = max_ending_here; 
   } 
   return max_so_far;    
  }
}
