"""
    copy_file.py    拷贝文件
"""

import os


class MyFileNotFoundError(Exception):
    def __init__(self, file_path):
        super().__init__(self)
        self._file_path = file_path

    def __str__(self):
        return "找不到该路径: " + self._file_path


def copy_file(file_path, new_file_name=None, new_file_path="./"):
    """
        拷贝文件
    :param file_path: 要拷贝文件的路径
    :param new_file_name: 保存文件的名称
    :param new_file_path: 保存文件的路径
    :return:
    """
    try:
        with open(file_path, "rb") as f:
            if not new_file_name:
                new_file_name = file_path.split("/")[-1]
            if new_file_path.split("/")[-1] == new_file_name:
                new_file_path = new_file_path
            else:
                if new_file_path[-1] != "/":
                    new_file_path = new_file_path + "/" + new_file_name
                else:
                    new_file_path += new_file_name
            print("拷贝地址:", new_file_path)
            with open(new_file_path, "wb") as nf:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    nf.write(data)
    except FileNotFoundError as notfile:
        error = "".join(list(str(notfile))[38:-1])
        raise MyFileNotFoundError(error)


if __name__ == "__main__":
    this_file_path = os.path.abspath(__file__)
    copy_file(this_file_path, "NewFile.txt")
