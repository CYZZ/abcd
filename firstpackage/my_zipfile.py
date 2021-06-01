import zipfile
import shutil
import asynchat

import pathlib


class MyZipFile:
    def __init__(self):
        pass

    @staticmethod
    def normal_unzip(path: str, new_path: str):
        unzip_file = zipfile.ZipFile(path, 'r')
        unzip_file.extractall(new_path)
        unzip_file.close()

    @staticmethod
    def custom_unzip(self, path: str, new_path: str):
        with zipfile.ZipFile(path, 'r') as zf:
            print(zf.namelist())
            for fn in zf.namelist():
                right_fn = new_path + '/' + fn.encode('cp437').decode('utf8')

                with open(right_fn, 'wb') as output_file:
                    with zf.open(fn, 'r') as origin_file:
                        shutil.copyfileobj(origin_file, output_file)

    @staticmethod
    def custom_unzip2(self, path: str, new_path: str):
        with zipfile.ZipFile(path, 'r') as f:
            for fn in f.namelist():
                # utf8_fn = fn.encode('cp437').decode('utf8')
                extracted_path = pathlib.Path(f.extract(fn, new_path))
                # print(extracted_path)
                extracted_path.rename(new_path + '//' + fn.encode('cp437').decode('utf-8'))
                # print(extracted_path)
