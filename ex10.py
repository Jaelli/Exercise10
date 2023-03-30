import sys
import glob
import os
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*.*')
print(glob.glob(pattern))

from os.path import getsize
from os.path import basename

# TODO: Use the glob.glob() function to obtain the list of filenames
print("# TODO: Use the glob.glob() function to obtain the list of filenames")
print(glob.glob(pattern))

# TODO: use os.path.getsize to find each file's size
print("# TODO: use os.path.getsize to find each file's size")
for f in glob.glob(pattern):
    print(f, os.path.getsize(f))

# TODO: Add a test to only display files that do not have a size of zero
print("# TODO: Add a test to only display files that do not have a size of zero")
for f in glob.glob(pattern):
    if os.path.getsize(f) > 0:
        print(f, os.path.getsize(f))

# TODO: Remove the leading directory name(s) from each filename before you print it -
print("# TODO: Remove the leading directory name(s) from each filename before you print it -")
# using os.path.basename()
for f in glob.glob(pattern):
    if os.path.getsize(f) > 0:
        print(os.path.basename(f), os.path.getsize(f))

for file in glob.glob(pattern):
    name = os.path.basename(file)
    size = int(os.path.getsize(file))
    if size > 0:
        print(name, size)
