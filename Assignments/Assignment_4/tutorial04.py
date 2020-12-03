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


lis=[]
for roll in roll_no_list:
    file=open('./grades/'+roll+'_individual.csv','r')
    with file:
        reader=csv.reader(file)
        for row in reader:
            if(re.fullmatch(valid_entry_check,row[0])):
                lis.append(row)
    slis=sorted(lis,key=lambda l:l[4])
    lis.clear()
    main_file = open('./grades/'+roll+'_overall.csv', 'a',newline='')
    with main_file:
        main_writer=csv.writer(main_file)
        main_writer.writerow(['Roll: '+roll])
        main_writer.writerow(['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI'])
    grades = {'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0}
    total_credits=0
    total_credits_cleared=0
    evry_Sem_included_total=0
    evry_Sem_cleared_total=0
    cursem='W'
    semester_performance_index=0
    cumulative_performance_index=0
    for row in slis:
        if(cursem=='W'):
            cursem=row[4]
        if(cursem==row[4]):
            total_credits+=int(row[1])
            total_credits_cleared+=int(row[1])
            evry_Sem_cleared_total+=int(row[1])
            semester_performance_index+=(grades[row[3]]*int(row[1]))
            evry_Sem_included_total+=int(row[1])
        else:
            cumulative_performance_index+=semester_performance_index
            lisc=[cursem,total_credits,total_credits_cleared,semester_performance_index/total_credits,evry_Sem_included_total,evry_Sem_cleared_total,cumulative_performance_index/evry_Sem_included_total]
            main_file = open('./grades/'+roll+'_overall.csv', 'a',newline='')
            with main_file:
                main_writer=csv.writer(main_file)
                main_writer.writerow(lisc)
            cursem=row[4]
            total_credits=int(row[1])
            total_credits_cleared=int(row[1])
            evry_Sem_cleared_total+=int(row[1])
            semester_performance_index=(grades[row[3]]*int(row[1]))
            evry_Sem_included_total+=int(row[1])
            
    cumulative_performance_index+=semester_performance_index
    lisc=[cursem,total_credits,total_credits_cleared,semester_performance_index/total_credits,evry_Sem_included_total,evry_Sem_cleared_total,cumulative_performance_index/evry_Sem_included_total]
    main_file = open('./grades/'+roll+'_overall.csv', 'a',newline='')
    with main_file:
        main_writer=csv.writer(main_file)
        main_writer.writerow(lisc)

#  *****HAPPY DIWALI***** 