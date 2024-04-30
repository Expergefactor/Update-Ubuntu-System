Version 1.2

![updating](https://github.com/Expergefactor/Update-Ubuntu-System/assets/133227259/a7209593-1a98-4962-bc63-4ebdeac7694d)

### DESCRIPTION
  Simple script to update your system using Ubuntu's APT and to clear up afterwards.

### HOW DO I USE IT?
  Place the update.py file in your home directory, open Terminal and use command,
  
  $ python3 update.py

### WHAT DOES IT DO?
  The script runs the following commands in sucession...
  
    $ sudo apt-get update
    $ sudo apt-get upgrade -y
    $ sudo apt-get dist-upgrade -y
    $ sudo apt autoremove -y
