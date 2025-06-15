import shutil, os, re

print("input name: ")
name = input()
print("input directory")
direct = input()
pattern = re.compile(r'.*\.jpe?g', re.IGNORECASE)
n = '001'

for file in os.listdir(str(direct)):
    photo = pattern.search(file)
    # check the file if it's a photo file
    # returns a match object
    # returns None if it fails to match the pattern

    if not photo:
        continue
    # if it's not a file, skip it 
    _, extension = os.path.splitext(file)
    new_name = str(name) + "_" + n + extension
    workingDir = os.path.abspath(str(direct))
    old_file = os.path.join(workingDir, file) 
    new_file = os.path.join(workingDir, new_name)
    # .join is better
    # concatenting often times misses using slashes 
    n = str(int(n) + 1).zfill(3)
    shutil.move(old_file, new_file)

print("done")
