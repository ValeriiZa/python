import os

os.chdir("c:\\Users\\admin\\Documents\\Invest\\3\\Продовження розслідування\\1\\")
os.getcwd()

files_list = os.listdir()
join_fname = "На продовження "

for f in files_list:
    if not f.startswith('.'):
        os.rename(f, join_fname + f)
