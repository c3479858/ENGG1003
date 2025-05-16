import pandas as pd

my_data = pd.read_csv("tiny.csv")
my_first_name = my_data["First name"][2]
print(my_data.describe())