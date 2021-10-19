import datetime

date1 = datetime.datetime.strptime('10/12/2013', '%m/%d/%Y')
date2 = datetime.datetime.strptime('10/15/2013', '%m/%d/%Y')


print(date1<date2)