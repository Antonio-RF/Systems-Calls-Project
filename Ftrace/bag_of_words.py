import numpy
import random

class BagOfWords:
    def __init__(self):
        self.normal_database = dict()
        self.mismatches = []

    def get(self):
        pass

    def set(self):
        pass

    def validate(self):
        pass

class SlidingWindow(BagOfWords):
    def get(self, trace, i):
        right_idx = min(len(trace), i + window_size + 1)
        return trace[i + 1:right_idx]

    def set(self, current_word, words):
        if current_word not in self.normal_database:
            self.normal_database[current_word] = set()
        self.normal_database[current_word].add(tuple(words))

    def validate(self, current_word, words):
        mismatches = 0
        if current_word not in self.normal_database or \
                tuple(words) not in self.normal_database[current_word]:
            mismatches += window_size
        return mismatches

class Skipgram(BagOfWords):
    def get(self, trace, i):
        left_idx = max(0, i - window_size)
        right_idx = min(len(trace), i + window_size + 1)
        return trace[left_idx:i] + trace[i + 1:right_idx]

    def set(self, current_word, words):
        if current_word not in self.normal_database:
            self.normal_database[current_word] = set()
        self.normal_database[current_word].update(words)

    def validate(self, current_word, words):
        mismatches = 0
        for word in words:
            if current_word not in self.normal_database or \
                    word not in self.normal_database[current_word]:
                mismatches += 1
        return mismatches

def create_normal_database(bag_of_words):
    trace = dict()
    with open(base_path + trace_filename, 'r') as trace_file:
        for line in trace_file.readlines():
            command, words = line.split('|')
            trace[command] = words.strip().split(';')

    for command, words in trace.items():
        for i in range(len(words)):
            word = words[i]
            current_bag_of_words = bag_of_words.get(words, i)
            bag_of_words.set(word, current_bag_of_words)
 
def get_mismatches(bag_of_words):
    for tests in range(0, 10):
        test_command = ''
        test_words = []
        #with open(base_path + trace_filename, 'r') as trace_file:
        with open(base_path + 'ls_syscall_parsed.txt', 'r') as trace_file:
            traces = trace_file.readlines()
            trace = random.randint(0, len(traces) - 1)
            command, words = traces[trace].split('|')
            test_command = command
            test_words = words.split(';')

        mismatches = 0
        for i in range(len(test_words)):
            test_word = test_words[i]
            test_bag_of_words = bag_of_words.get(test_words, i)
            mismatches += bag_of_words.validate(test_word, test_bag_of_words)
        bag_of_words.mismatches.append(mismatches)

        print(f'{test_command}: {mismatches} | {len(test_words)}')

base_path = 'trace_files/'
trace_filename = 'grep_syscall_parsed.txt'
window_size = 5

bag_of_words = Skipgram()
create_normal_database(bag_of_words)
get_mismatches(bag_of_words)

#print(f'Commands mismatches average {numpy.average(mismatches_list)}')
#print(f'Commands mismatches standard deviation {numpy.std(mismatches_list)}')
