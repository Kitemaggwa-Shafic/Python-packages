english   = int(input("Enter English Marks : "))
maths     = int(input("Enter  Maths Marks : "))
sst     = int(input("Enter  SST Marks : "))
science     = int(input("Enter  Science Marks : "))

totalMarks = (english+maths+sst+science)
average = totalMarks/4
print("Average scored :    ", average,"%")
if average >= 91 or average <= 100:
    print("Your Grade is D1")
elif average >= 81 or average < 91:
    print("Your Grade is D2")
elif average >= 71 or average < 81:
    print("Your Grade is C3")
elif average >= 61 and average < 71:
    print("Your Grade is C4")
elif average >= 51 and average < 61:
    print("Your Grade is C5")
elif average >= 41 and average < 51:
    print("Your Grade is C6")
elif average >= 33 and average < 41:
    print("Your Grade is P7")
elif average >= 25 and average < 33:
    print("Your Grade is P8")
else:
    print("F9 and Fail")