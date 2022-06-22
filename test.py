def fourOne(c):
    if c >= 4 and c <= 15:
        print("finish setting")


def practice_2(g):
    # Requriements
    # The input Value f(g) return from 4.35 to 8.2 as normal vaules.
    # The input value out of the range above is recognized as abnormal values

    # Question1
    # What would you ask an enginner who has written the above the requirement.
    # My answer
    # Check if the significant value is 8.20
    # Check if 4.35 and 8.20 are included in the normal values
    # Question2
    # List up seven kinds of values when you test the above requirements
    # in the following two ways.
    # Method1
    # Solve 4 kinds of test values to execute Equivalence partition and boarder analysis.
    # Considering hidden boarder values, solve 3 kinds of test value,
    # where the history of document does not exist and you can not ask the engineer about the history.
    # My answer2
    # I have no idea, bitch.( The answer was 5.0, 6.0 and 7.0! Who the fuck can guess the answer!!!!!)

    if g >= 4.35 and g <= 8.20:
        print("Normal Value")


def practice_3(age):
    print("Let's start pracetice3!")
    print("The entrance fee of WaiWai Aquarium is shown in the following table.")
    print("Find boarder values after dividing it into Equivalence partition")
    # Table:: The entrance fee of WaiWAi Aquarium.
    # Adult(grater than or equal to 16 years old):2000 yen
    # Junior(grater than or equal to 7years old): 900 yen
    # Child(grater than or equal to 4years old): 400yen
    # Infant(less than 4 years old): 0yen
    if age >= 16:
        print("print")
    elif age >= 7 and age < 16:
        print("900")
    elif age >= 4 and age < 7:
        print("400")
    elif age < 4:
        print("0")


age = input()
practice_3(int(age))
