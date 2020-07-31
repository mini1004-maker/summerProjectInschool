#전처리 1 평균 평점 없는 데이터 선별
import glob
import os
import shutil
import os
files = glob.glob('*.txt')
try:
    if not(os.path.isdir("empty")):
        os.makedirs(os.path.join("empty"))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

for file in files:
    with open(file, 'r') as f:
        element_txt=f.read().split(';')
        if(element_txt[3].strip()==""):
            
            shutil.copy(file, "empty/"+file)
files = glob.glob('empty/*.txt')


for file in files:
    try:
        os.remove(file[6:])
    except:
        pass
