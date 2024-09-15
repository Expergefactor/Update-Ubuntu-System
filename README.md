Version 9

![updating](https://github.com/Expergefactor/Update-Ubuntu-System/assets/133227259/a7209593-1a98-4962-bc63-4ebdeac7694d)

### DESCRIPTION
  Script to update your Ubuntu based system & to clear up afterwards.

  Automatic elevation to sudo if not run as sudo in first instance. 
  
  Progress of tasks is printed to Terminal with information such as volume of data processed, time elapsed & confirmation that the task completed (or not).

  Version 9 introduces an option to update the Snap Store application which is useful in instances when the Snap Store cannot be updated whilst it is open/running. 


### REQUIREMENTS
  Required for display of dynamic information on task progress...
  
    $ pip install tqdm

### HOW DO I USE IT?
  Place the update.py file in your home directory, open Terminal and use command,
  
    $ python3 update.py

### WHAT DOES IT DO?
  The script executes the following commands in sucession...
  
    $ sudo apt-get update
    $ sudo apt-get upgrade -y
    $ sudo apt-get dist-upgrade -y
    $ sudo apt autoremove -y
    $ sudo snap refresh

  If the Snap Store is to be updated, the following command will be executed...

    $ sudo pkill snap-store && sudo snap refresh snap-store

### TDQM ISSUE?

Try running:

    $ sudo apt install python3-tqdm
