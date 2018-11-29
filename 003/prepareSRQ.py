import subprocess
import func
mySRQ=func.SRQProject(SRQ="00011123",RFC="997",Site="CABRAMPTO1",Client="CASEPHBC",Description="CW: Print costam > pliku")
folder=myFolders=mySRQ.createFolders()
subprocess.Popen('explorer "%s"' % folder)