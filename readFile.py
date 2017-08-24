import glob
import re
import os
lst = []
directory = {}
files = []
path = "Testfiles\/"
def read_file():
    for filename in glob.glob(os.path.join(path, '*.txt')):
        #File reading
        f = open(filename,'r')
        st = re.sub(r'[^a-z0-9_\n]', ' ', f.read().lower())
        # st=f.read().lower()
        f.close()
        #Directory of files
        file_name = filename.split('\\')
        file=""
        for i in file_name:
            if path.find(i) == -1:
                file += i
        files.append(file)
        directory[file] = st
    print(directory)