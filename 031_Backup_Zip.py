# Backup Program
# Copies an entire folder and its contents into
# a zip file whose filename will increments

import zipfile, os

def backupToZio(folder):
  folder = os.path.abspath(folder)
  
  number = 1
  while True:
    zipFile = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exits(zipFilename):
      break
     number = number + 1
