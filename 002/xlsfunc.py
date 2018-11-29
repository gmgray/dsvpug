"""
Module for simple and easy creating  XLS files
"""
import xlwt

class xls:
    """
    xls class represents simple xls file. 
    You can set filename, title and sheet name during class initialization.
    if description is given, then it will be added below title.    
    """
    def __init__(self, filename='output.xls',title='Created with Python and XLWT',sheet='Python is awesome!',description=None):
        self.filename       = filename
        self.title          = title
        self.sheet          = sheet
        self.__styleBold    = xlwt.easyxf('font: bold on')
        self.__styleItalic  = xlwt.easyxf('font: italic on')
        self.__workbook     = xlwt.Workbook()
        self.__sheet        = self.__workbook.add_sheet(sheet)
        self.row            = 0
        self.column         = 0
        self.description    = description
        # add a title 
        self.__sheet.write(self.row,self.column,self.title,self.__styleBold)
        self.row += 1        
        if self.description:
            self.__sheet.write(self.row,self.column,self.description,self.__styleItalic)
            self.row += 1
        
    def feed(self,data=[]):
        """Feed the data into excel.
        Data has to be a list of list, or array of arrays, etc.
        """        
        try:
            #iterate through rows:
            for _row in data:
                #iterate through columns:
                if (isinstance(_row,str) or isinstance(_row,int)):
                    self.__sheet.write(self.row,self.column,_row)
                    self.row += 1
                    self.column = 0
                else:
                    for _column in _row:
                        self.__sheet.write(self.row,self.column,_column)                
                        #increment column
                        self.column += 1
                #next row here: increment row, reset colum
                    self.row += 1
                    self.column = 0
        except:
            print("Not valid data format. Cannot convert it to table!")
            

    def save(self):
        """
        Save the sheet to file defined in .filename.
        """
        self.__workbook.save(self.filename)


    
    