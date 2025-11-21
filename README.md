.

🍽️ Firebase Recipe Analytics Pipeline
End-to-End ETL + Analytics Project Using Firebase & Python

A complete data engineering workflow built using Firebase Firestore, Python, and Pandas.
This project demonstrates ETL extraction, data cleaning, validation, transformation, analytics, and visual chart generation.

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

7.1 Users Chart

7.2 Recipes Chart

7.3 Interactions Chart

7.4 Difficulty Pie Chart

7.5 Ingredients Bar Chart

Screenshots

Known Limitations

Future Enhancements

Conclusion

1️⃣ Project Overview

This project implements a complete ETL + Analytics Pipeline using Firebase as the source system.
It processes recipe data, user data, and interaction data, then performs cleaning, validation, normalization, and analytics.

2️⃣ Features

🔥 Integration with Firebase Firestore

🧱 Clean & normalized data modeling

🔄 Full ETL (Extract → Transform → Validate → Load)

✔ Data quality checks

📊 Interactive analytics & charts

📁 Production-ready folder structure

📄 Easy-to-read CSV outputs

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
│     ├── users.png
│     ├── recipe.png
│     ├── interactions.png
│     ├── piechart.png
│     ├── barchart.png
└── pycache/

4️⃣ Data Model

Your final output consists of four normalized datasets, ideal for analytics.

4.1 recipe.csv
Column	Description
id	Recipe ID
title	Recipe name
prep_time	Preparation time (minutes)
difficulty	easy / medium / hard
created_by	User ID (FK → users)
4.2 ingredients.csv
Column	Description
recipe_id	FK → recipe.id
name	Ingredient name
4.3 steps.csv
Column	Description
recipe_id	FK → recipe.id
step_no	Step number
description	Step instructions
4.4 users.csv (Optional)
Column	Description
id	User ID
name	User name
email	User email
4.5 interactions.csv
Column	Description
user_id	FK → users
recipe_id	FK → recipe
viewed	1 = viewed
liked	1 = liked
cooked	1 = attempted cook
5️⃣ ETL Pipeline
5.1 Extract

Connects to Firestore using firebase_config.py

Reads collections: recipes, users, interactions

Saves raw documents to Python structures

5.2 Transform

Removes duplicates

Standardizes difficulty labels

Converts timestamps → dates

Converts viewed/liked/cooked → 0/1

Splits recipe into normalized tables

Cleans malformed / empty data

5.3 Validate

Checks performed by validate_data.py:

Null or missing values

Broken foreign keys

Invalid difficulty fields

Invalid numeric fields

Empty ingredients or steps

Mismatched interaction references

5.4 Load

Exports clean, structured datasets:

recipe.csv

ingredients.csv

steps.csv

interactions.csv

6️⃣ How to Run the Project
1. Install Dependencies
pip install pandas matplotlib firebase-admin seaborn plotly


If needed:

pip install --user pandas matplotlib seaborn plotly

2. Add Firebase Key

Place admin_key.json inside the project folder.

3. Run ETL
python etl_pipeline.py

4. Run Validation
python validate_data.py

5. Run Analytics
python analytics.py


Charts will be stored in:

screenshots/

7️⃣ Analytics & Visualizations

The pipeline generates the following insights:

7.1 Users Chart

Distribution of users and basic engagement counts.

7.2 Recipes Chart

Top recipes based on appearance and metadata.

7.3 Interactions Chart

Bar chart showing views, likes, cooked attempts per recipe.

7.4 Difficulty Pie Chart

Pie chart showing distribution of easy/medium/hard recipes.

7.5 Ingredients Bar Chart

Top ingredients used across all recipes.

8️⃣ Screenshots
Image	Description
<img width="1814" height="905" alt="users" src="https://github.com/user-attachments/assets/e87fb4ed-f4b2-455a-8656-454bbb86303a" />
	User analytics bar chart
<img width="1816" height="912" alt="recipe" src="https://github.com/user-attachments/assets/8943f2ea-0be8-4a2b-a4fe-9a56c4aadf3e" />
	Recipes summary
<img width="1804" height="904" alt="Interactions" src="https://github.com/user-attachments/assets/1e465b7b-70f2-4837-8371-8ec2b424a9b7" />
	Views, likes, cooked chart
<img width="1728" height="894" alt="Piechart" src="https://github.com/user-attachments/assets/b19896e2-3d57-4b75-9ed2-88ed527cbb38" />
  Difficulty distribution
<img width="1876" height="993" alt="Barchart" src="https://github.com/user-attachments/assets/4e46139e-5666-48bd-ae2d-cb24c3d93c8a" />
	Common ingredients bar chart
9️⃣ Known Limitations

Firestore not ideal for relational queries

ETL is batch-based, not real-time

Nested Firestore JSON → CSV flattening is limited

No ratings or comments included

🔟 Future Enhancements

Convert ETL into Apache Airflow DAG

Move datasets to BigQuery

Build Power BI / Tableau dashboards

Add interaction types:

ratings

comments

user engagement scoring

Real-time update pipeline using Firebase Triggers

Dockerize entire solution

1️⃣1️⃣ Conclusion

This project demonstrates a complete, industry-style data engineering workflow using Firebase and Python.
It delivers structured datasets, powerful analytics, and a modular, maintainable architecture suitable for real-world use.
