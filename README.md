RECIPE PROJECT

🍽️ FIREBASE RECIPE ANALYTICS PIPELINE

A Complete ETL + Analytics Project Using Firebase Firestore & Python

📌 PROJECT OVERVIEW

This project implements a complete data engineering pipeline that:
Extracts recipe, user, and interaction data from Firebase Firestor Transforms, validates, and normalizes the data using Python Loads clean structured data into CSV datasets Generates visual and statistical analytics insights


THIS PROJECT DEMONSTRATES:

🔥 Firebase Database Integration

🧱 Proper Data Modeling

🔄 ETL Pipeline (Extract → Transform → Load)

✔ Data Quality Validation

📊 Analytics & Charts

📁 Production-ready folder structure

📝 Industry-grade documentation

📂 PROJECT STRUCTURE
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

🧱 DATA MODEL

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
🔄 ETL PIPELINE(etl_pipeline.py)

1️⃣EXTRACT

Connects to Firestore using firebase_config.py

Fetches collections:

recipes

users

interactions

Saves raw data to CSV

2️⃣ TRANSFORM

Cleans and standardizes:

Removes duplicates

Converts timestamps to date

Standardizes difficulty labels

Converts viewed/liked/cooked → 0/1

Removes blank or malformed rows

3️⃣ VALIDATE(validate_data.py)

Quality checks performed:

Missing or null values

Broken foreign keys

Invalid difficulty fields

Incorrect datatypes

Empty ingredient/step lists

4️⃣ LOAD

Outputs final normalized CSV files:

recipe.csv

ingredients.csv

steps.csv

interactions.csv

📊 ANALYTICS (analytics.py)

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

🧪 HOW TO RUN THIS PROJECT

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

⚠️KNOWN LIMITATIONS


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

OUTPUT:
1] USERS DETAILS:
<img width="1814" height="905" alt="users" src="https://github.com/user-attachments/assets/e65cf045-6cbb-429d-9b63-f2d479bc5068" />
📘 Description:

This image shows the Users collection in Firebase Firestore.
Each user document includes:
1]User ID
2]Name
3]Email
4]Created_at timestamp
This dataset helps track who interacts with recipes, forming the basis for interactions analytics such as views, likes, and cook attempts.

2]RECIPE DETAILS:
<img width="1816" height="912" alt="recipe" src="https://github.com/user-attachments/assets/bc09dfdc-9039-4577-a673-b27d65cfd7eb" />

📘 Description:

This image shows the Recipes collection inside Firebase Firestore.

It displays:

1]Recipe IDs

2]Title
3]Difficulty
4]Ingredients array
5]Step-by-step instructions
6]Created_by (User ID reference)
This represents the raw data source your ETL pipeline extracts before transforming and normalizing it into CSV files.

3]INTERACTION DETAILS:
<img width="1804" height="904" alt="Interactions" src="https://github.com/user-attachments/assets/60257a82-7c5e-481a-bc2f-8ad82c982dee" />
This bar chart visualizes user engagement across recipes.
Each bar represents a different recipe (identified by recipe IDs), and the height of the bar shows how many times that recipe was:
1]Viewed
2]Liked
3]Cooked (attempted)
The chart clearly shows which recipes are the most popular among users.
This metric measures real engagement beyond browsing — it shows which recipes users actually use.
4]PIECHART
<img width="1728" height="894" alt="Piechart" src="https://github.com/user-attachments/assets/56fa63b2-641a-43b4-8156-cd89f67142a6" />
📘 Description:
This pie chart visualizes the distribution of recipes based on their difficulty levels.
The chart divides recipes into three categories:
1]Easy
2]Medium
3]Hard
Each slice represents the percentage share of that difficulty category in the entire dataset.
This chart helps quickly understand whether your recipe collection leans more toward simple dishes or advanced ones.

5]BARCHART
<img width="1876" height="993" alt="Barchart" src="https://github.com/user-attachments/assets/6233e252-35d1-4637-b78f-853668331f59" />
📘 Description:
This bar chart displays the top most frequently used ingredients across all recipes.
1]The Y-axis lists ingredient names.
2]The X-axis shows the number of recipes that include each ingredient.
This visualization highlights which ingredients are the most common (e.g., Salt, Onion, Tomato), helping identify cooking patterns and recipe trends.





🔚 CONCLUSION

This project delivers a complete end-to-end ETL and analytics pipeline built on Firebase and Python. It converts raw Firestore data into clean, validated CSV datasets and generates meaningful insights with visual charts. The structure is modular, easy to extend, and serves as a strong foundation for real-world data engineering workflows.
