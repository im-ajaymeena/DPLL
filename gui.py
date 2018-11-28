from tkinter import *
from def_dpll import dpll
import timeit
#from timeit import Timer

root = Tk()
solu = {}
our_clauses = []

left_outer = Frame(root, bd=1)
left_outer.pack(side=LEFT, fill=Y, pady=5, padx=5)
center_outer = Frame(root, bd=1)
center_outer.pack(side=BOTTOM, fill=Y, pady=5, padx=5)
right_outer = Frame(root, bd=1)
right_outer.pack(side=RIGHT, fill=Y, pady=5, padx=5)


left = Frame(left_outer, bd=2, relief=SUNKEN)
right = Frame(right_outer, bd=2, relief=SUNKEN)
left.pack(fill=Y)
right.pack(fill=Y)

t_input = Text(left, width=30, height=200)
t_input.pack(side=LEFT, fill=Y)
s_start = Scrollbar(left)
s_start.pack(side=RIGHT, fill=Y)
s_start.config(command=t_input.yview)
t_input.config(yscrollcommand=s_start.set)
t_input.config(xscrollcommand=s_start.set)

t_output = Text(right, width=40, height=200)
t_output.pack(side=RIGHT)

input_entry = Entry(center_outer)
input_entry.pack(side=TOP)
	
def ps():
	print("H")
	a=Entry.get(input_entry)
	our_clauses.append(list(map(int, a.split(','))))
	t_input.delete('1.0',END)
	t_input.insert(END,'All clause sets shown in \n integer format:')
	t_input.insert(END,'\n')
	for i in range(len(our_clauses)):
		t_input.insert(END,'clause ')
		t_input.insert(END,i+1)
		t_input.insert(END,' is: ')
		for x in our_clauses[i]:
			t_input.insert(END, x)
			t_input.insert(END, ' ')
		t_input.insert(END, '\n')
	print(our_clauses)
	input_entry.delete(0, 'end')
	
append_button = Button(center_outer, text="append",command=ps)
append_button.pack(side=TOP)

time_text = Text(center_outer, width=40, height=2)
time_text.pack(side=BOTTOM,fill=X)

def run_dpll():
	t_output.delete('0.0',END)
	solu = {}
	solu_time = {}
	status_dpll = dpll(our_clauses,solu)
	t1 = timeit.Timer(lambda: dpll(our_clauses,solu_time))
	time_text.delete('0.0',END)
	time_text.insert(END,'Time taken by DPLL :\n ')
	time_text.insert(END,t1.timeit(number=1))
	del our_clauses[:]
	if not status_dpll:
		t_output.insert(END,'clause set unsatisfied')
	else:	
		for set in solu:
			t_output.insert(END, 'value of literal ')
			t_output.insert(END, set)
			t_output.insert(END, ' is: ')
			t_output.insert(END, solu[set])
			t_output.insert(END, '\n')
	

button_dpll = Button(center_outer, text="DPLL",command=run_dpll)
button_dpll.pack(side=TOP)

root.geometry("500x200")
root.mainloop()
