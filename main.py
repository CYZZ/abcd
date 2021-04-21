# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import pathlib
# import sys
# from shutil import copyfile
# import shutil
import plistlib
import os


def read_plist(file_path: str):
    if os.path.exists(file_path):
        print("plist文件存在")
        with open(file_path, "rb") as fp_bytes:
            pl = plistlib.load(fp_bytes)
            # pl: dict = pl
            print("dic=", pl)
            return pl
    else:
        print("plist文件不存在")
        return {}


def write_plist(target_file: str, value: dict, is_cover=True):
    """
    写入plist文件，当前只支持在dict格式的plist文件添加keyValue
    :param target_file: 目标文件路径
    :param value: 写入的keyValue值
    :param is_cover: 是否覆盖原来的
    :return: 写入之后的字典
    """
    if os.path.exists(target_file):
        print("plist文件存在")
        pl: dict = read_plist(target_file)
        if is_cover:
            # 如果允许覆盖直接更新原来的key
            pl.update(value)
        with open(target_file, "wb") as fpw:
            plistlib.dump(value=pl, fp=fpw)
            return pl
    else:
        print("文件不存在", target_file)


def write_plist_for_icon(target_file: str):
    """
    设置info.plist文件的icon配置
    :return: 无
    """
    icon_dict = {
        "CFBundleIcons": {"CFBundlePrimaryIcon": {"CFBundleIconFiles": ["AppIcon20x20", "AppIcon29x29", "AppIcon60x60"],
                                                  "CFBundleIconName": "AppIcon"}
                          },
        'CFBundleIcons~ipad': {'CFBundlePrimaryIcon': {
            'CFBundleIconFiles': ['AppIcon20x20', 'AppIcon29x29', 'AppIcon40x40', 'AppIcon60x60', 'AppIcon76x76',
                                  'AppIcon83.5x83.5'], 'CFBundleIconName': 'AppIcon'}}
    }
    write_plist(target_file=target_file, value=icon_dict)


def write_url_types(target_file: str, identifier: str, scheme: str) -> dict:
    """
    写入URlType,支付宝回调相关
    :return:返回写入后生成的字典
    """
    plist_dic: dict = read_plist(file_path=target_file)
    url_types = plist_dic.get("CFBundleURLTypes")
    if url_types is not None:
        print("不为空的urlTypes")
        if isinstance(url_types, list):
            url_types: list = url_types
            for i in range(0, len(url_types)):
                item = url_types[i]
                if isinstance(item, dict):
                    if identifier == item["CFBundleURLName"]:
                        print("存在相同的")
                        item["CFBundleURLSchemes"] = [scheme]
                        url_types[i] = item
                        plist_dic["CFBundleURLTypes"] = url_types
                        with open(target_file, "wb") as fpw:
                            plistlib.dump(value=plist_dic, fp=fpw)
                        return plist_dic
                    # else:
                    # print("不是：", identifier)
                    print(item)
            print("循环结束了")
            # 循环结束都没有存在相同的key就添加一个
            new_item = {"CFBundleURLName": identifier, "CFBundleURLSchemes": [scheme]}
            url_types.insert(0, new_item)
            plist_dic["CFBundleURLTypes"] = url_types
            with open(target_file, "wb") as fpw:
                plistlib.dump(value=plist_dic, fp=fpw)
            return plist_dic
            # print("当前读取的是数组")
        else:
            print("当前的URLTypes不是数组")
            new_item = {"CFBundleURLName": identifier, "CFBundleURLSchemes": [scheme]}
            url_types = [new_item]
            plist_dic["CFBundleURLTypes"] = url_types
            with open(target_file, "wb") as fpw:
                plistlib.dump(value=plist_dic, fp=fpw)
            return plist_dic
    else:
        print("当前的URLTypes为空")
        new_item = {"CFBundleURLName": identifier, "CFBundleURLSchemes": [scheme]}
        url_types = [new_item]
        plist_dic["CFBundleURLTypes"] = url_types
        with open(target_file, "wb") as fpw:
            plistlib.dump(value=plist_dic, fp=fpw)
        return plist_dic
    # 读取结束了


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    print("hhh")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    write_plist_for_icon()

    my_info_plist = "/Users/cyz/Downloads/拨号盘/ttt/GameInfo.plist"
    result_plist = write_url_types(target_file=my_info_plist, identifier="unback", scheme="ungame12388899")
    # result_plist = write_url_types(target_file=my_info_plist, identifier="Alipay", scheme="hetaoHezi90")

    print("最终的plist=", result_plist)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
