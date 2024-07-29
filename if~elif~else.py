import datetime

today=datetime.datetime.now()
if today.weekday()<4:
    print('まだ頑張る')
elif today.weekday()==4:
    print('あと１日頑張る')
else:
    print('休み')