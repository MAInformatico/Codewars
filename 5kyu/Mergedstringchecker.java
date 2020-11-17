public class StringMerger {
    public static boolean isMerge(String s, String part1, String part2) {
      if (s.equals("")) {
  			return part1.equals("") && part2.equals("");
  		}
      else {
  			boolean merge1 = false, merge2 = false;
  			if (part1.length() > 0 && s.charAt(0) == part1.charAt(0))
  				merge1 = isMerge(s.substring(1), part1.substring(1), part2);
  			if (part2.length() > 0 && s.charAt(0) == part2.charAt(0))
  				merge2 = isMerge(s.substring(1), part1, part2.substring(1));
  			return merge1 || merge2;
  		}
    }
}
