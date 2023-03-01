def myList():
    names = ["Edgar", "Mark", "Pato", "Audrie"]
    for name in names:
        print(name)
myList()

# demostrating an If and elif statements, with in a function
def person():
    isMale = True
    isTall = False

    if isMale and isTall:
        print("Yes, he is a tall male guy")
    elif isMale and not(isTall):
        print("Yes, he is a male short guy")
    elif isTall and not(isMale):
        print("Yes, not male but tall guy")
    else:
        print("Yes, Not male neither tall")        
person()

