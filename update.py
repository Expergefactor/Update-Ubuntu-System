# To run the script
import os
import subprocess
# For the display of progress bars.
from tqdm import tqdm

# Define the cript version
SCRIPT_VERSION = "\033[1;92mV.1.3\033[0m"


# Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Clear condole
clear_console()

# print script version
print(f"\n\033[1;92m                            Running version: \033[0m{SCRIPT_VERSION}")

# ASCI art from patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=
print("""

        ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗██╗███╗   ██╗ ██████╗          
        ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝          
        ██║   ██║██████╔╝██║  ██║███████║   ██║   ██║██╔██╗ ██║██║  ███╗         
        ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██║██║╚██╗██║██║   ██║         
        ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗██╗
         ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝

""")


def apt_update():
    # command to run
    command = 'sudo apt-get update'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Read and count the number of lines in the output to estimate progress
        total_lines = 0
        for line in process.stdout:
            total_lines += 1

        # Set up the progress bar with an estimated total number of lines
        estimated_total_lines = max(total_lines, 100)  # Using 100 as a fallback if no lines are outputted

        # Re-run the command to display progress
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with tqdm(total=estimated_total_lines, desc="Updating Advanced Packaging Tool") as pbar:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pbar.update(1)  # Update progress bar by 1 for each line

            # Ensure the process has completed
            return_code = process.poll()
            if return_code != 0:
                print(f" Command failed with return code {return_code}\n\n")
            else:
                print(" Command executed successfully.\n\n")

            # Final update to ensure the progress bar completes
            pbar.update(pbar.total - pbar.n)

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit. Exiting...\n\n")


def apt_upgrade():
    # command to run
    command = 'sudo apt-get upgrade -y'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Read and count the number of lines in the output to estimate progress
        total_lines = 0
        for line in process.stdout:
            total_lines += 1

        # Set up the progress bar with an estimated total number of lines
        estimated_total_lines = max(total_lines, 100)  # Using 100 as a fallback if no lines are outputted

        # Re-run the command to display progress
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with tqdm(total=estimated_total_lines, desc="Upgrading Advanced Packaging Tool") as pbar:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pbar.update(1)  # Update progress bar by 1 for each line

            # Ensure the process has completed
            return_code = process.poll()
            if return_code != 0:
                print(f" Command failed with return code {return_code}\n\n")
            else:
                print(" Command executed successfully.\n\n")

            # Final update to ensure the progress bar completes
            pbar.update(pbar.total - pbar.n)

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit. Exiting...\n\n")


def dist_upgrade():
    # command to run
    command = 'sudo apt-get dist-upgrade -y'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Read and count the number of lines in the output to estimate progress
        total_lines = 0
        for line in process.stdout:
            total_lines += 1

        # Set up the progress bar with an estimated total number of lines
        estimated_total_lines = max(total_lines, 100)  # Using 100 as a fallback if no lines are outputted

        # Re-run the command to display progress
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with tqdm(total=estimated_total_lines, desc="Upgrading Distribution") as pbar:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pbar.update(1)  # Update progress bar by 1 for each line

            # Ensure the process has completed
            return_code = process.poll()
            if return_code != 0:
                print(f" Command failed with return code {return_code}\n\n")
            else:
                print(" Command executed successfully.\n\n")

            # Final update to ensure the progress bar completes
            pbar.update(pbar.total - pbar.n)

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit. Exiting...\n\n")


def autoremove():
    # command to run
    command = 'sudo apt autoremove -y'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Read and count the number of lines in the output to estimate progress
        total_lines = 0
        for line in process.stdout:
            total_lines += 1

        # Set up the progress bar with an estimated total number of lines
        estimated_total_lines = max(total_lines, 100)  # Using 100 as a fallback if no lines are outputted

        # Re-run the command to display progress
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with tqdm(total=estimated_total_lines, desc="Removing Redundant Packages") as pbar:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pbar.update(1)  # Update progress bar by 1 for each line

            # Ensure the process has completed
            return_code = process.poll()
            if return_code != 0:
                print(f" Command failed with return code {return_code}\n\n")
            else:
                print(" Command executed successfully.\n\n")

            # Final update to ensure the progress bar completes
            pbar.update(pbar.total - pbar.n)

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit. Exiting...\n\n")


def snap_refresh():
    # command to run
    command = 'sudo snap refresh'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Read and count the number of lines in the output to estimate progress
        total_lines = 0
        for line in process.stdout:
            total_lines += 1

        # Set up the progress bar with an estimated total number of lines
        estimated_total_lines = max(total_lines, 100)  # Using 100 as a fallback if no lines are outputted

        # Re-run the command to display progress
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with tqdm(total=estimated_total_lines, desc="Refreshing the Snap Store") as pbar:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pbar.update(1)  # Update progress bar by 1 for each line

            # Ensure the process has completed
            return_code = process.poll()
            if return_code != 0:
                print(f" Command failed with return code {return_code}\n\n")
            else:
                print(" Command executed successfully.\n\n")

            # Final update to ensure the progress bar completes
            pbar.update(pbar.total - pbar.n)

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit. Exiting...\n\n")


# Run processes with progress bars
def main():
    tasks = [apt_update, apt_upgrade, dist_upgrade, autoremove, snap_refresh]
    for task in tasks:
        task()
    print(f"\n\033[1;92m                Thank you for using the system updater by Expergefactor\033[0m\n")


if __name__ == "__main__":
    main()
