
try:
    files = []
    for i in range(1000000):
        files.append(open('some_file.txt', 'r'))
        print(i)
except Exception as error:
    print("Exception occurred: {}".format(error))