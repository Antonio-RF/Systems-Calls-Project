import os
import threading
import subprocess
import atexit
import re
import time
import concurrent.futures

base_path = 'trace_files/'
command_name = 'ls'
commands_filename = f'{command_name}_commands_testset.txt'
cpu_affinity = 3

def run_command(command):
    perf_command = f'perf --no-pager ftrace trace -C {cpu_affinity} -t function taskset -c {cpu_affinity}'
    process = subprocess.run(perf_command.split(' ') + command.split(' '), \
            stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    return process.stdout.decode('utf-8').split('\n')


def main():
    ftrace_parsed_filename = base_path + command_name + '_ftrace_parsed_testset.txt'
    with open(ftrace_parsed_filename, 'w') as ftrace_parsed_file:
        with open(base_path + commands_filename, 'r') as commands_file:
            j = 0
            commands = commands_file.readlines()[0:-1]
            #while j < 10:
            while j < len(commands):
                command = commands[j]
                ftrace_database = dict()
                trace_raw = run_command(command)
                traced = False
                for i in range(len(trace_raw)):
                    line = trace_raw[i].strip().split(' ')
                    if re.match(f'^{command_name}-[0-9]+$', line[0], re.IGNORECASE):
                        if command not in ftrace_database.keys():
                            ftrace_database[command] = []
                        ftrace_database[command].append(f'{line[-2]} {line[-1]}')
                        traced = True
                if not traced:
                    continue
                ftrace = ftrace_database[command]
                ftrace_parsed_file.write(f'{command.strip()}| {";".join(ftrace)}\n')
                print(j)
                j += 1


if __name__ == '__main__':
    main()
