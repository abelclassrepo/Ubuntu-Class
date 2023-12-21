# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import string


def genfiles(numtimes=1, length=10, extension='txt'):
    for i in range(numtimes):
        filename = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
        print(filename + '.' + extension)


def createfiles():
    genfiles(15, 6, 'txt')
    genfiles(20, 11, 'jpg')
    genfiles(10, 15, 'sh')
    genfiles(8, 22, 'pdf')
    genfiles(30, 3, 'png')
    genfiles(10, 9, 'doc')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createfiles()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
