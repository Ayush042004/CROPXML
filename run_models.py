import subprocess


model_1_process = subprocess.Popen(['python', 'Rnn/App2.py'])

model_2_process = subprocess.Popen(['python', 'App.py'])

model_3_process = subprocess.Popen(['python', 'App3.py'])

model_1_process.wait()
model_2_process.wait()
model_3_process.wait()