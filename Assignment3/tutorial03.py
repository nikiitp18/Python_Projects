import csv
import os
import shutil
import datetime

#  To traverse forward
def make(c):
    try:
        os.mkdir(f'{c}')
    except:
        pass
    os.chdir(f'{c}')   

#  To traverse backwards
def delet(level):
    c=os.getcwd()
    for i in range(level):
        s=os.path.split(c)[0]
        c=s
        i+=1
    os.chdir(c)    

#  Roll number checker
def roll_no_check(roll):
    if(len(roll)!=8):
        return False
    else:
        if roll[0:4].isdigit() and roll[4:6].isalpha() and roll[6:8].isdigit():
            if roll[2:4] in ['01','11','12','21']: # just to check that it is valid or not it's not used for file naming
                return True 
            else:
                return False    
        else:
            return False                      


def del_create_analytics_folder():
    # del the analytics folder including subfolder
    make('analytics')
    try:
        shutil.rmtree(os.getcwd())
    except:
        pass
    delet(1)
    os.rmdir('analytics')

    # mkdir the analytics folder (only mkdir)
    make('analytics')
    delet(1)
    pass


cols=['id','full_name','country','email','gender','dob','blood_group','state'] 

def course():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('course')
        not_useful=[]
        for row in reader:
            # print(rno[:4],rno[4:6],rno[6:8])
            print(dict(row)['id'])
            roll_no=dict(row)['id']  
            if roll_no_check(roll_no):
                branch = (roll_no[4:6]).lower()
                make(branch) # making branch folder 
                program_code=roll_no[2:4]
                program = ''
                if program_code=='01':
                    program="btech"
                    make(program)
                elif program_code=='11':
                    program="mtech"
                    make(program)
                elif program_code=='12':
                    program="msc"
                    make(program)
                else:
                    program="phd"
                    make(program)
                year_of_admi = roll_no[0:2]

                new_file = year_of_admi +'_'+ branch +'_'+ program + '.csv'

                with open(new_file,'a+',newline='') as file:
                    ad_data = csv.DictWriter(file,fieldnames=cols)
                    ad_data.writerow(row)
                delet(2)

            else:
                not_useful.append(row) 

        if len(not_useful)>0:
            with open('misc.csv','w',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=cols)
                ad_data.writeheader()
                ad_data.writerows(not_useful)   
    delet(2)
    # print(os.getcwd())
    # os.chdir(os.path.split(os.path.split(os.getcwd())[0])[0])
    # delet(2)
    # print(os.getcwd())

    pass


def country():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('country')
        not_useful=[]
        # i=0
        for row in reader:
            country_name=(dict(row)['country']).lower()
            # print(country_name)
            if len(country_name)!=0:
                new_file = country_name + '.csv'
                with open(new_file,'a+',newline='') as file:
                    ad_data = csv.DictWriter(file,fieldnames=cols)
                    ad_data.writerow(row)
            else:
                not_useful.append(row)  

        if len(not_useful)>0:
            with open('misc.csv','w',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=cols)
                ad_data.writeheader()
                ad_data.writerows(not_useful)
            #     break
            # i+=1    
    delet(2)  

    pass


def email_domain_extract():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('email_domain')
        not_useful=[]
        # i=0 
        for row in reader:
            email=(dict(row)['email']).lower()
            # print(country_name) 
            name_domain = email.split('@')
            if len(name_domain)==2:
                domain_with_addres = (name_domain[1]).split('.')
                if len(domain_with_addres)>1:
                    ch=''
                    chek1=1
                    for g in domain_with_addres:
                        if not g.isalpha():
                            chek1=0
                            break
                    if chek1==1:
                        if ch not in domain_with_addres:
                            new_file = domain_with_addres[0] + '.csv'
                            with open(new_file,'a+',newline='') as file:
                                ad_data = csv.DictWriter(file,fieldnames=cols)
                                ad_data.writerow(row)
                        else:
                            not_useful.append(row)         
                    else:
                        not_useful.append(row)       
                else:
                    not_useful.append(row)         
            else:
                not_useful.append(row) 

        if len(not_useful)>0:
            with open('misc.csv','w',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=cols)
                ad_data.writeheader()
                ad_data.writerows(not_useful)              
            # if i>5: 
            #     break 
            # i+=1    
    delet(2) 

    pass


def gender():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('gender')
        not_useful=[]
        # i=0
        for row in reader:
            std_gender=(dict(row)['gender']).lower()
            # print(std_gender)
            if std_gender=='f' or std_gender=='female':
                new_file = 'female.csv'
                with open(new_file,'a+',newline='') as file:
                    ad_data = csv.DictWriter(file,fieldnames=cols)
                    ad_data.writerow(row)
                # if i>5:
                #     break
                # i+=1 
            elif std_gender=='m' or std_gender=='male':
                new_file = 'male.csv'
                with open(new_file,'a+',newline='') as file:
                    ad_data = csv.DictWriter(file,fieldnames=cols)
                    ad_data.writerow(row)
                # if i>5:
                #     break
                # i+=1       
        if len(not_useful)>0:
            with open('misc.csv','w',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=cols)
                ad_data.writeheader()
                ad_data.writerows(not_useful) 

    delet(2)

    pass


def dob():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('dob')
        not_useful=[]
        # i=0
        for row in reader:
            inputDate=(dict(row)['dob']).lower()
            day,month,yr = inputDate.split('-')
            isValidDate = True
            try :
                datetime.datetime(int(yr),int(month),int(day))
            except ValueError :
                isValidDate = False 
            # print(country_name)
            if isValidDate:
                year=(int)(yr)
                if((year >= 1995) and (year <= 1999)):
                    new_file =  'bday_1995_1999' + '.csv'
                    with open(new_file,'a+',newline='') as file:
                        ad_data = csv.DictWriter(file,fieldnames=cols)
                        ad_data.writerow(row)
                elif(year <= 2004):
                    new_file =  'bday_2000_2004' + '.csv'
                    with open(new_file,'a+',newline='') as file:
                        ad_data = csv.DictWriter(file,fieldnames=cols)
                        ad_data.writerow(row)
                elif(year <= 2009):
                    new_file =  'bday_2005_2009' + '.csv'
                    with open(new_file,'a+',newline='') as file:
                        ad_data = csv.DictWriter(file,fieldnames=cols)
                        ad_data.writerow(row)
                elif(year <= 2014):
                    new_file =  'bday_2010_2014' + '.csv'
                    with open(new_file,'a+',newline='') as file:
                        ad_data = csv.DictWriter(file,fieldnames=cols)
                        ad_data.writerow(row)
                elif(year <= 2019):
                    new_file =  'bday_2015_2019' + '.csv'
                    with open(new_file,'a+',newline='') as file:
                        ad_data = csv.DictWriter(file,fieldnames=cols)
                        ad_data.writerow(row)  
                else:
                    not_useful.append(row)           
            else:
                not_useful.append(row)  
        if len(not_useful)>0:
            with open('misc.csv','w',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=cols)
                ad_data.writeheader()
                ad_data.writerows(not_useful)              
            # if i>5:
            #     break
            # i+=1    
    delet(2)  

    pass


def state():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('state')
        not_useful=[]
        # i=0
        for row in reader:
            state_name=(dict(row)['state']).lower()
            # print(country_name)
            if len(state_name)!=0:
                new_file = state_name + '.csv'
                with open(new_file,'a+',newline='') as file:
                    ad_data = csv.DictWriter(file,fieldnames=cols)
                    ad_data.writerow(row)
            else:
                not_useful.append(row)  

        if len(not_useful)>0:
            with open('misc.csv','w',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=cols)
                ad_data.writeheader()
                ad_data.writerows(not_useful)              
            # if i>5:
            #     break
            # i+=1 
    delet(2)

    pass


def blood_group():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('blood_group')
        not_useful=[]
        checker=['a-','a+','b+','b-','o+','o-','ab-','ab+'] # just to check that it is valid or not it's not used for file naming
        # i=0
        for row in reader:
            std_blood_grp=(dict(row)['blood_group']).lower()
            if len(std_blood_grp)!=0:
                if std_blood_grp in checker:
                    new_file = std_blood_grp + '.csv'
                    with open(new_file,'a+',newline='') as file:
                        ad_data = csv.DictWriter(file,fieldnames=cols)
                        ad_data.writerow(row)
                else:
                    not_useful.append(row)       
            else:
                not_useful.append(row)  

        if len(not_useful)>0:
            with open('misc.csv','w',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=cols)
                ad_data.writeheader()
                ad_data.writerows(not_useful)             
            # if i>5:
            #     break
            # i+=1 
    delet(2)

    pass
chec=True
# To create new file with 'split' added at last in the name of the file
def new_file():
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        new_cols=['id','first_name','last_name','country','email','gender','dob','blood_group','state'] 
        # i=0
        for row in reader:
            first_name,last_name=(dict(row)['full_name']).split(' ')
            new_file =  'studentinfo cs384 names split'+'.csv'
            if chec:
                with open(new_file,'a+',newline='') as file:
                    ad_data = csv.Writer(file)
                    ad_data.writerow(['id','first_name','last_name','country','email','gender','dob','blood_group','state'])
                    chec=False
            with open(new_file,'a+',newline='') as file:
                ad_data = csv.DictWriter(file,fieldnames=new_cols)
                ad_data.writerow([dict(row)['id'],first_name,last_name,dict(row)['country'],dict(row)['email'],dict(row)['gender'],dict(row)['dob'],dict(row)['blood_group'],dict(row)['state']])
            
    delet(1)

    pass

# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

new_file()