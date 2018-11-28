from tkinter import *
from def_dpll import dpll
import timeit
#from timeit import Timer

root = Tk()

solu = {}

#def printNmae():
#	print("Hello world")

# button1 = Button(root, text="Print name", command=printNmae)
# button1.pack()

#our_clauses = [[1,2,3,5],[-1,-2,-3],[1,2,3,5],[-1,-2,-3],[1,2,3,5],[-1,-2,-3]]
our_clauses = []


#t = Text(root)



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
#s_end = Scrollbar(right)
#s_end.pack(side=RIGHT)
#s_end.config(command=t_output.yview)
#t_output.config(yscrollcommand=s_end.set)




b = Entry(center_outer)
b.pack(side=TOP)
#b.focus_set()
	
def ps():
	print("H")
	a=Entry.get(b)
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
	b.delete(0, 'end')
	
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