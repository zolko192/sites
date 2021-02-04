/*
 * ClockPanel.java
 * 
 * Copyright 2020 john31 <john31@john31-Aspire-7735>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

import javax.swing.*;
import java.awt.*;
import java.util.*;

public class ClockPanel extends JPanel {
	
	public ClockPanel() {
		super();
		String currentTime = getTime();
		JLabel time = new JLabel("Time: ");
		JLabel current = new JLabel(currentTime);
		add(time);
		add(current);
	}
	
	String getTime() {
		String time;
		// Aktuális dátum és idő lekérdezése.
		Calendar now = Calendar.getInstance();
		int hour = now.get(Calendar.HOUR_OF_DAY);
		int minute = now.get(Calendar.MINUTE);
		int second = now.get(Calendar.SECOND);
		int year = now.get(Calendar.YEAR);
		int month = now.get(Calendar.MONTH) + 1;
		int day = now.get(Calendar.DAY_OF_MONTH);
		
		// Aktuális dátum és idő kiírása.
		String monthName = "";
		switch (month) {
			case 1:
				monthName = "Január";
				break;
			case 2:
				monthName = "Február";
				break;
			case 3:
				monthName = "Március";
				break;
			case 4:
				monthName = "Április";
				break;
			case 5:
				monthName = "Május";
				break;
			case 6:
				monthName = "Június";
				break;
			case 7:
				monthName = "Július";
				break;
			case 8:
				monthName = "Augusztus";
				break;
			case 9:
				monthName = "Szeptember";
				break;
			case 10:
				monthName = "Octóber";
				break;
			case 11:
				monthName = "November";
				break;
			case 12:
				monthName = "December";
				break;
			default:
				System.out.print("Nem sikerült beolvasni az aktuális hónap nevét!");
				break;
		}
		// A dátumok és idő kiegészítése.
		String days = "";
		if (day < 10) {
			days = "0" + day;
		}
		else {
			days = "" + day;
		}
		
		String minutes = "";
		if (minute == 0) {
			minutes = "0" + minute;
		}
		else if (minute < 10) {
			minutes = "0" + minute;
		}
		else if (minute < 60) {
			minutes = "" + minute;
		}
		
		String seconds = "";
		if (second == 0) {
			seconds = "0" + second;
		}
		else if (second < 10) {
			seconds = "0" + second;
		}
		else if (second < 60) {
			seconds = "" + second;
		}
		
		time = year + "." + monthName + "." + days + " " + hour + ":" + minutes + ":" + seconds;
		return time;
	}
}

