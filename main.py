import os.path
from os import listdir
from os.path import isfile, join
from os.path import isdir

data_types = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.webp': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.pdf': 'Documents',
    '.pptx': 'Documents',
    '.docx': 'Documents',
    '.epub': 'Documents',
    '.txt': 'Documents',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.opus': 'Audio',
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.py': 'Scripts',
    '.jar': 'Scripts',
    '.exe': 'Programs',
    '.dll': 'Programs',
    '.ini': 'Programs',
    '.msi': 'Programs',
    '.json': 'Web',
    '.html': 'Web',
    '.unitypackage': 'Game Dev'
}

path = r"DOWNLOAD_FOLDER"

# create dirs
folder_list = []

for value in data_types.values():
    folder_list.append(value) if value not in folder_list else None

for folder in folder_list:
    dir = os.path.join(path, folder)
    if not isdir(dir):
        os.mkdir(dir)

# files -> ext
files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    _, extension = os.path.splitext(file)
    folder = data_types[extension]
    # ext -> folder
    file_dir_old = os.path.join(path, file)
    file_dir_new = os.path.join(path, folder, file)

    os.rename(file_dir_old, file_dir_new)
