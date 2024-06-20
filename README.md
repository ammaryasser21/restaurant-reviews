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
