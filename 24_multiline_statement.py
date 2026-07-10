maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))
computer = int(input("Enter Computer marks: "))
gujarati = int(input("Enter Gujarati marks: "))
hindi = int(input("Enter Hindi marks: "))
social_science = int(input("Enter Social Science marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
biology = int(input("Enter Biology marks: "))

total = maths + science + english + computer + \
    gujarati + hindi + social_science + \
        physics + chemistry + biology
average = total / 10
print("total ",total)
print("average ",average)