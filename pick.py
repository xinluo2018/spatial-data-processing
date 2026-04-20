import pandas as pd
import numpy as np

def pick():
    path_stud = '课程考核记录/2026春/students_hometown_2026.csv'
    stud_info = pd.read_csv(path_stud)
    name_stud = stud_info['姓名']
    num_stud = len(name_stud)
    i = np.random.randint(num_stud)
    return name_stud[i]

name = pick()
print(name)