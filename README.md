.

🍽️ Firebase Recipe Analytics Pipeline
End-to-End ETL + Analytics Project Using Firebase & Python

This project demonstrates a complete data engineering workflow, built using Firebase Firestore, Python, and Pandas.
It includes ETL extraction, data cleaning, validation, transformation, and analytics, along with structured output datasets and meaningful visual insights.

📑 Table of Contents

Project Overview

Features

Project Structure

Data Model

4.1 Recipe Dataset

4.2 Ingredients Dataset

4.3 Steps Dataset

4.4 Users Dataset

4.5 Interactions Dataset

ETL Pipeline

5.1 Extract

5.2 Transform

5.3 Validate

5.4 Load

How to Run the Project

Analytics & Visualizations

7.1 Users Analytics

7.2 Recipe Analytics

7.3 User Interaction Analytics

7.4 Recipe Difficulty Distribution

7.5 Ingredient Frequency Analysis

Known Limitations

Future Enhancements

Conclusion

1️⃣ Project Overview

The Firebase Recipe Analytics Pipeline is a complete data engineering solution that:

Extracts recipe, user, and interaction data from Firebase Firestore

Cleans, transforms, and validates the data using Python

Normalizes Firestore’s nested JSON into clean CSV datasets

Generates powerful visual and statistical analytics

Follows a modular, production-grade folder structure

This project serves as a practical demonstration of ETL, NoSQL handling, and analytics in a real-world data engineering scenario.

2️⃣ Features

🔥 Seamless Firebase Firestore Integration

🧱 Normalized, analytics-friendly data modeling

🔄 Complete ETL Pipeline (Extract → Transform → Validate → Load)

✔️ Data quality and foreign key validation

📊 Analytics with charts and statistical summaries

📁 Clean, production-ready folder architecture

📝 Human-readable CSV exports

3️⃣ Project Structure
Recipeproject/
│── README.md
│── admin_key.json
│── firebase_config.py
│── etl_pipeline.py
│── validate_data.py
│── analytics.py
│── seed_recipes.py
│── seed_users.py
│── seed_interactions.py
│── recipe.csv
│── ingredients.csv
│── interactions.csv
│── steps.csv
│── screenshots/
└── __pycache__/

4️⃣ Data Model

Your pipeline converts Firestore into four fully normalized datasets.

4.1 recipe.csv
Column	Description
id	Unique recipe ID
title	Name of the recipe
prep_time	Time required to prepare
difficulty	easy / medium / hard
created_by	User ID who added the recipe
4.2 ingredients.csv
Column	Description
recipe_id	Foreign key → recipe.id
name	Name of the ingredient
4.3 steps.csv
Column	Description
recipe_id	Linked recipe
step_no	Step number
description	Instruction text
4.4 Users Dataset

Structure:

Field	Description
user_id	Unique user identifier
name	Full name
email	User email
created_at	Timestamp of user creation
4.5 interactions.csv
Column	Description
user_id	FK → user
recipe_id	FK → recipe
viewed	1 if viewed else 0
liked	1 if liked
cooked	1 if cook-attempted
5️⃣ ETL Pipeline
5.1 Extract

Connects to Firestore via Firebase Admin SDK

Reads collections: users, recipes, interactions

Converts Firestore documents into Python objects

5.2 Transform

Cleans and standardizes data:

Removes duplicate rows

Converts timestamps → date format

Normalizes difficulty levels

Converts values to numeric (0/1)

Splits nested recipe data into separate tables

Handles missing or empty arrays

5.3 Validate

Runs checks using validate_data.py:

Missing/null values

Broken foreign keys

Invalid difficulty types

Wrong data formats

Empty ingredient lists

Orphan interactions (user or recipe not found)

5.4 Load

Outputs four clean CSV files:

recipe.csv

ingredients.csv

steps.csv

interactions.csv

These datasets are now analytics-ready.

6️⃣ How to Run the Project
Step 1: Install Dependencies
pip install pandas matplotlib seaborn firebase-admin plotly


If needed:

pip install --user pandas matplotlib seaborn plotly

Step 2: Add Firebase Admin Key

Place your admin_key.json inside the project folder.

Step 3: Run ETL
python etl_pipeline.py

Step 4: Validate Data (optional)
python validate_data.py

Step 5: Run Analytics
python analytics.py


Charts will be saved inside the screenshots/ folder.

7️⃣ Analytics & Visualizations

The analytics pipeline produces the following insights:

7.1 Users Analytics

Shows user distribution and engagement.
Useful for understanding your active user base.

7.2 Recipe Analytics

Displays recipe count, difficulty types, preparation times, and other metadata patterns.

7.3 Interaction Analytics

Visualizes:

Total views per recipe

Total likes per recipe

Total cooked attempts

Helps identify high-performing or trending recipes.

7.4 Difficulty Distribution

Pie chart representing:

Easy

Medium

Hard recipes

Gives an overview of content complexity.

7.5 Ingredient Frequency

Bar chart showing the most commonly used ingredients.
Identifies cooking patterns and common recipe components.

8️⃣ Known Limitations

Firestore is not optimized for relational queries

Batch ETL (not real-time streaming yet)

CSV export cannot store nested JSON perfectly

Limited interaction types (no ratings/comments yet)

9️⃣ Future Enhancements

Convert ETL into an Apache Airflow DAG

Migrate cleaned data to BigQuery

Build a Power BI / Tableau Dashboard

Add more interaction types:

Ratings

Comments

User segmentation

Add Firebase Cloud Functions for real-time streaming

Dockerize the entire project

🔟 Conclusion

This project delivers a powerful and complete ETL + analytics workflow using Firebase and Python.
It transforms raw, unstructured Firestore data into clean, validated datasets and generates insightful visualizations.

The pipeline is modular, scalable, and ready for real-world data engineering applications.
