#create a z score calculator
data_point = float(input("Individual value: "))
mu = float(input("Population mean: "))
std = float(input("Standard deviation: "))

def z_Score(data_point, mu, std):
    z = (data_point - mu) / std
    return z

results = z_Score(data_point,mu,std)
print(f"Z Score: {results}")