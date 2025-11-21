.

🍽️ Firebase Recipe Analytics Pipeline

A Complete End-to-End ETL + Analytics Project Using Firebase Firestore & Python

<p align="center"> <a href="https://github.com/yourusername/RecipeProject/stargazers"> <img src="https://img.shields.io/github/stars/yourusername/RecipeProject?style=for-the-badge" alt="GitHub stars"/> </a> <a href="https://github.com/yourusername/RecipeProject/issues"> <img src="https://img.shields.io/github/issues/yourusername/RecipeProject?style=for-the-badge" alt="GitHub issues"/> </a> <a href="https://www.python.org/"> <img src="https://img.shields.io/badge/python-3.12-blue?style=for-the-badge" alt="Python Version"/> </a> <a href="https://pypi.org/project/pandas/"> <img src="https://img.shields.io/badge/pandas-2.3.3-lightgrey?style=for-the-badge" alt="Pandas"/> </a> <a href="https://pypi.org/project/matplotlib/"> <img src="https://img.shields.io/badge/matplotlib-3.10.7-orange?style=for-the-badge" alt="Matplotlib"/> </a> <a href="https://pypi.org/project/seaborn/"> <img src="https://img.shields.io/badge/seaborn-0.13.2-purple?style=for-the-badge" alt="Seaborn"/> </a> </p>
📌 Project Overview

This project implements a full data engineering pipeline:

Extract recipe, user, and interaction data from Firebase Firestore

Transform, validate, and normalize data using Python

Load clean structured data into CSV datasets

Generate statistical and visual analytics insights

Features:

🔥 Firebase Database Integration

🧱 Data Modeling

🔄 ETL Pipeline (Extract → Transform → Load)

✔ Data Quality Validation

📊 Analytics & Charts

📁 Project Structure
Recipeproject/
├── README.md
├── admin_key.json
├── firebase_config.py
├── etl_pipeline.py
├── validate_data.py
├── analytics.py
├── seed_recipes.py
├── seed_users.py
├── seed_interactions.py
├── recipe.csv
├── ingredients.csv
├── steps.csv
├── interactions.csv
├── screenshots/       # Add your analytics screenshots here
└── __pycache__/

🧱 Data Model
Recipe (recipe.csv)
Column	Description
id	Recipe ID
title	Recipe Name
prep_time	Preparation time (minutes)
difficulty	easy / medium / hard
created_by	User ID (FK → users)
Ingredients (ingredients.csv)
Column	Description
recipe_id	FK → recipe.id
name	Ingredient Name
Steps (steps.csv)
Column	Description
recipe_id	FK → recipe.id
step_no	Step Number
description	Step Instructions
Interactions (interactions.csv)
Column	Description
user_id	FK → users
recipe_id	FK → recipe
viewed	1 = viewed, 0 = not viewed
liked	1 = liked, 0 = not liked
cooked	1 = attempted cook, 0 = not attempted
🔄 ETL Pipeline

etl_pipeline.py Steps:

Extract: Fetch collections from Firestore → Save raw CSVs

Transform: Remove duplicates, standardize difficulty labels, convert interactions → 0/1, clean empty/malformed rows

Validate (validate_data.py): Check for nulls, broken foreign keys, invalid difficulty, wrong datatypes, empty ingredients/steps

Load: Save final normalized CSVs: recipe.csv, ingredients.csv, steps.csv, interactions.csv

📊 Analytics (analytics.py)

Generates:

Most common ingredients

Average preparation time

Difficulty distribution

Top viewed recipes

Top liked recipes

Prep_time vs likes correlation

User engagement metrics

Visual charts are saved in screenshots/.

Example Insights:

Insight	Example Output
Average prep time	22 minutes
Most common ingredient	Salt
Most liked recipe	r001
Most viewed recipe	r001
Strongest correlation	prep_time vs likes
🧪 How to Run
# Install dependencies
pip install pandas matplotlib seaborn plotly firebase-admin

# Run ETL Pipeline
python etl_pipeline.py

# Run Validation (optional)
python validate_data.py

# Run Analytics
python analytics.py


Charts will appear in screenshots/.

⚠️ Known Limitations

Firestore not optimized for heavy relational workloads

ETL is batch-based, not real-time

CSV cannot store nested JSON perfectly

Analytics limited to available interactions (no ratings/comments)

🚀 Future Enhancements

Convert to Apache Airflow DAG

Store cleaned data in BigQuery

Build Power BI / Tableau dashboards

Add ratings, comments, and user segmentation

Enable real-time streaming via Firebase triggers

Dockerize pipeline

🔚 Conclusion

This project delivers a complete end-to-end ETL and analytics workflow using Firebase and Python.
Raw Firestore data is converted into clean CSV datasets with insights and visualizations.
Modular structure ensures scalability and provides a strong foundation for real-world data engineering projects.
