import os
from zipfile import ZipFile

file_name = "geschenk.zip"
path = "data/"
job_done = False


#run until all files are unzipped
while job_done != True:

    #unzip file
    with ZipFile(path + file_name, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print('Extracting files')
        zip.extractall(path)
        print('Done!\n')

    pathContent = os.listdir(path)

    if len(pathContent)>1:
        pathContent.remove(file_name)
        os.remove(path+file_name)
        file_name = pathContent[0]

    else:
        job_done = True

print("Process finsihed, please check folder")