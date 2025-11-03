# Find the percentage of data between 2 points on a standard distribution
x1 = float(input("Enter First X Value: "))
x2 = float(input("Enter Second X Value: "))
mu = float(input("Populations mean: "))
std = float(input("Standard deviation: "))

# Z score calculator lower score
def z_score_calculator_lower(x1,mu,std):
    z = (x1-mu)/std
