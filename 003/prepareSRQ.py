from tkinter import *
import subprocess
import func

window = Tk()
window.title("SRQ WorkFiles")
# define window layout
lblSRQ          =   Label(window,width=4,anchor=E,text="SRQ:").grid(row=0,column=0)
lblRFC          =   Label(window,width=4,anchor=E,text="RFC:").grid(row=0,column=2)
lblInstance     =   Label(window,width=8,anchor=E,text="Instance:").grid(row=0,column=4)
lbl4            =   Label(window,width=10,anchor=E,text="Requestor:").grid(row=1,column=0)
lbl5            =   Label(window,width=10,anchor=E,text="Description:").grid(row=2,column=0)
#--
txtSRQ          =   Entry(window,width=20).grid(row=0,column=1,sticky=W+E,padx=5,pady=5)
txtRFC          =   Entry(window,width=20).grid(row=0,column=3,sticky=W+E,padx=5,pady=5)
txtInstance     =   Entry(window,width=10).grid(row=0,column=5,sticky=W+E,padx=5,pady=5)
txtRequestor    =   Entry(window,width=44).grid(row=1,column=1,sticky=W+E,columnspan=5,padx=5,pady=5)
txtDescription  =   Entry(window,width=40).grid(row=2,column=1,sticky=W+E,columnspan=5,padx=5,pady=5)
# buttons
btnClose=   Button(window,text="Cancel",command=window.destroy).grid(row=5,column=1)
# textbox
txtBox          =   Text(window,height=20).grid(row=6,column=0,sticky=W+E+N+S,columnspan=6,padx=5,pady=5)
# configure grid weight; the more weight - the more widget resizes on root container resize.
window.grid_columnconfigure(0,weight=0)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=0)
window.grid_columnconfigure(3,weight=1)
window.grid_columnconfigure(4,weight=0)
window.grid_columnconfigure(5,weight=1)
window.grid_rowconfigure(6,weight=1)
window.mainloop()

# mySRQ=func.SRQProject(SRQ="00011123",RFC="997",Site="CABRAMPTO1",Client="CASEPHBC",Description="CW: Print costam > pliku")
# folder=myFolders=mySRQ.createFolders()
# subprocess.Popen('explorer "%s"' % folder)
