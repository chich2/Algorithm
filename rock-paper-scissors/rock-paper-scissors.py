def main():
    rst = input_rpc()
    print(rpc(rst))


def input_rpc():
    tmp = input()
    list_tmp = tmp.split(" ")
    return list_tmp


def rpc(list_input):
    tmp = int(list_input[0])-int(list_input[1])
    if tmp==1 or tmp==-2:
        return "A"
    else:
        return "B"

if __name__ == '__main__':
    main()