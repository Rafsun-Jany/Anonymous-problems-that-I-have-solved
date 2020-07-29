import os

parent_path = "E:\\Downloads\\Physics_Lab\\TA\\Sec_6(HrR_Sir)\\Students"
file1 = open("E:\\Downloads\\Physics_Lab\\TA\\Sec_6(HrR_Sir)\\students.txt", "r")
lines = file1.readlines()
count = 1
for i in lines:
    new_folder = str(count) + ". " + str(i.rstrip())
    new_folder = str(new_folder)
    path = os.path.join(parent_path, new_folder)
    os.mkdir(path)
    count += 1
