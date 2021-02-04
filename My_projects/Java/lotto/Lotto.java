/*
 * Lotto.java
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

public class Lotto extends JFrame {
	// 1.sor létrehozása.
	JPanel row1 = new JPanel();
	ButtonGroup option = new ButtonGroup(); 
	JCheckBox quickpick = new JCheckBox("Quick Pick", false);
	JCheckBox personal = new JCheckBox("Personal", true);
	// 2.sor létrehozása.
	JPanel row2 = new JPanel();
	JLabel numbersLabel = new JLabel("Your picks: ", JLabel.RIGHT);
	JTextField[] numbers = new JTextField[6];
	JLabel winnersLabel = new JLabel("Winners: ", JLabel.RIGHT);
	JTextField[] winners = new JTextField[6];
	// 3.sor létrehozása.
	JPanel row3 = new JPanel();
	JButton stop = new JButton("Stop");
	JButton play = new JButton("Play");
	JButton reset = new JButton("Reset");
	// 4.sor létrehozása.
	JPanel row4 = new JPanel();
	JLabel got3Label = new JLabel("3 of 6: ", JLabel.RIGHT);
	JTextField got3 = new JTextField("0");
	JLabel got4Label = new JLabel("4 of 6: ", JLabel.RIGHT);
	JTextField got4 = new JTextField("0");
	JLabel got5Label = new JLabel("5 of 6: ", JLabel.RIGHT);
	JTextField got5 = new JTextField("0");
	JLabel got6Label = new JLabel("6 of 6: ", JLabel.RIGHT);
	JTextField got6 = new JTextField("0", 10);
	JLabel drawingsLabel = new JLabel("Drawings: ", JLabel.RIGHT);
	JTextField drawings = new JTextField("0");
	JLabel yearsLabel = new JLabel("Years: ", JLabel.RIGHT);
	JTextField years = new JTextField();
	
	public Lotto() {
		super("Lottó sorsolása");
		setSize(550, 270);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		// Az egész panel igazítás.
		GridLayout layout = new GridLayout(5, 1, 10, 10);
		setLayout(layout);
		// 1.sor hozzáadása, formázása.
		FlowLayout layout1 = new FlowLayout(FlowLayout.CENTER, 10, 10);
		option.add(quickpick);
		option.add(personal);
		row1.setLayout(layout1);
		row1.add(quickpick);
		row1.add(personal);
		// 1.sor megjelenítése.
		add(row1);
		// 2.sor hozzáadása, formázása.
		GridLayout layout2 = new GridLayout(2, 7, 10, 10);
		row2.setLayout(layout2);
		row2.add(numbersLabel);
		for (int i = 0; i < 6; i++) {
			numbers[i] = new JTextField();
			row2.add(numbers[i]);		
		}
		row2.add(winnersLabel);
		for (int i = 0; i < 6; i++) {
			winners[i] = new JTextField();
			row2.add(winners[i]);		
		}
		// 2.sor megjelenítése.
		add(row2);
		// 3.sor hozzáadása, formázása.
		FlowLayout layout3 = new FlowLayout(FlowLayout.CENTER, 10, 10);
		row3.setLayout(layout3);
		stop.setEnabled(false);
		row3.add(stop);
		row3.add(play);
		row3.add(reset);
		// 3.sor megjelenítése.
		add(row3);
		// 4.sor hozzáadása, formázása.
		GridLayout layout4 = new GridLayout(2, 3, 20, 10);
		row4.setLayout(layout4);
		row4.add(got3Label);
		got3.setEditable(false);
		row4.add(got3);
		row4.add(got4Label);
		got4.setEditable(false);
		row4.add(got4);
		row4.add(got5Label);
		got5.setEditable(false);
		row4.add(got5);
		row4.add(got6Label);
		got6.setEditable(false);
		row4.add(got6);
		row4.add(drawingsLabel);
		drawings.setEditable(false);
		row4.add(drawings);
		row4.add(yearsLabel);
		years.setEditable(false);
		row4.add(years);
		// 4.sor megjelenítése.
		add(row4);
		// Az egész panel megjelenítése.
		setVisible(true);
	}
	
	public static void main (String[] args) {
		Lotto lotto = new Lotto();
	}
}
