#!/bin/bash

sudo chmod u+x error.bash

xfce4-panel --quit
pkill xfconfd
sudo rm -rf ~/.config/xfce4/panel
sudo rm -rf ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
xfce4-panel
