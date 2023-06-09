import sys
import glob
import os
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
# TODO: Use the glob.glob() function to obtain the list of filenames
# TODO: use os.path.getsize to find each file's size
# TODO: Add a test to only display files that do not have a size of zero
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

files = glob.glob("*.py")
print(files)

from os.path import getsize
from os.path import basename

filePath = 'main.py', 'ex10.py', 'empty.py'
for file in filePath:
    fileSize = getsize(filePath)
    print('File Size; ', fileSize)

