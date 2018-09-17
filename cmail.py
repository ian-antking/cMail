import tkinter as tk
from tkinter import messagebox
import os


root = tk.Tk()
root.resizable(width=False, height=False)

root.title("cMail")
root.geometry('850x600')
root.iconbitmap('logo.ico')
root.configure(background="#BFBFBF")

send_logo = tk.PhotoImage(file="send-mail.png")

filepath = "%s\Documents\cmail" % os.path.expanduser("~")

print (filepath)

if not os.path.exists(filepath):
    os.mkdir(filepath)

def send_mail():
    global filepath
    if not toinput.get():
        messagebox.showerror('Error','You must enter an email address!')
    elif not subjectinput.get():
        messagebox.showerror('Error','You must enter a subject')
    else:
        filename = subjectinput.get()
        mail_out = open("%s\%s.txt" % (filepath, filename), "w")
        mail_out.write("To: %s" % toinput.get())
        mail_out.write("\nCC: %s" % ccinput.get())
        mail_out.write("\nSubject: %s\n" % subjectinput.get())
        mail_out.write("\nMessage:\n %s" % email.get("1.0", "end"))
        mail_out.close()
        os.startfile("%s\%s.txt" % (filepath, filename))

#define widgets
send = tk.Button(root, text="Send", image=send_logo, compound = tk.TOP, width = 90, height = 90, bg="#BFBFBF", command=send_mail)

inputs = tk.Frame(root, bg="#BFBFBF")

tolabel = tk.Label(inputs, text="To:", width=7, anchor=tk.E, bg="#BFBFBF")
cclabel = tk.Label(inputs, text="CC:", width=7, anchor=tk.E, bg="#BFBFBF")
subjectlabel = tk.Label(inputs, text="Subject:", width=7, anchor=tk.E, bg="#BFBFBF")

toinput = tk.Entry(inputs, width=100)
ccinput = tk.Entry(inputs, width=100)
subjectinput = tk.Entry(inputs, width=100)

email = tk.Text(root)


#display widgets
send.grid(column=0, row=0, padx=20, pady=10)
inputs.grid(column=1, row=0)
tolabel.grid(column=0, row=0, pady=5)
cclabel.grid(column=0, row=1, pady=5)
subjectlabel.grid(column=0, row=2, pady=5)
toinput.grid(column=1, row=0)
ccinput.grid(column=1, row=1)
subjectinput.grid(column=1, row=2)

email.grid(column = 0, row = 1, columnspan=2, pady=20, padx=20, sticky="we")



root.mainloop()
