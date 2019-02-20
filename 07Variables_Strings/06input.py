print("How many KM did you cycle today?")
# by default input return string input
kms = float(input())
miles = kms/1.61
# precisions
miles = round(miles, 3)
print(f"Your {kms} KM is {miles} Miles")