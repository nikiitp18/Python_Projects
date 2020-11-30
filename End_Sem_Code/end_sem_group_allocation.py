import pandas as pd
import os
import shutil
import re
import csv


def group_allocation(filename, number_of_groups):
    # Entire Logic
    # You can add more functions, but in the test case, we will only call the group_allocation() method,

    #  declaring dictionary with branch_code as key 
    Btech_2020_data = {}

    # file path
    cd = os.getcwd()

    # extracting students info
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            roll_no = row[0]

            #  checking for valid roll_no
            if not re.match('[0-9]{4}\w+', roll_no):
                continue

            # extracting branch name using roll_no
            branch_code = roll_no[4:6]

            # checking if this key exist in our dictionary or not
            if branch_code not in Btech_2020_data:
                Btech_2020_data[branch_code] = []
            Btech_2020_data[branch_code].append(row)

    # extracting number of students in each branch
    branch_strength = {}
    for branch_code in Btech_2020_data:
        total_std_cnt = 0
        for std_data in Btech_2020_data[branch_code]:
            total_std_cnt+=1;
        branch_strength[branch_code] = total_std_cnt

    # sorted by STRENGTH, if there is a clash then branch code is prefered in lexicographical order
    list_branch_strength_sort = sorted(branch_strength.items(), reverse=True,key=lambda x: x[1])

    # task - 1 is implemented
    student_file_data = os.path.join(cd, 'branch_strength.csv')
    with open(student_file_data, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['BRANCH_CODE', 'STRENGTH'])
        for detail in list_branch_strength_sort:
            branch_code = detail[0]
            branch_strength = detail[1]
            writer.writerow([branch_code, branch_strength])

    # task - 2 is implemented
    for branch_code in Btech_2020_data:
        # file for particular branch code
        file_name = os.path.join(cd, branch_code.upper() + '.csv')
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)

            #  declaring column names in csv file
            writer.writerow(['Roll', 'Name', 'Email'])
            for row in Btech_2020_data[branch_code]:
                # extracting roll no, name , email
                Roll_no = row[0]
                Name = row[1]
                Email = row[2]
                writer.writerow([Roll_no, Name, Email])


    group_data = {}
    # students left after equal distribution
    remaining_students = {}     
    for num in range(1, number_of_groups+1,1):
        # declaring group number
        if num-10 < 0:
            group_number = 'G0'+str(num)
        else:
            group_number = 'G'+str(num)
        if group_number not in group_data:
            group_data[group_number] = {}
        for detail in list_branch_strength_sort:
            # extracting details
            branch_code = detail[0]
            branch_strength = detail[1]
            # equal distribution of students in each group
            group_data[group_number][branch_code] = branch_strength//number_of_groups
            # storing the remaining number of childs in each branch
            remaining_students[branch_code] = branch_strength - (number_of_groups * (branch_strength//number_of_groups))


filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)