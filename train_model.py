import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# load dataset
df = pd.read_csv("data/energy.csv")

# features and target
X = df[['temperature','humidity','wind_speed']]
y = df['consumption']

# split data
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# train model
model = RandomForestRegressor()
model.fit(X_train,y_train)

# save model
pickle.dump(model,open("models/model.pkl","wb"))

print("Model trained successfully!")