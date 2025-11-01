# Create a Calculator that tells you what percentile the data falls under
z = float(input("Enter Z score: "))
mu = float(input("The populations mean: "))
sigma = float(input("Populations Standard Deviation: "))

#Calculation for the percentile
def percentile(mu,z,sigma):
    x = (sigma * z) +mu
    return x

#Print
results = percentile(mu,z,sigma)
print(f"The data point falls with the {results} percentile")