try:
    f = open('some_file.txt', 'r')
    file_data = f.read()
    print(f'File content read, method 1:\n\n"\n{file_data}\n\"\n\n')
    f.close()
except Exception as error:
    print("Exception occurred: {}".format(error))


try:
    with open('some_file.txt', 'r') as f:
        file_data = f.read()
    print(f'File content read, method 2:\n\n"\n{file_data}\n\"\n')
    f.close()
except Exception as error:
    print("Exception occurred: {}".format(error))
