def copy_file(file_path, new_file_name):
    with open(file_path, "rb") as f:
        new_file_path = "./" + new_file_name
        with open(new_file_path, "wb") as nf:
            while True:
                data = f.read(1024)
                if not data:
                    break
                nf.write(data)
