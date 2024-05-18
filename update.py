# To run the script
import os
import subprocess
# For the display of progress bars.
from tqdm import tqdm

# Define the cript version
SCRIPT_VERSION = "\033[1;92mV.1.4\033[0m"


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

        # Initialize the progress bar with an initial estimate
        estimated_total_lines = 100  # Start with an arbitrary number
        pbar = tqdm(total=estimated_total_lines, desc="Updating Advanced Packaging Tool")

        line_count = 0

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line_count += 1
                # Update progress bar
                if line_count > estimated_total_lines:
                    # Dynamically increase the total if needed
                    pbar.total = line_count
                pbar.update(1)  # Increment progress bar

        # Ensure the process has completed
        return_code = process.poll()
        if return_code != 0:
            print(f" Command failed with return code {return_code}\n\n")
        else:
            print(" Command executed successfully\n\n")

        # Final update to ensure the progress bar completes
        pbar.update(pbar.total - pbar.n)
        pbar.close()

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit, exiting...\n\n")


def apt_upgrade():
    # command to run
    command = 'sudo apt-get upgrade -y'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Initialize the progress bar with an initial estimate
        estimated_total_lines = 100  # Start with an arbitrary number
        pbar = tqdm(total=estimated_total_lines, desc="Upgrading Advanced Packaging Tool")

        line_count = 0

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line_count += 1
                # Update progress bar
                if line_count > estimated_total_lines:
                    # Dynamically increase the total if needed
                    pbar.total = line_count
                pbar.update(1)  # Increment progress bar

        # Ensure the process has completed
        return_code = process.poll()
        if return_code != 0:
            print(f" Command failed with return code {return_code}\n\n")
        else:
            print(" Command executed successfully\n\n")

        # Final update to ensure the progress bar completes
        pbar.update(pbar.total - pbar.n)
        pbar.close()

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit, exiting...\n\n")


def dist_upgrade():
    # command to run
    command = 'sudo apt-get dist-upgrade -y'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Initialize the progress bar with an initial estimate
        estimated_total_lines = 100  # Start with an arbitrary number
        pbar = tqdm(total=estimated_total_lines, desc="Upgrading Distribution")

        line_count = 0

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line_count += 1
                # Update progress bar
                if line_count > estimated_total_lines:
                    # Dynamically increase the total if needed
                    pbar.total = line_count
                pbar.update(1)  # Increment progress bar

        # Ensure the process has completed
        return_code = process.poll()
        if return_code != 0:
            print(f" Command failed with return code {return_code}\n\n")
        else:
            print(" Command executed successfully\n\n")

        # Final update to ensure the progress bar completes
        pbar.update(pbar.total - pbar.n)
        pbar.close()

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit, exiting...\n\n")


def autoremove():
    # command to run
    command = 'sudo apt autoremove -y'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Initialize the progress bar with an initial estimate
        estimated_total_lines = 100  # Start with an arbitrary number
        pbar = tqdm(total=estimated_total_lines, desc="Removing Redundant Packages")

        line_count = 0

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line_count += 1
                # Update progress bar
                if line_count > estimated_total_lines:
                    # Dynamically increase the total if needed
                    pbar.total = line_count
                pbar.update(1)  # Increment progress bar

        # Ensure the process has completed
        return_code = process.poll()
        if return_code != 0:
            print(f" Command failed with return code {return_code}\n\n")
        else:
            print(" Command executed successfully\n\n")

        # Final update to ensure the progress bar completes
        pbar.update(pbar.total - pbar.n)
        pbar.close()

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit, exiting...\n\n")


def snap_refresh():
    # command to run
    command = 'sudo snap refresh'

    try:
        # Start the process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Initialize the progress bar with an initial estimate
        estimated_total_lines = 100  # Start with an arbitrary number
        pbar = tqdm(total=estimated_total_lines, desc="Refreshing the Snap Store")

        line_count = 0

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line_count += 1
                # Update progress bar
                if line_count > estimated_total_lines:
                    # Dynamically increase the total if needed
                    pbar.total = line_count
                pbar.update(1)  # Increment progress bar

        # Ensure the process has completed
        return_code = process.poll()
        if return_code != 0:
            print(f" Command failed with return code {return_code}\n\n")
        else:
            print(" Command executed successfully\n\n")

        # Final update to ensure the progress bar completes
        pbar.update(pbar.total - pbar.n)
        pbar.close()

    except Exception as e:
        print(f" An unexpected error occurred while executing command: {command}\n\n")
        print(f" Error message: {e}\n\n")

    except KeyboardInterrupt:
        print(" User initiated exit, exiting...\n\n")


# Run processes with progress bars
def main():
    apt_update()
    apt_upgrade()
    dist_upgrade()
    autoremove()
    snap_refresh()
    print(f"\n\033[1;92m    Thank you for using the system updater by Expergefactor\033[0m\n")


if __name__ == "__main__":
    main()
