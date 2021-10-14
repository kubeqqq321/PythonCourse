# file detection---------------------------------------------------------
#------------------------------------------------------------------------
import os

path = "D:\\Python Projects Community\\21_FILES\\test.txt"
# path = "D:\\Python Projects Community\\21_FILES\\test"

if os.path.exists(path):
    print("The location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("This location doesn't exists!")




#write to file-----------------------------------------------------------
#------------------------------------------------------------------------
print("")

#text = "Yoooooooooo\nThis is awesome, you can do that\nHave a nice day :)\n"
text = "Uh oh! This text hasn't been overwritten\n"

# r - read file
# w - write to file (nadpisuje zawartośc pliku)
# a - append to file (nie nadpisuje zawartośći tylko dodaje nową linie)

with open(path, 'a') as file:
    file.write(text)




#read from file----------------------------------------------------------
#------------------------------------------------------------------------
print("")

try:
    # with open("D:\\Python Projects Community\\21_FILES\\test.txt") as file:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found :( ")




#copy a file-------------------------------------------------------------
#------------------------------------------------------------------------
# copyfile() - copies contents of a file
# copy() -     copyfile() + permission mode + destination can be directory
# copy2() -    copy() + copies metadata (file's creation and modification times)
print("")
import shutil

shutil.copyfile('test.txt' , 'copyfile.txt') #source , destination
shutil.copy('test.txt' , 'copy.txt') #source , destination
shutil.copy2('test.txt' , 'copy2.txt') #source , destination
#shutil.copyfile('test.txt' , "D:\\Python Projects Community\\21_FILES\\copy.txt")




#move a file-------------------------------------------------------------
#------------------------------------------------------------------------

import os

source = 'copy.txt'
destination = "D:\\Python Projects Community\\21_FILES\\move\\copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found :()")



#delete a file-----------------------------------------------------------
#------------------------------------------------------------------------

import os
import shutil

path = "copy.txt"
path_directory = "empty_folder"

try:
    os.remove(path)                  # usuwa plik
    os.rmdir(path_directory)          # usuwa cały folder jendnak jeżeli są w nim plikki nie zrobi tego
    shutil.rmtree(path_directory)     # usuwa cały folder razem ze wszystkimi plikami w środku
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not permission to delete that!")
except OSError:
    print("You cannot delete that using that function! ")
else:
    print(path_directory + " deleted")



