# importing modules and library
import os
import csv
import re
import shutil
import datetime


if(os.path.isdir(r'./grades')):
    shutil.rmtree('./grades')
os.makedirs('./grades')


roll_no_list=[]

col_names=['sl','roll','sem','year','sub_code','total_credits','credit_obtained','timestamp','sub_type']

roll_no_check=re.compile(r'^[0-9]{4}[A-Za-z]{2}[0-9]{2}$')

sem_credit_check=re.compile(r'^[0-9]+$')

valid_entry_check=re.compile(r'^[A-Z]{2}[0-9]{3}$',re.I)

credit_check=re.compile(r'AA|AB|BC|BB|CC|CD|DD|I|F',re.I)


# misc file for error realted entries
file=open('./grades/misc.csv','a',newline='')
with file:
    main_writer=csv.writer(file)
    main_writer.writerow(col_names)


# creating files for a particluar student excluding misc things
file=open('./acad_res_stud_grades.csv','r')
with file:
        reader=csv.reader(file)
        for row in reader:
            if(not row[0]=='sl'):
                if(not (re.fullmatch(roll_no_check,row[1]) and re.fullmatch(sem_credit_check,row[2]) and re.fullmatch(sem_credit_check,row[5]) and re.fullmatch(valid_entry_check,row[4]) and re.fullmatch(credit_check,row[6]))):
                    file=open('./grades/misc.csv','a',newline='')
                    with file:
                        main_writer=csv.writer(file)
                        main_writer.writerow(row)
                    continue
                roll_no=row[1]+'_individual.csv'
                if(not os.path.isfile('./grades/'+roll_no)):
                    roll_no_list.append(row[1])
                    main_file = open('./grades/'+roll_no, 'a',newline='')
                    with main_file:
                        main_writer=csv.writer(main_file)
                        main_writer.writerow(['Roll: '+row[1]])
                        main_writer.writerow(['Semester Wise Details'])
                        main_writer.writerow(['Subject','Credits','Type','Grade','Sem'])
                list1=[row[4],row[5],row[8],row[6],row[2]]
                main_list = open('./grades/'+roll_no, 'a',newline='')
                with main_list:
                    main_writer=csv.writer(main_list)
                    main_writer.writerow(list1)
