"""Set of helpers for creating SRQ project folders"""
import os
import re
from shutil import copyfile

# some const here:

#FOLDER_ROOT: here is the main folder containing all the new directories
FOLDER_ROOT = "C:\\Users\\gabriel.milczarek\\OneDrive - DSV\\CRQ\\2. Active"
UAT_FILE    = "C:\\Users\\gabriel.milczarek\\OneDrive - DSV\\CRQ\\SRQ9999999 User Acceptance Test Form Result.xlsx"
SDD_FILE    = "C:\\Users\\gabriel.milczarek\\OneDrive - DSV\\CRQ\\Solutions Deploy Document SRQ9999999.docm"


class SRQProject():
    """Represents all the data connected to the project:
    SRQ number, RFC number, Site, Client, Requestor, Description
    can create folder structure for a given project."""
    
    def __init__(self,SRQ=0,RFC=0,Site='NLCWIT',Client='None',Requestor='None',Description='None'):
        "Initialise default values for SRQProject object"
        self.SRQ        =   SRQ            
        self.RFC        =   RFC
        self.Site       =   Site
        self.Client     =   Client
        self.Requestor  =   Requestor
        self.Description=   Description.replace(':','').replace('>','2').replace('!','')
        #self.Description=   Description
        self.__folder__ = None

    def createFolders(self):
        """Creates workfolder with name created from SRQ parameters,
        subfolders for workfiles and deployer files,
        and copies template Solution Deployment and UAT Documents."""
        vDir= "%s_%s [%s.%s] %s" % (self.RFC,self.SRQ,self.Site,self.Client,self.Description)
        try:
            self.__folder__=os.sep.join([FOLDER_ROOT,vDir])
            os.mkdir(self.__folder__)
            os.mkdir(os.sep.join([self.__folder__,'DEPLOYER']))
            os.mkdir(os.sep.join([self.__folder__,'WRK']))
        except FileExistsError:
            print("Warning: folder exists already, I won't fuck off with it and leave as it is!")
        except:
            print("ERROR: Cannot create folder %s" % self.__folder__)
            exit()
        print("%s created successfully" % self.__folder__)
        try:
        #     # Copy UAT file
            __uat_fullpath=os.path.join(self.__folder__,UAT_FILE.split('\\')[-1].replace('9999999',self.SRQ))        
            print("Copy %s to %s"%(UAT_FILE,__uat_fullpath))
            copyfile(UAT_FILE,__uat_fullpath)
    #     # Copy SDD File
            __sdd_fullpath=os.path.join(self.__folder__,'DEPLOYER',SDD_FILE.split('\\')[-1].replace('9999999',self.SRQ))        
            print("Copy %s to %s"%(SDD_FILE,__sdd_fullpath))
            copyfile(SDD_FILE,__sdd_fullpath)
        except:
             print("ERROR: Cannot copy template files")
             exit()
        return self.__folder__
