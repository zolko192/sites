/*
 * KeyView.java
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

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class KeyView extends JFrame implements KeyListener {
	JTextField keyText = new JTextField(60);
	JLabel keyLabel = new JLabel("Press any key in the text field.");
	
	KeyView() {
		super("KeyView");
		setSize(350, 100);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		keyText.addKeyListener(this);
		BorderLayout border = new BorderLayout();
		setLayout(border);
		add(keyLabel, BorderLayout.NORTH);
		add(keyText, BorderLayout.CENTER);
		setVisible(true);
	}
     
    public void keyTyped(KeyEvent input) {
        char key = input.getKeyChar();
        keyLabel.setText("You pressed " + key);
    }
     
    public void keyPressed(KeyEvent txt) {
        // Nem csinál semmit.
    }
     
    public void keyReleased(KeyEvent txt) {
        // Nem csinál semmit.
    }
	
	public static void main (String[] args) {
		KeyView keyview = new KeyView(); 
	}
}

