#take input for the student that he can attend the exam or not
medical_cause = input("did you have medical cause y or n:")
#take the input of the attendance
atten= int(input("enter the attendance of the student:"))
#checking the user input predicting output accordingly
if medical_cause=="Y":#checking the condition1
    print("you are allowed")
else:
    if atten >= 75:#checking the condition2
        print("allowed")
    else:
     print("not allowed")