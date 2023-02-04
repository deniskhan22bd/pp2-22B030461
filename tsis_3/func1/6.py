def str_return(string: str):
    string_list = string.split()
    for i in range(len(string_list) - 1, -1, -1):
        print(string_list[i], end=" ")

str_return("We are ready")

