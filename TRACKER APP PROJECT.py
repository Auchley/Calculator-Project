from datetime import date
import csv

dt = date.today()
dt = dt.strftime('%d/%m/%y')

filename = "test.csv"
exp = []
stopped = False
with open(filename, 'a',newline='') as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input('what is the expense (type 0 to stop): '))
        if xp==0:
            stopped = True
        else:
            csvwriter.writerow([dt,xp])
            exp.append(xp)
file.close()
print('Your expenses today are, ',exp)
print('Your total is',sum(exp))