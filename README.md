Version 1.3

![updating](https://github.com/Expergefactor/Update-Ubuntu-System/assets/133227259/a7209593-1a98-4962-bc63-4ebdeac7694d)

### DESCRIPTION
  Script to update your Ubuntu based system & to clear up afterwards.
  Individual tasks are prevented from displaying on-screen and are replaced with a task progress bar to provide a cleaner appearance. 

### HOW DO I USE IT?
  Place the update.py file in your home directory, open Terminal and use command,
  
  $ python3 update.py

### WHAT DOES IT DO?
  The script runs the following commands in sucession...
  
    $ sudo apt-get update
    $ sudo apt-get upgrade -y
    $ sudo apt-get dist-upgrade -y
    $ sudo apt autoremove -y
    $ sudo snap refresh
