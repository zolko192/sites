import javax.swing.*;
import java.awt.event.*;

public class LottoEvent implements ActionListener, ItemListener, Runnable {
	Lotto gui;
	Thread playing;
	
	public LottoEvent(Lotto in) {
		gui = in;
	}
	
	public void actionPerformed(ActionEvent event) {
		String command = event.getActionCommand();
		if (command == "Play") {
			startPlaying();
		}
		if (command == "Stop") {
			stopPlaying();
		}
		if (command == "Reset") {
			clearAllFields();
		}
	}
}
