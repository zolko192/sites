#!/bin/bash
chmod u+x clean.bash
yes | sudo rm -i /var/lib/dpkg/lock
yes | sudo rm -i /var/cache/apt/archives/lock
sudo apt-get -y clean
sudo apt-get -y autoclean
sudo apt-get -y remove
sudo apt-get -y autoremove
sudo apt-get -y update
sudo apt-get -y upgrade
if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
