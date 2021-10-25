fh = open('fh_test.txt','a')
for i in range(2):
    name = input('Enter name here: ')
    fh.write(name + "\n")
fh.close()

fh = open('fh_test.txt', 'r')
for line in fh:
    print(line)
fh.close()