try:
    file1 = open('sample.txt', 'r')
    r = file1.read()
    print(r)
    file1.close()
except FileNotFoundError:
    print("file not found")
finally:
    print("continue")





