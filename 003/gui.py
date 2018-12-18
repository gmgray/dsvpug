import func
from tkinter import *
from tkinter import ttk
import subprocess

class CreateSRQ:
    def __init__(self,title="SRQ WorkFiles"):
        self.window = Tk()
        self.window.title(title)
        self.instances=(['A','B','C','D','P','All'])
        self.SRQ=StringVar()
        self.RFC=StringVar()
        self.Instance=StringVar()
        self.Site=StringVar()
        self.Client=StringVar()
        self.Requestor=StringVar()
        self.Description=StringVar()
        self.lblSRQ          =   Label(self.window,width=4,anchor=E,text="SRQ:").grid(row=0,column=0)
        self.lblRFC          =   Label(self.window,width=4,anchor=E,text="RFC:").grid(row=0,column=2)
        self.lblSite         =   Label(self.window,width=4,anchor=E,text="Site:").grid(row=1,column=0)
        self.lblClient       =   Label(self.window,width=6,anchor=E,text="Client:").grid(row=1,column=2)
        self.lblRequestor    =   Label(self.window,width=10,anchor=E,text="Requestor:").grid(row=2,column=0)
        self.lblInstance     =   Label(self.window,width=8,anchor=E,text="Instance:").grid(row=2,column=2)
        self.lblDescription  =   Label(self.window,width=10,anchor=E,text="Description:").grid(row=3,column=0)
        self.txtSRQ          =   ttk.Entry(self.window,width=15,textvariable=self.SRQ)
        self.txtRFC          =   ttk.Entry(self.window,width=15,textvariable=self.RFC)
        self.txtSite         =   ttk.Entry(self.window,width=15,textvariable=self.Site)
        self.txtClient       =   ttk.Entry(self.window,width=15,textvariable=self.Client)
        self.txtRequestor    =   ttk.Entry(self.window,width=15,textvariable=self.Requestor)
        self.txtInstance     =   ttk.Combobox(self.window,width=10,values=self.instances,textvariable=self.Instance)
        self.txtDescription  =   ttk.Entry(self.window,width=40,textvariable=self.Description)
        self.txtBox          =   Text(self.window,height=20)
        self.txtSRQ.grid(row=0,column=1,sticky=W+E,padx=5,pady=5)
        self.txtRFC.grid(row=0,column=3,sticky=W+E,padx=5,pady=5)
        self.txtSite.grid(row=1,column=1,sticky=W+E,padx=5,pady=5)
        self.txtClient.grid(row=1,column=3,sticky=W+E,padx=5,pady=5)
        self.txtRequestor.grid(row=2,column=1,sticky=W+E,padx=5,pady=5)
        self.txtInstance.grid(row=2,column=3,sticky=W+E,padx=5,pady=5)
        self.txtDescription.grid(row=3,column=1,sticky=W+E,columnspan=4,padx=5,pady=5)
        self.txtBox.grid(row=4,column=0,sticky=W+E+N+S,columnspan=5,padx=5,pady=5)
        self.btnOK            =   Button(self.window,text="Create",width=15,command=self.btnClick)
        self.btnCancel        =   Button(self.window,text="Cancel",width=15,command=self.window.destroy).grid(row=1,column=4,sticky=W+E,padx=5,pady=5)
        self.btnConfigure     =   Button(self.window,text="Configure",width=15,command=self.window.destroy,state=DISABLED).grid(row=2,column=4,sticky=W+E,padx=5,pady=5)        
        self.window.grid_columnconfigure(0,weight=0)
        self.window.grid_columnconfigure(1,weight=1)
        self.window.grid_columnconfigure(2,weight=0)
        self.window.grid_columnconfigure(3,weight=1)
        self.window.grid_columnconfigure(4,weight=0)
        self.window.grid_rowconfigure(4,weight=1)
        self.btnOK.grid(row=0,column=4,sticky=W+E,padx=5,pady=5)

    def btnClick(self):
        # make some validation here!
        mySRQ=func.SRQProject(  SRQ     =   self.SRQ.get(),
                                RFC     =   self.RFC.get(),
                                Site    =   self.Site.get(),
                                Client  =   self.Client.get(),
                                Description=self.Description.get())
        folder=myFolders=mySRQ.createFolders()
        subprocess.Popen('explorer "%s"' % folder)    
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    guiFrame = CreateSRQ()
    guiFrame.run()