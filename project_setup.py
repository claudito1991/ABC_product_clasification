import os
import sys
#from setuptools import setup, find_packages

def create_folders(folder_1, folder2):
    root_dir = os.path.dirname(sys.executable)
    folder1_path = os.path.join(root_dir, 'entrada_abc')
    folder2_path = os.path.join(root_dir, 'salida_abc')
    os.makedirs(folder1_path, exist_ok=True)
    os.makedirs(folder2_path, exist_ok=True)


# create_folders()


# setup(
#     name='Clasificador ABC',
#     version='1.0',
#     packages=find_packages(),
#     py_modules=['application_GUI.py'], 
# )
