import bentoml

model = bentoml.sklearn.load_model("iris_clf:latest")

result = model.predict([[5.9, 3.0, 5.1, 1.8]])

print(result)