import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

data = pd.read_csv("train.csv")
print(data.head())
print(data.shape)

#Working with null values
missing_values = data.isnull().sum().sort_values(ascending=False)
missing_values.plot(kind="barh")
data.drop("Cabin", axis=1, inplace=True)
data["Age"].fillna(data["Age"].mean(), inplace=True)
data["Age"] = data["Age"].astype("int")
data["Embarked"].fillna(method="bfill", inplace=True)
print(data.isnull().sum())
data.drop(["Name", "Ticket", "Fare", "PassengerId"], axis=1, inplace=True)

#Encoding
encoder = LabelEncoder()
data["Embarked"] = encoder.fit_transform(data["Embarked"])
data["Sex"] = encoder.fit_transform(data["Sex"])
x = data[:]

#Scaling
for col in x:
    scale = MinMaxScaler()
    x[col] = scale.fit_transform(x[[col]])

#Convert to CSV
x.to_csv("Titanic_Dataset.csv", index=False)
