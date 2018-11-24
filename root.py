from tkinter import *
from subprocess import call


class Application:
        def __init__(self, master, *args, **kwargs):

                self.master = master
                self.heading = Label(master, text='Daw Bedding Stores', font=('arial 40 bold'), fg='steelblue', bg='lightblue')
                self.heading.place(x=50, y=0)
                # Generate Bills Button.
                self.gen_btn = Button(master, text='1. GENERATE BILLS', width=20, height=2, bg='steelblue', fg='white', command=self.import_main )
                self.gen_btn.place(x=220, y=200)

                # Add to Database Button
                self.atd_btn = Button(master, text='2. ADD TO DATABASE', width=20, height=2, bg='orange', fg='white', command=self.import_addDB )
                self.atd_btn.place(x=220, y=300)

                # Update Database Button
                self.upd_btn = Button(master, text='3. UPDATE DATABASE', width=20, height=2, bg='green', fg='white', command=self.import_update )
                self.upd_btn.place(x=220, y=400)

                # My Logo
                self.myLabel = Label(master, text='Developed by Malayanil Senapati ©', font=('calibri 14 italic'), bg='lightblue')
                self.myLabel.place(x=300, y=550)
                
        def import_main(self, *args, **kwargs):
                call(["python", "main.py"])

        def import_addDB(self, *args, **kwargs):
                call(["python", "add_to_db.py"])

        def import_update(self, *args, **kwargs):
                call(["python", "update.py"])

     
root=Tk()
root.title('Daw Bedding Inventory and Invoice Systems')
root.geometry('600x600')
root.configure(background='lightblue')
b = Application(root)
root.mainloop()
