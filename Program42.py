#Reading in CSV files into Python
import csv
with open('data.csv', 'r+') as csvfile:
    readit = csv.reader(csvfile, delimiter=',')
    print('Last' +'\t' + '    First' +'\t' + 'Salary')
    for row in readit:
        curline = ''
        for i in row:
            curline = curline + i + '\t\t'
        print(curline)
