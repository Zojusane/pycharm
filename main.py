# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    a = ['a', 'b', 'c', 'd']
    b = a[0:2]
    b[0] = 'q'
    print(b)
    print(a)
    dict2 = {'runoob': 'runoob.com', 'google': 'google.com'}
    print(repr(dict2))
    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
    print(tinydict.keys())
    print(tinydict.values())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
