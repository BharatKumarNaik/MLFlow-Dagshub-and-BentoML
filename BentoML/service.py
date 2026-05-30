import numpy as np
import bentoml


@bentoml.service
class IrisClassifierService:

    def __init__(self):
        # Load the latest saved sklearn model
        self.model = bentoml.sklearn.load_model("iris_clf:latest")

    # Creates a POST API endpoint: /classify
    @bentoml.api
    def classify(self, input_series: np.ndarray) -> np.ndarray:

        # Run prediction directly using the sklearn model
        result = self.model.predict(input_series)

        return result