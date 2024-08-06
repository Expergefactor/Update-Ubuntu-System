Version 1.8

![updating](https://github.com/Expergefactor/Update-Ubuntu-System/assets/133227259/a7209593-1a98-4962-bc63-4ebdeac7694d)

### DESCRIPTION
  Script to update your Ubuntu based system & to clear up afterwards.

  Automatic elevation to sudo if not run as sudo in first instance. 
  
  Individual tasks are represented with a progress bar whcih counts completed tasks per function. When the function is complete, progress bar displays 100%. 


### REQUIREMENTS
  Required for display of progress bars.
  
    $ pip install tqdm

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

### TDQM ISSUE?

Try running:

    $ sudo apt install python3-tqdm
