def calculate_bmi(weight,height):
    bmi=weight/height**2
    print("BMI result :",bmi)
    if(bmi<18.5):
        print("Underweight")
    elif(18.5<=bmi<25):
        print("Normal")

    elif(25<=bmi<30):
        print("Overweight")
    elif(bmi>=30):
        print("Obese")
    else:
        print("Invalid Input")
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))
if (weight>0 and height>0):
    calculate_bmi(weight,height)
else:
    print("INVALID INPUT")