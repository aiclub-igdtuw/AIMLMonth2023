from sklearn.linear_model import LinearRegression

X = [[1], [2], [3]]
y = [2, 4, 6]

model = LinearRegression()
model.fit(X, y)

print("Model trained")
print("Prediction:", model.predict([[4]]))
