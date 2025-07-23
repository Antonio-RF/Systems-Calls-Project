import os
import threading
import subprocess
import atexit
import re
import time
import concurrent.futures

base_path = 'trace_files/'
command_name = 'cat'
commands_filename = f'{command_name}_commands.txt'

def run_command(command):
    process = subprocess.run(['strace'] + command.split(' '), \
            stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    return process.stderr

def main():
    if os.getuid() != 0:
        print('Could not run as normal user, please run as root')
        return

    commands = set()
    with open(base_path + commands_filename, 'r') as commands_file:
        commands.update(commands_file.readlines()[0:-1])

    parsed = dict()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for command, syscalls in zip(commands, executor.map(run_command, commands)):
            syscall = []
            for line in syscalls.split(b'\n')[0:-2]:
                line = line.decode('utf-8')
                if re.match(r'^[a-z]+\(', line, re.IGNORECASE):
                    syscall.append(line.split('(')[0])
            parsed[command.strip()] = ';'.join(syscall)

    syscall_parsed_filename = base_path + command_name + '_syscall_parsed.txt'
    with open(syscall_parsed_filename, 'w') as syscall_parsed_file:
        for command, syscalls in parsed.items():
            syscall_parsed_file.write(f'{command}: {syscalls}\n')


if __name__ == '__main__':
    main()
