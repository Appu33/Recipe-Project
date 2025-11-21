# Recipe-Project

🥘 Firebase-Based Recipe Analytics Pipeline

This project is part of the Data Engineering Assessment.
It builds an end-to-end ETL + Analytics pipeline using Firebase (Firestore) as the source system.

🔧 1. Data Model

The project uses three main collections in Firestore.

📘 Recipes Collection

Stores all recipes uploaded by users.

Field	Type	Description
recipe_id	string	Unique ID (e.g., r001)
title	string	Recipe name
ingredients	array/text	List of ingredients
steps	array/text	Cooking steps
cooking_time	number	Time in minutes
created_by	string	user_id of the creator
created_at	timestamp	Creation time
👤 Users Collection

Stores basic user profile data.

Field	Type	Description
user_id	string	Unique ID
name	string	Full name
email	string	Email address
joined_at	timestamp	Account creation time
⭐ User Interactions Collection

Tracks how users interact with recipes.

Field	Type	Description
interaction_id	string	Unique ID
user_id	string	User performing the action
recipe_id	string	Recipe they interacted with
interaction_type	string	view / like / cook_attempt
timestamp	timestamp	When the interaction happened

Relationships:

A User can interact with many Recipes

A Recipe can have many Interactions

Interactions link Users ↔ Recipes

🛠 2. Instructions for Running the Pipeline

Follow the steps below to run the ETL pipeline in VS Code.

Step 1 — Install Dependencies
pip install firebase-admin pandas

Step 2 — Add Firebase Credentials

Download your Firebase serviceAccountKey.json and place it in the project directory.

Folder structure:

project/
│── serviceAccountKey.json
│── etl_extract.py
│── etl_transform.py
│── etl_load.py
│── analytics.ipynb / analytics.py

Step 3 — Run Extract Script
python etl_extract.py


This will pull recipes, users, and interactions from Firestore and save them as raw CSV files.

Step 4 — Run Transform Script
python etl_transform.py


This script:

cleans missing values

fixes data types

formats timestamps

removes duplicates

validates fields

You get cleaned CSV files.

Step 5 — Run Load Script (Optional)
python etl_load.py


This loads cleaned data into:

SQL databases

Data warehouse

Or keeps them as clean CSV files

Output Files (Normalized)

recipes_clean.csv

users_clean.csv

interactions_clean.csv

🔄 3. ETL Process Overview
Extract

Connects to Firebase using Admin SDK

Reads data from 3 collections

Dumps to raw .csv

Transform

Data quality rules applied:

Remove duplicates

Validate recipe_id & user_id

Standardize timestamp format

Convert cooking_time to integer

Clean empty ingredients/steps

Load

Save normalized CSV

Optional: Load into PostgreSQL / BigQuery

Ready for analytics & visualization

📊 4. Insights Summary (Analytics)

The analytics file generates the following insights:

🍽 Top 5 Most Viewed Recipes

Shows recipes with the highest number of view interactions.

❤️ Most Liked Recipes

Ranks recipes by number of like interactions.

🔥 Most Cooked Recipes

Based on cook_attempt interactions — shows real engagement.

👨‍🍳 Most Active User

User with highest:

views

likes

cook attempts

⏱ Hourly / Daily Interaction Trend

Identifies when users engage most with recipes.

📈 Dashboard-Ready CSV

All analytics outputs can be visualized using:

Power BI

Tableau

Python Matplotlib

Excel

⚠️ 5. Known Constraints / Limitations

Firebase querying is limited (no heavy joins).

Pipeline depends on internet connection.

Data size small since manual entry.

No real-time streaming (batch only).

If Firebase schema changes → scripts need updates.

Timestamps assumed to be valid and properly formatted.

No complex NLP on ingredients/steps (basic cleaning only).

🎯 Conclusion

This project demonstrates:

Data modeling

ETL pipeline creation

Firebase integration

Data cleaning

Analytics and insights generation
