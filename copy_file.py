"""
    copy_file.py    拷贝文件
"""
def copy_file(file_path, new_file_name=None, new_file_path="./"):
    """
        拷贝文件
    :param file_path: 要拷贝文件的路径
    :param new_file_name: 保存文件的名称
    :param new_file_path: 保存文件的路径
    :return: 
    """
    with open(file_path, "rb") as f:
        if not new_file_name:
            new_file_name = file_path.split("/")[-1]
        if new_file_path.split("/")[-1] == new_file_name:
            new_file_path = new_file_path
        else:
            new_file_path += new_file_name
        print(new_file_path)
        with open(new_file_path, "wb") as nf:
            while True:
                data = f.read(1024)
                if not data:
                    break
                nf.write(data)
