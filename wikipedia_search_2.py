from tkinter import *   #using * will use it will import all functions in tkinter
import wikipedia

def  on_press():
    q = get_q.get()
    text.insert(INSERT,wikipedia.summary(q))

root = Tk()
root.title("WIKI Search app")
question = Label(root,text="Question")
question.pack()
get_q = Entry(root,bd=5)
get_q.pack()
submit = Button(root,text="Search",command=on_press)
submit.pack()
text = Text(root)
text.pack()

root.mainloop()