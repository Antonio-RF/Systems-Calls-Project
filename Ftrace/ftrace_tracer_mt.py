import os
import threading
import subprocess
import atexit
import re
import time
import concurrent.futures

base_path = 'trace_files/'
command_name = 'grep'
commands_filename = f'{command_name}_commands.txt'
cpu_affinity = 11
SELF_COMMANDS_PID = []

def rollback_tracer():
    tracing_on('0')
    current_tracer('nop')
    clear_trace()

def clear_trace():
    print('clear_trace')
    #with open(f'/sys/kernel/tracing/trace', 'w') as tracing_on:
    with open(f'/sys/kernel/tracing/per_cpu/cpu{cpu_affinity}/trace', 'w') as tracing_on:
        tracing_on.write('')

def clear_trace_pipe():
    print('clear_trace_pipe')
    #process = subprocess.Popen(['cat', f'/sys/kernel/tracing/trace_pipe'], \
    process = subprocess.Popen(['cat', f'/sys/kernel/tracing/per_cpu/cpu{cpu_affinity}/trace_pipe'], \
            stdout = subprocess.DEVNULL)
    SELF_COMMANDS_PID.append(process.pid)
    time.sleep(5)
    process.kill()
    process.wait()

def tracing_on(value):
    print(f'tracing_on: {value}')
    with open('/sys/kernel/tracing/tracing_on', 'w') as tracing_on:
        tracing_on.write(value)

def current_tracer(value):
    print(f'current_tracer: {value}')
    with open('/sys/kernel/tracing/current_tracer', 'w') as current_tracer:
        current_tracer.write('function')

def trace_pipe(output_filename):
    print(f'trace_pipe: {output_filename}')
    with open(output_filename, 'a') as output:
        #process = subprocess.Popen(['cat', f'/sys/kernel/tracing/trace_pipe'], \
        process = subprocess.Popen(['cat', f'/sys/kernel/tracing/per_cpu/cpu{cpu_affinity}/trace_pipe'], \
                stdout = output)
        SELF_COMMANDS_PID.append(process.pid)
        process.wait()

def run_command(command):
    #process = subprocess.Popen(command.split(' '), \
    process = subprocess.Popen(['taskset', '-c', str(cpu_affinity)] + command.split(' '), \
            stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    SELF_COMMANDS_PID.append(process.pid)
    process.wait()
    return process.pid

def run_ftrace(commands, command_pids, output_filename):
    clear_trace()
    tracing_on('1')
    current_tracer('function')

    trace_pipe_thread = threading.Thread(target = trace_pipe, args = (output_filename,))
    trace_pipe_thread.start()

    commands_left = [key for key, value in commands.items() if not value]
    for command in commands_left:
        pid = run_command(command)
        if pid not in command_pids.keys():
            command_pids[pid] = command
    '''
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for command, pid in zip(commands_left, executor.map(run_command, commands_left)):
            if pid not in command_pids.keys():
                command_pids[pid] = command
    '''

    rollback_tracer()
    trace_pipe_thread.join()

def main():
    if os.getuid() != 0:
        print('Could not run as normal user, please run as root')
        return

    commands = dict()
    with open(base_path + commands_filename, 'r') as commands_file:
        for command in commands_file.readlines()[0:-1]:
            commands[command] = False

    ftrace_raw_filename = base_path + command_name + '_ftrace_raw_test.txt'
    if os.path.isfile(ftrace_raw_filename):
        os.remove(ftrace_raw_filename)

    ftrace_database = dict()
    command_pids = dict()
    print(f'Commands traced {len(ftrace_database)}')
    while len(ftrace_database) != len(commands):
        run_ftrace(commands, command_pids, ftrace_raw_filename)
        with open(ftrace_raw_filename, 'r+') as ftrace_raw_file:
            ftrace_raw = ftrace_raw_file.readlines()
            for i in range(len(ftrace_raw)):
                line = ftrace_raw[i].strip().split(' ')
                if re.match(f'^{command_name}-[0-9]+$', line[0], re.IGNORECASE):
                    pid = int(re.sub(f'^{command_name}-([0-9]+)$', r'\1', line[0]))
                    if pid in SELF_COMMANDS_PID:
                        continue
                    if command_pids[pid] in ftrace_database.keys():
                        ftrace_database[command_pids[pid]].append(f'{line[-2]} {line[-1]}')
                    else:
                        ftrace_database[command_pids[pid]] = []

        print(f'Commands traced {len(ftrace_database)}')
        for command in ftrace_database.keys():
            commands[command] = True

    ftrace_parsed_filename = base_path + command_name + '_ftrace_parsed_test.txt'
    with open(ftrace_parsed_filename, 'w') as ftrace_parsed_file:
        for command, ftrace in ftrace_database.items():
            ftrace_parsed_file.write(f'{command.strip()}: {";".join(ftrace)}\n')


if __name__ == '__main__':
    atexit.register(rollback_tracer)
    main()
