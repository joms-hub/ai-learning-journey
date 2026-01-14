# K-Nearest Neighbors (KNN) Implementation from Scratch

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview
This project is a custom implementation of the **K-Nearest Neighbors (KNN)** algorithm built entirely in pure Python.

**The Goal:** To classify the [Iris Flower Dataset](https://archive.ics.uci.edu/ml/datasets/iris) without using "black box" machine learning libraries like `scikit-learn`. This project demonstrates a foundational understanding of:
* Vector mathematics and Euclidean distance.
* Algorithm efficiency and complexity.
* Object-Oriented Programming (OOP) in Python.

## 🧮 The Math Behind the Code
Instead of importing a pre-made classifier, I implemented the distance logic manually. The core of this algorithm relies on the **Euclidean Distance** formula to find the similarity between data points:

$$d(p, q) = \sqrt{\sum_{i=1}^n (q_i - p_i)^2}$$

Where:
* $p$ and $q$ are two data points (rows in the dataset).
* $n$ is the number of features (dimensions).

The algorithm proceeds in three steps:
1.  **Calculate Distances:** Measure the distance between the query point and every other point in the training set.
2.  **Get Neighbors:** Sort the distances and pick the top $k$ closest neighbors.
3.  **Vote:** The neighbors vote on the class label (majority rule).

## 📂 Project Structure
```text
├── data/
│   └── iris.csv          # The raw dataset
├── src/
│   ├── knn.py            # The class containing the KNN algorithm logic
│   └── utils.py          # Helper functions for loading data and calculating accuracy
├── main.py               # The entry point to run the classification
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (minimal, mostly for data handling)
