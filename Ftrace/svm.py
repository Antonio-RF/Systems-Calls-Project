import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import random

data = []
ls_file = open('trace_files/ls_ftrace_parsed.txt')
data += ls_file.readlines()
cat_file = open('trace_files/cat_ftrace_parsed.txt')
data += cat_file.readlines()
'''
grep_file = open('trace_files/grep_syscall_parsed.txt')
data += grep_file.readlines()
'''

'''
with open('trace_files/ls_ftrace_parsed.txt') as data_file:
    data += data_file.readlines()
with open('trace_files/cat_ftrace_parsed.txt') as data_file:
    data += data_file.readlines()
with open('trace_files/grep_ftrace_parsed.txt') as data_file:
    data += data_file.readlines()
'''

parsed_data = []
for entry in data:
    params, ftrace = entry.split("| ")
    ftrace_list = ftrace.split(";")
    command = params.split(' ')[0]
    parsed_data.append({"ftrace": " ".join(ftrace_list), "label": command})
    '''
    if "ls" in command:
        parsed_data.append({"ftrace": " ".join(ftrace_list), "label": "bin"})
    else:
        parsed_data.append({"ftrace": " ".join(ftrace_list), "label": "not_bin"})
    '''

print('[+] parsed!')

df = pd.DataFrame(parsed_data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['ftrace'])

X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.8)

#model = svm.SVC(kernel='linear')
#model = RandomForestClassifier(n_estimators=100, random_state=42)
model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


ls_file = open('trace_files/ls_ftrace_parsed_testset.txt')
test_data = ls_file.readlines()
for i in range(0, len(test_data)):
    #new_function_trace = test_data[random.randint(0, len(test_data))]
    new_function_trace = test_data[i]
    command, new_ftrace = new_function_trace.split("| ")
    new_ftrace_list = new_ftrace.split(";")
    new_ftrace_str = " ".join(new_ftrace_list)

    new_X = vectorizer.transform([new_ftrace_str])

    predicted_label = model.predict(new_X)
    print(f'Predicted {command} as {predicted_label[0]}')

'''
test_data = cat_file.readlines()
for i in range(0, 10):
    new_function_trace = test_data[random.randint(0, len(test_data))]
    command, new_ftrace = new_function_trace.split("| ")
    new_ftrace_list = new_ftrace.split(";")
    new_ftrace_str = " ".join(new_ftrace_list)

    new_X = vectorizer.transform([new_ftrace_str])

    predicted_label = model.predict(new_X)
    print(f'Predicted {command} as {predicted_label[0]}')

test_data = grep_file.readlines()
for i in range(0, 10):
    new_function_trace = test_data[random.randint(0, len(test_data))]
    command, new_ftrace = new_function_trace.split("| ")
    new_ftrace_list = new_ftrace.split(";")
    new_ftrace_str = " ".join(new_ftrace_list)

    new_X = vectorizer.transform([new_ftrace_str])

    predicted_label = model.predict(new_X)
    print(f'Predicted {command} as {predicted_label[0]}')
'''
