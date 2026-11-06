# Basic experience calculator program
try:
    input_IT_experience = input("Enter your years of experience in IT: ")
    converted_IT_experience = float(input_IT_experience)
    if converted_IT_experience < 0:
        print("Experience cannot be negative. Please enter a valid number.")
    else:
        is_there_experience_outside_IT = input("Do you have experience outside of IT? : ")
        converted_experience_outside_IT = float(is_there_experience_outside_IT)

        if converted_experience_outside_IT < 0:
            print("Experience cannot be negative. Please enter a valid number.")
        else: 
            display_total_experience = converted_IT_experience + converted_experience_outside_IT
            print(f"Total experience: {display_total_experience} years")

except ValueError:
    print("Invalid input. Please enter a valid number for years of experience.")
