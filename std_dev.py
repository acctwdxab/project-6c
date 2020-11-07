# Dan Wu
# 11/6/2020
# Write a function to calculate the standard deviation

class Person:
    """
       Represents two data members - the person's name and age
       """
    def __init__(self,name,age):
     """takes two values and uses them to initialize the data members."""
     self.name = name
     self.age = age

def std_dev(persons):
    """calculate the standard deviation"""
    ages = []
    for p in persons:
        ages.append(p.age)

    total = sum(ages)
    mean = total / len(ages)

    total = 0
    for a in ages:
        total += (a-mean)**2;
    total /=len(ages)

    dev = total**.5
    return dev

if  __name__=="__main__":
    p1 = Person( "Kyoungmin" ,73)
    p2 = Person ( "Mercedes" , 24 )
    p3 = Person ( "Beatrice" , 48 )
    person_list = [p1 , p2 , p3]
    answer = std_dev ( person_list )




