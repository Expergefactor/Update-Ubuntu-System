Version 1.1

![updating]([https://github.com/221702/Update/assets/133227259/fa26cef5-adaa-46eb-bf01-8d53677ec92f](https://github.com/Expergefactor/Update-Ubuntu-System/blob/main/img/updating.png))

### DESCRIPTION
  Simple script to update your system using Ubuntu's APT and to clear up afterwards.

### HOW DO I USE IT?
  Place the update.py file in your home directory, open Terminal and use command,
  
  $ python3 update.py

### WHAT DOES IT DO?
  The script runs the following commands...
  
    $ sudo apt-get update
    $ sudo apt-get upgrade -y
    $ sudo apt-get dist-upgrade -y
    $ sudo apt autoremove -y
