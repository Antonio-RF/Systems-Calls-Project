import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.preprocessing import LabelEncoder


data = []
ls_file = open('trace_files/ls_ftrace_parsed.txt')
data += ls_file.readlines()
'''
cat_file = open('trace_files/cat_ftrace_parsed.txt')
data += cat_file.readlines()
grep_file = open('trace_files/grep_syscall_parsed.txt')
data += grep_file.readlines()
'''

ftrace_logs = []
for entry in data:
    params, ftrace = entry.split("| ")
    ftrace_list = ftrace.split(";")
    command = params.split(' ')[0]
    ftrace_logs.append({"ftrace": ftrace_list, "label": command})

data = [] # free some memory i guess
print('[+] parsed!')

def parse_ftrace_logs(ftrace_logs):
    function_names = []
    for logs in ftrace_logs:
        function_names.extend(logs['ftrace'])
    return function_names

function_names = parse_ftrace_logs(ftrace_logs)
print('[+] function names!')

df = pd.DataFrame(function_names, columns=['function_name'])

label_encoder = LabelEncoder()
df['function_encoded'] = label_encoder.fit_transform(df['function_name'])
print('[+] transformed!')

normal_data = df['function_encoded'].values.reshape(-1, 1)
print('[+] reshaped!')

model = svm.OneClassSVM(gamma='auto', nu=0.1)
model.fit(normal_data)
print('[+] fit!')


data = []
ls_file = open('trace_files/ls_ftrace_parsed_testset.txt')
data += ls_file.readlines()

new_ftrace_logs = []
for entry in data:
    params, ftrace = entry.split("| ")
    ftrace_list = ftrace.split(";")
    command = params.split(' ')[0]
    new_ftrace_logs.append({"ftrace": ftrace_list, "label": command})

new_function_names = parse_ftrace_logs(new_ftrace_logs)

new_df = pd.DataFrame(new_function_names, columns=['function_name'])
new_df['function_encoded'] = label_encoder.transform(new_df['function_name'])

new_features = new_df['function_encoded'].values.reshape(-1, 1)

predictions = model.predict(new_features)

for i, prediction in enumerate(predictions):
    if prediction == 1:
        print(f"The new execution from {list(new_ftrace_log.keys())[0]} is classified as normal.")
    else:
        print(f"The new execution from {list(new_ftrace_log.keys())[0]} is classified as an anomaly.")

