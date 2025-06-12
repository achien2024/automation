import shutil, os, re

print("input name: ")
name = input()
print("input directory")
direct = input()

for photo in os.listdir(str(direct)):

    new_name = str(name) + "_" + str(photo)
    workingDir = os.path.abspath(str(direct))
    old_file = os.path.join(workingDir, photo) 
    new_file = os.path.join(workingDir, new_name)
    # .join is better
    # concatenting often times misses using slashes 

    shutil.move(old_file, new_file)

print("done")
