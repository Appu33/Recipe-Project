Recipeproject

🍽️ Firebase Recipe Analytics Pipeline

A Complete ETL + Analytics Project Using Firebase Firestore & Python

📌 Project Overview

This project implements a complete data engineering pipeline that:

Extracts recipe, user, and interaction data from Firebase Firestore

Transforms, validates, and normalizes the data using Python

Loads clean structured data into CSV datasets

Generates visual and statistical analytics insights

This project demonstrates:

🔥 Firebase Database Integration

🧱 Proper Data Modeling

🔄 ETL Pipeline (Extract → Transform → Load)

✔ Data Quality Validation

📊 Analytics & Charts

📁 Production-ready folder structure

📝 Industry-grade documentation

📂 Project Structure
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

🧱 Data Model

Your pipeline produces four normalized datasets.

📘 recipe.csv
Column	Description
id	Recipe ID
title	Recipe name
prep_time	Preparation time (min)
difficulty	easy / medium / hard
created_by	User ID (FK → users)
🥗 ingredients.csv
Column	Description
recipe_id	FK → recipe.id
name	Ingredient name
📄 steps.csv
Column	Description
recipe_id	FK → recipe.id
step_no	Step number
description	Step instructions
⭐ interactions.csv
Column	Description
user_id	FK → users
recipe_id	FK → recipe
viewed	1 = viewed
liked	1 = liked
cooked	1 = attempted cook
🔄 ETL Pipeline (etl_pipeline.py)
1️⃣ Extract

Connects to Firestore using firebase_config.py

Fetches collections:

recipes

users

interactions

Saves raw data to CSV

2️⃣ Transform

Cleans and standardizes:

Removes duplicates

Converts timestamps to date

Standardizes difficulty labels

Converts viewed/liked/cooked → 0/1

Removes blank or malformed rows

3️⃣ Validate (validate_data.py)

Quality checks performed:

Missing or null values

Broken foreign keys

Invalid difficulty fields

Incorrect datatypes

Empty ingredient/step lists

4️⃣ Load

Outputs final normalized CSV files:

recipe.csv

ingredients.csv

steps.csv

interactions.csv

📊 Analytics (analytics.py)

Run:

python analytics.py


Generates insights such as:

✔ Most common ingredients

✔ Average preparation time

✔ Recipe difficulty distribution

✔ Top viewed recipes

✔ Top liked recipes

✔ Correlation: prep_time vs likes

✔ User engagement metrics

Visual charts are automatically saved inside:

screenshots/

📈 Example Insights
Insight	Example Output
Average prep time	22 minutes
Most common ingredient	Salt
Most liked recipe	r001
Most viewed recipe	r001
Strongest correlation	prep_time vs likes

🧪 How to Run This Project
1️⃣ Install dependencies
pip install pandas matplotlib firebase-admin seaborn plotly


If permission issues occur:

pip install --user pandas matplotlib seaborn plotly

2️⃣ Add Firebase Admin Key

Place admin_key.json inside the project folder.

3️⃣ Run ETL
python etl_pipeline.py

4️⃣ Run Data Validation (optional)
python validate_data.py

5️⃣ Run Analytics
python analytics.py

⚠️ Known Limitations

Firestore is not optimized for heavy relational workloads

ETL runs in batch mode, not real-time

CSV export cannot store nested JSON perfectly

Analytics limited to available interaction types (no ratings/comments)

🚀 Future Enhancements

Convert this pipeline into an Apache Airflow DAG

Store cleaned data in BigQuery instead of CSV

Build a full Power BI / Tableau dashboard

Add:

recipe ratings

comments

user segmentation

Add real-time streaming using Firebase triggers

Dockerize the entire pipeline

🔚 Conclusion

This project delivers a complete end-to-end ETL and analytics pipeline built on Firebase and Python. It converts raw Firestore data into clean, validated CSV datasets and generates meaningful insights with visual charts. The structure is modular, easy to extend, and serves as a strong foundation for real-world data engineering workflows.
