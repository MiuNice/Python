import os


def file_split(path, split_num, new_path = "./fileSplit"):
    path_name = path.split("/")[-1].split(".")[0]
    new_path = new_path + "-" + path_name
    file_size = os.path.getsize(path)
    every_read_b = file_size // split_num
    test_name = 1
    if os.path.exists(new_path) is False:
        os.makedirs(new_path)
    with open(path, "rb") as f:
        
        while True:
            b = f.read(every_read_b)
            if not b:
                break
            with open(new_path + "/" + path_name + "-" + str(test_name) + ".zip", "wb") as f1:
                f1.write(b)
            test_name += 1

def file_join(path):
    new_list = []
    f = os.walk(path)
    print(f)
    for i in f:
        file_geshi = i[-1][0].split(".")[-1]
        file_name = i[-1][0].split(".")[0].split("-")[0]
        for j in i[-1]:
            new_list.append(int(j.split(".")[0].split("-")[-1]))
    new_list.sort()
    max_file_num = new_list[len(new_list) - 1]
    print(max_file_num)
    for i in range(max_file_num):
        with open(path + "/" + file_name + "-" + str(i + 1) + "." + file_geshi, "rb") as rb_f:
            with open("./" + file_name + "_wmiu." + file_geshi, "ab") as ab_f:
                ab_f.write(rb_f.read())

    


if __name__ == "__main__":
    # file_split("./1.zip", 10)
    file_join("./fileSplit-1")
