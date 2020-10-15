import csv
import os
import shutil

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
            if roll[2:4] in ['01','11','12','21']:
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
    pass


cols=['id','full_name','country','email','gender','dob','blood_group','state'] 

def course():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as f:
        reader=csv.DictReader(f)
        make('analytics')
        make('course')
        not_useful=[]
        i=0
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
            if i>5:
                break
            i+=1        

        with open('misc.csv','w',newline='') as file:
            ad_data = csv.DictWriter(file,fieldnames=cols)
            ad_data.writeheader()
            ad_data.writerows(not_useful)    
    delet(1)
    # print(os.getcwd())
    # os.chdir(os.path.split(os.path.split(os.getcwd())[0])[0])
    # delet(2)
    # print(os.getcwd())

    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

