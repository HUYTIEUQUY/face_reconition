


a={"1911020030":{"ma":"1911020030","thongtin":"có", "tgvao":"11:00:00", "tgra":"12:00:00"},
"1911020031":{"ma":"1911020033","thongtin":"không", "tgvao":"", "tgra":""},
}

a['1911020030']['thongtin']="không"


e=[]
j=[]
for i in a:
    e=[a[i]['ma'],a[i]['thongtin'],a[i]['tgvao'],a[i]['tgra']]
    j.append(e)
print(j)
