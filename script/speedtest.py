import os

os.system("speedtest > result-temp.txt")
os.system("sed -i 's/ //g' ./result-temp.txt")

os.system("touch result.txt")

list_result = []

with open('result-temp.txt', 'r') as f:
    for line in f:
        if 'Download' in line or 'Upload' in line:
            part = line.split('(')
            list_result.append(part[0])

with open('result.txt', 'w') as s:
    s.write(str(list_result[0]) + '\n')
    s.write(str(list_result[1]))


os.system('rm result-temp.txt')