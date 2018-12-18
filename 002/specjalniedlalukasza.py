from xlsfunc import xls
lukaszowyplik=xls(filename='fiutek.xls',title='Ania',description="Ładna",sheet='PS jest gupi')
dane=[(1,2),
    (3,4),
    "234444",
    23452345254,
    ("1234134","asdgfasdfa"),]

lukaszowyplik.feed(dane)
lukaszowyplik.save()