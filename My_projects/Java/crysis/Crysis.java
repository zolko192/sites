/*
 * Crysis.java
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

public class Crysis extends JFrame {
	JButton btn1 = new JButton("Panic");
	JButton btn2 = new JButton("Don't Panic");
	JButton btn3 = new JButton("Blame Others");
	JButton btn4 = new JButton("Notify the Media");
	JButton btn5 = new JButton("Save Yourself");
	
	public Crysis() {
		super("Crysis");
		setSize(400, 300);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel panel = new JPanel();
		BoxLayout box = new BoxLayout(panel, BoxLayout.Y_AXIS);
		panel.setLayout(box);
		add(panel);
		panel.add(btn1);
		panel.add(btn2);
		panel.add(btn3);
		panel.add(btn4);
		panel.add(btn5);
		setVisible(true);
	}
	
	public static void main (String[] args) {
		Crysis crisis = new Crysis();
	}
}

