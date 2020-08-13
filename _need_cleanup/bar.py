
#import foo
#print ("Im a __name__ from bar program which is", __name__)
#print(foo.__name__)

def swappy():
    print("here I am")

def anshuma():
    print('there you are')

def abc():
    print ("Im a __name__ from bar program which is", __name__)

def sort_me(list):
    pass
    return []


if __name__ == "__main__":
    #swappy()
    #anshuma()
    #abc()
    a = [4,6,3,3,5]
    output = sort_me(a)

    expected = [3,3,4,5,6]
    if output == expected:
        print(True)
    else:
        print(False)
