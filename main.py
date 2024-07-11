import random

age = int(random.randint(0, 100))
print (f" You age is {age}")

if age <= 30:
    print (f"you are young keep going!!!")

elif age > 30 and age < 60:
    print (f"you are old keep going!!!")

else:
    print (f"you need to rest and then advice the young people on the path to success)!!")