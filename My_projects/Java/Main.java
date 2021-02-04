/*
 * Main.java
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

import java.util.*;
import javax.swing.*;
import java.awt.*;
		
public class Main extends JFrame {
	
	public Main() {
		// A keretet létrehozó utasítások.
		super();
		setTitle("Próba!");
		setSize(800, 600);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
		FlowLayout btn = new FlowLayout();
		setLayout(btn);
		// Button gombok létrehozása.
		JButton playButton = new JButton("Play");
		JButton pauseButton = new JButton("Pause");
		JButton stopButton = new JButton("Stop");
		JButton exitButton = new JButton("Kilépés");
		add(playButton);
		add(pauseButton);
		add(stopButton);
		add(exitButton);
		// Címke és üres mező létrehozása.
		JLabel pageLabel = new JLabel("Web page address: ", JLabel.RIGHT);
		JTextField pageAddress = new JTextField(20);
		String choiceAddress = pageAddress.getText();
		JLabel pagePrinter = new JLabel(choiceAddress);
		FlowLayout flo = new FlowLayout();
		setLayout(flo);
		add(pageLabel);
		add(pageAddress);
		add(pagePrinter);
		setVisible(true);
		
	}
	
	public static void main(String[] args) {
		Main root = new Main();
	}
}
