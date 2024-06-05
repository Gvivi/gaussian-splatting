import os
import subprocess

COMMAND_FILE = "command_queue.txt"

def execute_command(command):
    full_command = f"conda activate gaussian_splatting && {command}"
    process = subprocess.Popen(full_command, shell=True)
    process.wait()

def get_commands_from_file():
    if os.path.exists(COMMAND_FILE):
        with open(COMMAND_FILE, 'r') as file:
            commands = file.readlines()
        # Clear the file after reading commands
        with open(COMMAND_FILE, 'w') as file:
            file.truncate()
        return [cmd.strip() for cmd in commands]
    return []

def main():
    commands = get_commands_from_file()
    if not commands:
        print("No commands to execute.")
        return

    for command in commands:
        execute_command(command)
    print("All commands executed and file cleared.")

if __name__ == "__main__":
    main()
