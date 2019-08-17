"""
    copy_file.py    拷贝文件
"""
def copy_file(file_path, new_file_name):
    """
        file_path : 拷贝文件路径
        new_file_name : 保存文件名称
    """
    with open(file_path, "rb") as f:
        new_file_path = "./" + new_file_name
        with open(new_file_path, "wb") as nf:
            while True:
                data = f.read(1024)
                if not data:
                    break
                nf.write(data)
