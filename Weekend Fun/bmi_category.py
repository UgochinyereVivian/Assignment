

weight = float(input('Hey Odili🤽️,enter your weight: '))
height = float(input('Hey Odili🤪️,enter your height: '))
compute_bmi = weight / height * height

if compute_bmi < 18.5:
    print(compute_bmi, '= underweight')

elif compute_bmi >= 18.5 and compute_bmi <= 24.9:
    print(compute_bmi, '= Normal')

elif compute_bmi >= 25 and compute_bmi <= 29.9:
    print(compute_bmi, '= Overweight')

elif compute_bmi >= 30:
    print(compute_bmi, '= Obese')
