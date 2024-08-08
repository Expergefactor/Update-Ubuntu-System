import os
import subprocess
import sys
import threading
import time
from tqdm import tqdm

SCRIPT_VERSION = "\033[1;92m1.8.2\033[0m"


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def checkpermissions():
    try:
        if os.geteuid() != 0:
            print(" \033[91mSystem updater requires Super User privileges, elevating to sudo...\033[0m")
            args = ["sudo", sys.executable] + sys.argv
            os.execvp("sudo", args)
    except PermissionError:
        pass


def run_command_with_progress(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, text=True,
                               shell=True)

    bar_format = "{l_bar} Processing... {bar} Processed: {n}B | Rate: {rate_fmt} | Time Elapsed: {elapsed}"

    pbar = tqdm(range(1024 * 1024 * 100), unit="MB", unit_scale=True, unit_divisor=1024*1024,
                bar_format=bar_format)

    start_time = time.time()

    def read_output():
        nonlocal pbar
        for line in process.stdout:
            bytes_processed = len(line.encode('utf-8'))
            pbar.update(bytes_processed)

    output_thread = threading.Thread(target=read_output)
    output_thread.start()

    process.wait()
    output_thread.join()

    pbar.close()
    end_time = time.time()
    print(f"\033[1;92m Successfully completed in {end_time - start_time:.2f} seconds\033[0m\n")


def apt_update():
    command = 'sudo apt-get update'
    print("\033[1;97m Updating Advanced Packaging Tool...\033[0m")
    try:
        run_command_with_progress(command)

    except Exception as apt_update_error:
        print(f'{apt_update_error}')


def apt_upgrade():
    command = 'sudo apt-get upgrade -y'
    print("\033[1;97m Upgrading Advanced Packaging Tool...\033[0m")

    try:
        run_command_with_progress(command)

    except Exception as apt_upgrade_error:
        print(f'{apt_upgrade_error}')


def dist_upgrade():
    command = 'sudo apt-get dist-upgrade -y'
    print("\033[1;97m Upgrading Distribution...\033[0m")

    try:
        run_command_with_progress(command)

    except Exception as dist_upgrade_error:
        print(f'{dist_upgrade_error}')


def autoremove():
    command = 'sudo apt autoremove -y'
    print("\033[1;97m Removing Redundant Packages...\033[0m")

    try:
        run_command_with_progress(command)

    except Exception as autoremove_error:
        print(f'{autoremove_error}')


def snap_refresh():
    command = 'sudo snap refresh'
    print("\033[1;97m Refreshing the Snap Store...\033[0m")

    try:
        run_command_with_progress(command)

    except Exception as snap_refresh_error:
        print(f'{snap_refresh_error}')


try:
    clear_console()
    checkpermissions()

    print(f"""

            ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗██╗███╗   ██╗ ██████╗          
            ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝          
            ██║   ██║██████╔╝██║  ██║███████║   ██║   ██║██╔██╗ ██║██║  ███╗         
            ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██║██║╚██╗██║██║   ██║         
            ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗██╗
             ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
                                
                                        \033[1;92mv.\033[0m{SCRIPT_VERSION}
    """)

    print(f"")

    apt_update()
    apt_upgrade()
    dist_upgrade()
    autoremove()
    snap_refresh()

    print(f"\033[1;92m    Thank you for using the system updater by Expergefactor\033[0m\n")

except Exception as e:
    print(f"\033[1;91m An unexpected error occurred while executing command: {command} - {e}\n\033[0m")

except KeyboardInterrupt:
    print("\n\033[1;92m User initiated exit, exiting...\n"
          "         Thank you for using the system updater by Expergefactor.\033[0m\n")
