import pandas as pd

data = {
    "Name": ["Mikko", "Joona", "Jesse","Pete"],
    "Age": [28, 30,22,23],
    "City": ["Mikkeli", "Kotka","Lahti", "Helsinki"]
}

df = pd.DataFrame(data)

print ("Full dataframe: ")
print(df)