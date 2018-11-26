from xlsfunc import xls

myXls=xls()
myData=[(1,2,3,4,5,6,7,8),(2,3,4,2,5,3,),("One","Two","Three",4432),(2345,2,5,333,5,3,2)]
myXls.feed(myData)
myXls.save()

secondXls=xls(description='Another file',filename='second.xls')
myData=[(1,2,3,4,5,6,7,8),
        (2,3,4,2,5,3,),
        ("One","Two","Three",4432),
        (2345,2,5,333,5,3,2),
        ('And this is some line single in a row...',)]
secondXls.feed(myData)        
secondXls.save()