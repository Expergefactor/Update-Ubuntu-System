import os
import subprocess

# Define the commands to run
commands = [
    "sudo apt-get update",
    "sudo apt-get upgrade -y",
    "sudo apt-get dist-upgrade -y",
    "sudo apt autoremove -y",
    "sudo snap refresh"
]
# Define the cript version
SCRIPT_VERSION = "\033[1;92mV.1.2\033[0m"


# Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Run commands
def run_command(command):
    try:
        print(f"Running command: {command}")
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        print(f"Command output: {result.stdout}")
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e}")
        print(f"Command output: {e.stdout}")
    except Exception as e:
        print(f"An unexpected error occurred while executing command: {command}")
        print(f"Error message: {e}")


# Clear condole
clear_console()

# print script version
print(f"\033[1;92m                         Running version: \033[0m{SCRIPT_VERSION}")

# ASCI art from patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=
print("""
                                                                                      
    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗██╗███╗   ██╗ ██████╗          
    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝          
    ██║   ██║██████╔╝██║  ██║███████║   ██║   ██║██╔██╗ ██║██║  ███╗         
    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██║██║╚██╗██║██║   ██║         
    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗██╗
     ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
                                               
""")

# Execute each command
for cmd in commands:
    run_command(cmd)

# print epilog
print(f"\n\033[1;92m    Thank you for using the system updater by Expergefactor\033[0m\n")
