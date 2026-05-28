# MLflow Wine Quality Prediction Project

## Overview

This project demonstrates how to use **MLflow** for tracking Machine Learning experiments using a simple Wine Quality Prediction model.

The model is built using the **ElasticNet Regression** algorithm from Scikit-learn and trained on the famous Wine Quality dataset from the UCI Machine Learning Repository.

The main learning objective of this project is to understand:

* MLflow experiment tracking
* Logging parameters
* Logging metrics
* Logging models
* Model signatures
* MLflow runs
* Model registry basics
* Reproducibility in ML workflows

---

# Project Architecture

```text
Dataset --> Train/Test Split --> Model Training --> Evaluation
                                                |
                                                v
                                      MLflow Tracking
                                      - Parameters
                                      - Metrics
                                      - Model
                                      - Signature
```

---

# Dataset Information

Dataset Source:

Wine Quality Dataset
http://archive.ics.uci.edu/ml/datasets/Wine+Quality

Research Paper:

> P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
> Modeling wine preferences by data mining from physicochemical properties.
> Decision Support Systems, Elsevier, 47(4):547-553, 2009.

The dataset contains physicochemical properties of red wine such as:

* Fixed acidity
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Alcohol
* pH
* Sulphates

Target Column:

```text
quality
```

Wine quality score ranges from:

```text
3 to 9
```

---

# Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Pandas       | Data Handling        |
| NumPy        | Numerical Operations |
| Scikit-learn | Machine Learning     |
| MLflow       | Experiment Tracking  |
| ElasticNet   | Regression Algorithm |

---

# What is MLflow?

MLflow is an open-source platform used to manage the complete Machine Learning lifecycle.

It helps in:

* Experiment tracking
* Parameter logging
* Metric logging
* Model versioning
* Model packaging
* Model deployment
* Reproducibility

---

# MLflow Components

## 1. Tracking

Tracks:

* Parameters
* Metrics
* Artifacts
* Models

Example:

```python
mlflow.log_param("alpha", alpha)
mlflow.log_metric("rmse", rmse)
```

---

## 2. Projects

Standardized packaging format for ML code.

---

## 3. Models

Allows storing models in a reusable format.

Example:

```python
mlflow.sklearn.log_model(lr, "model")
```

---

## 4. Model Registry

Used to manage model versions and lifecycle.

Example:

```python
registered_model_name="ElasticnetWineModel"
```

---


# MLflow Run

```python
with mlflow.start_run():
```

Creates a new MLflow experiment run.

Everything inside this block gets tracked.

---

# Logging Parameters

```python
mlflow.log_param("alpha", alpha)
mlflow.log_param("l1_ratio", l1_ratio)
```

Logs hyperparameters used for training.

Useful for experiment comparison.

---

# Logging Metrics

```python
mlflow.log_metric("rmse", rmse)
mlflow.log_metric("mae", mae)
mlflow.log_metric("r2", r2)
```

Stores evaluation results.

Helps compare model performance.

---

# Infer Signature

```python
predictions = lr.predict(train_x)
signature = infer_signature(train_x, predictions)
```

## What does infer_signature do?

Automatically identifies:

* Input schema
* Output schema
* Data types
* Shape information

Example:

```text
Input:
fixed acidity -> float
alcohol -> float

Output:
Predicted quality -> float
```

Benefits:

* Input validation during inference
* Better deployment support
* Improved reproducibility
* Easier model serving

---

# Logging Model

```python
mlflow.sklearn.log_model(lr, "model")
```

Stores:

* Model weights
* Model structure
* Dependencies
* Metadata

inside MLflow artifacts.

---

# Model Registry

```python
registered_model_name="ElasticnetWineModel"
```

Registers the model into MLflow Model Registry.

Useful for:

* Versioning
* Staging
* Production deployment

---

# File Store vs Remote Store

```python
tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
```

Checks whether MLflow is using:

* Local file storage
* Remote tracking server

---

# DAGsHub / Remote Tracking

Example:

```python
remote_server_uri=""
mlflow.set_tracking_uri(remote_server_uri)
```

This can connect MLflow to:

* DAGsHub
* Remote MLflow Server
* Cloud Tracking Servers

Benefits:

* Centralized experiment tracking
* Team collaboration
* Shared model registry

---

# How to Run the Project
Default execution:

```bash
python app.py
```

Custom hyperparameters:

```bash
python app.py 0.2 0.4
```

Where:

```text
0.2 -> alpha
0.4 -> l1_ratio
```

---

# Viewing MLflow UI

Run:

```bash
mlflow ui
```

Open browser:

```text
http://127.0.0.1:5000
```

You can view:

* Experiments
* Runs
* Metrics
* Parameters
* Models
* Artifacts

---

# Important MLflow Concepts Learned

| Concept           | Purpose                      |
| ----------------- | ---------------------------- |
| start_run()       | Starts experiment tracking   |
| log_param()       | Logs hyperparameters         |
| log_metric()      | Logs evaluation metrics      |
| log_model()       | Saves model                  |
| infer_signature() | Captures input/output schema |
| Model Registry    | Version control for models   |

---

# Key Learnings From This Project

After completing this project, you will understand:

* Basic MLflow workflow
* Experiment tracking
* Hyperparameter logging
* Metric tracking
* Model packaging
* Model signatures
* Model registry basics
* Reproducible ML pipelines

---

# Future Improvements

Possible enhancements:

* Add classification models
* Add hyperparameter tuning
* Integrate DVC
* Use MLflow Projects
* Deploy using MLflow Serving
* Add Docker support
* Integrate with Azure ML
* Use DAGsHub remote tracking

---