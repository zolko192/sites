import java.util.*;

class Clock {
	public static void main(String[] args) {
		timer();
	}
	
	public static void timer() {
		// Az aktuális idő és dátum megállapítása.
		Calendar now = Calendar.getInstance();
		int hour = now.get(Calendar.HOUR_OF_DAY);
		int minute = now.get(Calendar.MINUTE);
		int second = now.get(Calendar.SECOND);
		int year = now.get(Calendar.YEAR);
		int month = now.get(Calendar.MONTH) + 1;
		int day = now.get(Calendar.DAY_OF_MONTH);
		
		// Aktuális dátum kiírása.
		System.out.print(year + ".");
		switch (month) {
			case 1:
				System.out.print("Január");
				break;
			case 2:
				System.out.print("Február");
				break;
			case 3:
				System.out.print("Március");
				break;
			case 4:
				System.out.print("Április");
				break;
			case 5:
				System.out.print("Május");
				break;
			case 6:
				System.out.print("Június");
				break;
			case 7:
				System.out.print("Július");
				break;
			case 8:
				System.out.print("Augusztus");
				break;
			case 9:
				System.out.print("Szeptember");
				break;
			case 10:
				System.out.print("Octóber");
				break;
			case 11:
				System.out.print("November");
				break;
			case 12:
				System.out.print("December");
				break;
			default:
				System.out.print("Nem található megfelelő hónap");
				break;
			}
		if (day < 10) {
			System.out.println(".0" + day);
		}
		else {
			System.out.print("." + day);
		}
			
		// Az aktuális idő kiírása.
		System.out.print(hour + ":");
		if (minute == 0) {
			System.out.print("0" + minute);
		}
		else if (minute < 10) {
			System.out.print("0" + minute);
		}
		else if (minute < 60) {
			System.out.print("" + minute);
		}
		System.out.print(":");
		if (second == 0) {
			System.out.print("0" + second);
		}
		else if (second < 10) {
			System.out.print("0" + second);
		}
		else if (second < 60) {
			System.out.print("" + second);
		}
		String[] ids = TimeZone.getAvailableIDs();
		for (int i = 0; i < ids.length; i++) {
			System.out.println(ids[i].toString());
		}
	}
}
