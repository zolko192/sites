#!/usr/bin/env python3.8
# zene.py
# __author__ = Horváth Zoltán

from pygame import mixer 
  
# Starting the mixer 
mixer.init(); 
	
def eleresi_ut():
	bekeres = str(input("Kérem írja be az elérési útját: "));
	if bekeres[0] == "~":
		szoveg = "/home/john31";
		if bekeres[1] == "/":
			szoveg += bekeres;
			uj = ("{0}{1}".format(szoveg[0:12], szoveg[13:200]));
			return uj;

# Loading the song
mixer.music.load(eleresi_ut());
  
# Setting the volume 
mixer.music.set_volume(0.1); 
  
# Start playing the song 
mixer.music.play(); 
  
# infinite loop 
while True: 
      
    print("Press 'p' to pause, 'r' to resume"); 
    print("Press 'e' to exit the program"); 
    query = input(""); 
      
    if query == 'p': 
  
        # Pausing the music 
        mixer.music.pause();      
    elif query == 'r': 
  
        # Resuming the music 
        mixer.music.unpause();
     
    elif query == 'e': 
  
        # Stop the mixer 
        mixer.music.stop(); 
        break;
