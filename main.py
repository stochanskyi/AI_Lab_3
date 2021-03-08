from task import *
from tkinter import *
from tkmacosx import Button as MacosButton


def calculate_score():
    k = int(k_input.get())
    if k <= 0:
        return
    score = get_learning_score(neighbours_classifier(k))
    score_label['text'] = 'Learning score: ' + str(int(score * 100)) + '%'

root = Tk()

root.title("Lab 2")
root.geometry("1300x800")

# Task one layout

task_one_frame = Frame(root)
task_one_frame.place(relx=0.05, rely=0.05, relwidth=0.5, relheight=1)

task_one_title = Label(task_one_frame, text='TASK', font='Helvetica 14 bold')
task_one_title.pack()

task_one_description = Label(task_one_frame, text='Please enter k that is number of neighbours that will be used to '
                                                  'calculate item class\n(k > 0)')
task_one_description.pack()

input_frame = Frame(task_one_frame)
input_frame.pack(pady=20)

k_label = Label(input_frame, text='k', fg='grey')
k_label.pack(side=LEFT)

k_input = Entry(input_frame)
k_input.pack(side=LEFT)

button_zero_to_one = MacosButton(task_one_frame, text='Check score for k', command=calculate_score)
button_zero_to_one.pack(pady=10)

score_label = Label(task_one_frame)
score_label.pack(pady=20)

# Task two layout

task_two_frame = Frame(root)
task_two_frame.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=1)

Label(task_two_frame, text='Classes description', font='Helvetica 14 bold').pack()

classes_label = Label(task_two_frame)
classes_label.pack(pady=10)

classes_label['text'] = '\n'.join(map(str, newgroups_bunch.target_names))

Label(task_two_frame, text='Top 5 input data\nFormat: (i, j) value', font='Helvetica 14 bold').pack()

data_label = Label(task_two_frame)
data_label.pack()

input_data = newgroups_bunch.data
counter = 0

for i, j in zip(*input_data.nonzero()):
    data_label['text'] += '\n' + "(%d, %d) %s" % (i, j, input_data[i, j])
    counter += 1
    if counter >= 5:
        break

root.mainloop()

