def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height*height)
    print("bmi = " + str(bmi))
    
    if bmi>25:
        print("User is overweight")
    elif bmi>18:
        print("User is normal weight")  
    else:
        print("User is underweight")
      

calculate_bmi(weight=57, height=1.73)

    