
from  fpdf import FPDF
import tkinter as tk
import sqlite3
from datetime import date

"""
CrossBooks Book Keeping software developed for St. Alban's Anglican Church.

In loving memory of Linda Floud. 
"""

__author__ = "Liam Burns"
__credits__ = ["Noel Henry"]
__version__ = "1.00"
__email__ = "liamburns@cmail.carleton.ca"

con = sqlite3.connect('contributers.db')

#Die
class SampleApp(tk.Tk):
    """
    Each page is an instance its spesific page , when a new page is called that instance is destroyed. Going to need to find a way to pass the key on each time for spesific year.
    probly a more efficent way to do this, maybe make each page a subclass of a master page class?
    """
    def __init__(self):
        self.key = None
        tk.Tk.__init__(self,self.key)
        self._frame = None
        self.switch_frame(StartPage,self.key)

    def switch_frame(self, frame_class,key):
        """Destroys current frame and replaces it with a new one."""
        self.key = key
        new_frame = frame_class(self,self.key)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    """ Startup page key for year is entered here"""
    def __init__(self, master,key):
        self.key = key
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter The Year!").pack(side="top", fill="x", pady=10)
        enter = tk.Entry(self, bg='grey')
        enter.pack(side="top", fill='x', expand=True)
        tk.Button(self, text="Save Year", background="#6d88a8",command=lambda: self.save_key(enter.get())).pack()
        tk.Button(self, text="Submit", background="#6d88a8",command=lambda: master.switch_frame(main_menue,self.get_key())).pack()
    def save_key(self,key_str):
        self.key = key_str
        print(key_str)

    def get_key(self):
        return self.key


class main_menue(tk.Frame):
    def __init__(self, master,key):
        self.key = key
        tk.Frame.__init__(self, master)
        tk.Label(self, text="For The Year " + str(self.get_key())).grid(column=0,row=0)
        tk.Button(self, text="New Entry",command=lambda: master.switch_frame(new_entry,self.get_key()),width=12).grid(row=1,column=0)

        tk.Button(self, text="Print Individual",command=lambda: master.switch_frame(prints1,self.get_key()),width=12).grid(row=1,column=1)

        tk.Button(self, text="Print Church",command=lambda: master.switch_frame(prints2,self.get_key()),width=12).grid(row=2,column=0)

        tk.Button(self, text="Edit",command=lambda: master.switch_frame(edits,self.get_key()),width=12).grid(row=2,column=1)




    def get_key(self):
        return self.key

class edits(tk.Frame):
    def __init__(self, master, key):
        self.key = key
        tk.Frame.__init__(self, master)
        tk.Button(self, text="back",
                  command=lambda: master.switch_frame(main_menue,self.get_key())).pack()

    def get_key(self):
        return self.key

class new_entry(tk.Frame):
    def __init__(self, master, key):
        self.key = key
        tk.Frame.__init__(self, master)

        tk.Label(self, text="First Name").grid(row=0, column=0)
        tk.Label(self, text="Last Name").grid(row=1, column=0)
        tk.Label(self, text="Ammount:").grid(row=2, column=0)
        tk.Label(self, text="Number:").grid(row=3, column=0)
        enter1 = tk.Entry(self, bg='grey',).grid(row=0, column=1)
        enter2 = tk.Entry(self, bg='grey').grid(row=1, column=1)
        enter3 = tk.Entry(self, bg='grey').grid(row=2, column=1)
        enter4 = tk.Entry(self, bg='grey').grid(row=3, column=1)

        tk.Button(self, text="back",
                  command=lambda: master.switch_frame(main_menue,self.get_key())).grid(row=4, column=0)
        tk.Button(self, text="Submit").grid(row=4, column=1)


    def get_key(self):
        return self.key

class prints2(tk.Frame):
    def __init__(self, master, key):
        self.key = key

        tk.Label(self, text="First Name").grid(row=0, column=0)
        tk.Label(self, text="Last Name").grid(row=1, column=0)
        tk.Frame.__init__(self, master)
        tk.Button(self, text="back",
                  command=lambda: master.switch_frame(main_menue,self.get_key())).grid(row=4, column=1)

    def get_key(self):
        return self.key

class prints1(tk.Frame):
    def __init__(self, master, key):
        self.key = key
        tk.Frame.__init__(self, master)

        tk.Label(self, text="First Name").grid(row=0, column=0)
        tk.Label(self, text="Last Name").grid(row=1, column=0)
        enter1 = tk.Entry(self, bg='grey', ).grid(row=0, column=1)
        enter2 = tk.Entry(self, bg='grey').grid(row=1, column=1)

        tk.Button(self, text="back",
                  command=lambda: master.switch_frame(main_menue, self.get_key())).grid(row=4, column=0)
        tk.Button(self, text="Submit",command=lambda:self.gen_pdf()).grid(row=4, column=1)

    def get_key(self):
        return self.key

    def gen_pdf(self):
        """
        \nCanada Revenue Agency:canada.ca/charities-giving\nSt. Alban\'s Church\n67 Main Street, PO box 156,\n Odessa,Ontario,K0H 2H0\nTax Reg: #742967920RR00001")

        """
        today = date.today()
        pdf = FPDF('L','mm',(150,250))
        pdf.add_page()
        pdf.set_font('times','', 11)
        pdf.image('images/csbx.jpg', x=190, y=25, w=50, h=25,)
        pdf.cell(40,5,"Offcial donation receipt for income tax purposes                                                                                                           Receipt Number:",ln=True)
        pdf.cell(40, 5, "Canada Revenue Agency:canada.ca/charities-giving                                                                                                     Date:  "+today.strftime("%b-%d-%Y") , ln=True)
        pdf.cell(40, 5, "St. Alban\'s Anglican Church", ln=True)
        pdf.cell(40, 5, "67 Main Street, PO box 156,", ln=True)
        pdf.cell(40, 5, "PO box 156,", ln=True)
        pdf.cell(40, 5, "Odessa,Ontario,K0H 2H0", ln=True)
        pdf.cell(40, 5, "Tax Reg: #742967920RR00001", ln=True)
        pdf.cell(40, 50, " ", ln=True)
        pdf.set_font('times', '', 14)
        pdf.cell(40, 5, "Recived From:",ln=True )
        pdf.cell(40, 5, "For Donation to St. Alban\'s Anglican Church ", ln=True)
        pdf.cell(40, 5, "From January 1st" + " YEAR" + "to December 31st" + " YEAR", ln=True)



        pdf.output('pdf1.pdf')


def get_text(textbox):

    print(textbox.get())

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()



"""
OLD CODE
startup = [[sg.Text('CrossBooking v0.01')],
            [sg.InputText("enter current year",key='YEAR')],
            [sg.Button('Ok')]]

layout =  [[sg.Text('CrossBooking v0.01')],
            [sg.InputText("enter a name",key='NAME')],
            [sg.Button('GENREC')],
           [sg.Button('ADD')]]

add_person =  [[sg.Text('CrossBooking v0.01')],
            [sg.InputText("enter a name",key='add_Name')],
            [sg.InputText("enter the ammount", key='add_Ammount')],
            [sg.InputText("enter the Account number", key='add_account')],
            [sg.Button('okayadd')]
            ]
window = sg.Window("CrossBooking",startup)


while True:             # Event Loop

    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Ok':
        c = load_list(values['YEAR'])
        window = sg.Window("CrossBooking",layout)
    elif event == 'GENREC':
        create_rec(c,'NAME')
    elif event == 'ADD':
        window = sg.Window("CrossBooking", add_person)
        if event == 'okayadd':
            add_person_func(c, 'add_Name',"add_Ammount","add_account")
            window.Close()
            #First Window On Startup, Collect Year info to sellect what SQL object to use.
root = tk.Tk()
frame = tk.Frame(root,bg="#6da2a8")
frame.place(relwidth=1,relheight=1)
enter = tk.Entry(frame, bg='grey')
enter.pack(side="top",fill='x',expand=True)
button = tk.Button(frame,text="Submit", background="#6d88a8")
button.pack(side='bottom')
root.mainloop()

root = tk.Tk()
frame = tk.Frame(root, bg="#6da2a8")
frame.place(relwidth=1, relheight=1)
enter = tk.Entry(frame, bg='grey')
enter.pack(side="top", fill='x', expand=True)
button = tk.Button(frame, text="Submit", background="#6d88a8")
button.pack(side='bottom')
root.mainloop()



"""






















