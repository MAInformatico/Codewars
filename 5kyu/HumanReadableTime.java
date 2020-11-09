public class HumanReadableTime {
  public static String makeReadable(int seconds) {
    int HourInSecs = 3600;
		int MinuteInSecs = 60;
		
		String h = Integer.toString((seconds / HourInSecs));
		String m = Integer.toString((seconds % HourInSecs) / MinuteInSecs);
		String secs = Integer.toString(seconds % MinuteInSecs);
		
		if (h.length() == 1)  h = "0" + h;
    
		if (m.length() == 1)  m = "0" + m;
		
		if (secs.length() == 1)  secs = "0" + secs;
				
		return h + ":" + m + ":" + secs;
  }
}
