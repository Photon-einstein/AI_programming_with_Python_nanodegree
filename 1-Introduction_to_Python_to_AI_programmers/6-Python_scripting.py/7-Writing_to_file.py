try:
    f = open('my_file_write.txt', 'w')
    f.write("Hello there!")
    f.close()
except Exception as error:
    print("Exception occurred: {}".format(error))