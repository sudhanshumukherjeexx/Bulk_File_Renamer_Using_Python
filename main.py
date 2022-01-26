import os

def main():
    i = 0
    path = "D:/Sensei's Den/Data Science/Projects/Python Projects/Bulk File Renamer/images/"
    for filename in os.listdir(path):
        my_filesname = "img" + str(i) + ".jpg"
        my_source =path + filename
        my_filesname =path + my_filesname
        os.rename(my_source, my_filesname)
        i += 1

if __name__ == '__main__':
    main()

