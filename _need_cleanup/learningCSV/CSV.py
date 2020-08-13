

import csv

with open('mylist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print csv_reader
    for row in csv_reader:
        for i in row:
            print i + ",",
        print ""

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')

    employee_writer.writerow(['John Smith', 'Swappy', 'Anshuma'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])




