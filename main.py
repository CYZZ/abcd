# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import pathlib
# import sys
# from shutil import copyfile
import locale
import os.path
import shutil
import sys

import myfunction_test
from firstpackage import *
from firstpackage.calculate import Person, Student
import plist_file_manager
from firstpackage import decoration
from firstpackage import my_zipfile


# import firstpackage


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    print("hhh")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    zip_path = "/Users/cyz/Desktop/PythonTest/mytest/ios_clcloo_803.zip"
    out_path = "/Users/cyz/Desktop/PythonTest/mytest/newAll"

    testzip = my_zipfile.MyZipFile
    testzip.normal_unzip(zip_path, out_path)
    # testzip.custom_unzip(zip_path, out_path)
    # testzip.custom_unzip2(zip_path, out_path)
    # testzip.noraml_unzip(zip_path, out_path)

    exit(0)

    print('当前编码是', sys.getdefaultencoding())
    print('当前的文件编码是', sys.getfilesystemencoding())
    print('local.getlocal = ', locale.getlocale())
    # locale.setlocale(locale.LC_ALL, 'en_CN')
    print('local.getdefaultLocal=', locale.getdefaultlocale())
    # locale.setlocale(locale.LC_ALL, "zh_CN.UTF-8")
    print(sys.stdout.encoding)

    print(sys.version)
    game_output_path = "/Users/cyz/Desktop/PythonTest"
    for parent, dir_names, file_names in os.walk(os.path.join(game_output_path, "Payload")):
        for dir_name in dir_names:
            if dir_name[-4:] == '.app':
                print('当前的app是', dir_name)

    game_path = "client ios.app"
    frame_works = "Frameworks"

    game_framework_path = os.path.join(game_path, frame_works)
    print("拼接后的路径=", game_framework_path)


    # print(sys.version_info)

    @decoration.check
    def comment():
        print("开始键盘侠模式")


    comment()

    # write_plist_for_icon()
    #
    my_info_plist = "/Users/cyz/Downloads/拨号盘/ttt/HuoSdkConfig.plist"
    read_resut = plist_file_manager.read_plist(my_info_plist)
    print(read_resut)
    print('type = %s', read_resut.__class__)

    # result_plist = write_url_types(target_file=my_info_plist, identifier="unback", scheme="ungame12388899")
    # # result_plist = write_url_types(target_file=my_info_plist, identifier="Alipay", scheme="hetaoHezi90")
    #
    # print("最终的plist=", result_plist)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
