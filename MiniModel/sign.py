"""
    sign.py 符号保留
"""

def sign(x):
    num_sign = []
    for i in x:
        if i < 0:
            num_sign.append(-1)
        elif i > 0:
            num_sign.append(1)
        else:
            num_sign.append(0)
    return num_sign

if __name__ == "__main__":
    x = [9,16,-28,0,1,-2]
    print(sign(x))
