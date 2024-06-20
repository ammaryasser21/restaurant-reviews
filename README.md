# Restaurant Reviews Sentiment Analysis

## Table of Contents

- [Introduction](#introduction)
- [Dataset Overview](#dataset-overview)
- [Project Objectives](#project-objectives)
- [Methodology](#methodology)
- [Data Exploration](#data-exploration)
- [Data Preprocessing](#data-preprocessing)
- [Feature Extraction](#feature-extraction)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Conclusion](#conclusion)

---

## Introduction
This project aims to analyze restaurant reviews to determine the sentiment (positive or negative) of each review. We use various natural language processing (NLP) techniques and machine learning algorithms to preprocess the data, extract features, and build a sentiment classification model.

## Dataset Overview
The dataset consists of restaurant reviews, with each review labeled as liked (`1`) or not liked (`0`). The dataset is loaded from a CSV file named `Restaurant_Reviews.csv`.

## Project Objectives
1. Preprocess the text data to clean and normalize it.
2. Extract features from the text using the Bag of Words method.
3. Train a RandomForestClassifier on the processed data.
4. Evaluate the performance of the trained model.

## Methodology
The project methodology includes the following steps:
1. Importing necessary libraries.
2. Loading and exploring the dataset.
3. Preprocessing the text data.
4. Extracting features using CountVectorizer.
5. Splitting the data into training and testing sets.
6. Training a RandomForestClassifier.
7. Evaluating the model's performance.

## Data Exploration
- Display the first 20 rows of the dataset.
- Get the shape and summary statistics of the dataset.
- Check for missing values and their percentage.

## Data Preprocessing
Text data is preprocessed through the following steps:
- Tokenization: Splitting text into individual words.
- Removing stop words: Eliminating common words that do not contribute to the sentiment.
- Lemmatization: Converting words to their base form.
- Removing punctuation.

## Feature Extraction
The Bag of Words method is used to convert the text data into numerical features. The text data is transformed into a matrix of token counts.

## Model Training
The data is split into training and testing sets, and a RandomForestClassifier is trained on the training data. The classifier is used to predict the sentiment of the reviews in the test set.

## Model Evaluation
The performance of the model is evaluated using accuracy, precision, recall, and F1 score. A classification report is generated to provide detailed metrics on the model's performance.

## Conclusion
The project successfully preprocesses the text data, extracts features using the Bag of Words method, trains a RandomForestClassifier, and evaluates the model's performance. The model provides valuable insights into the sentiment of restaurant reviews, which can be useful for business decisions and customer feedback analysis.
