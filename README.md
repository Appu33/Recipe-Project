.

🍽️ Firebase Recipe Analytics Pipeline
A Complete End-to-End ETL + Analytics Project Using Firebase Firestore & Python
📌 Project Overview
<pre> ``` This project implements a complete data engineering pipeline that: - Extracts recipe, user, and interaction data from Firebase Firestore - Transforms, validates, and normalizes the data using Python - Loads clean structured data into CSV datasets - Generates visual and statistical analytics insights This project demonstrates: - Firebase Database Integration - Proper Data Modeling - ETL Pipeline (Extract → Transform → Load) - Data Quality Validation - Analytics & Charts - Production-ready folder structure - Industry-grade documentation ``` </pre>
📁 Project Structure
<pre> ``` Recipeproject/ ├── README.md ├── admin_key.json ├── firebase_config.py ├── etl_pipeline.py ├── validate_data.py ├── analytics.py ├── seed_recipes.py ├── seed_users.py ├── seed_interactions.py ├── recipe.csv ├── ingredients.csv ├── steps.csv ├── interactions.csv ├── screenshots/ <-- Add your screenshots here manually └── __pycache__/ ``` </pre>
🧱 Data Model
<pre> ``` Recipe (recipe.csv) ├─ id → Recipe ID ├─ title → Recipe Name ├─ prep_time → Preparation time (minutes) ├─ difficulty → easy / medium / hard └─ created_by → User ID (FK → users) Ingredients (ingredients.csv) ├─ recipe_id → FK → recipe.id └─ name → Ingredient name Steps (steps.csv) ├─ recipe_id → FK → recipe.id ├─ step_no → Step number └─ description → Step instructions Interactions (interactions.csv) ├─ user_id → FK → users ├─ recipe_id → FK → recipe ├─ viewed → 1 = viewed, 0 = not viewed ├─ liked → 1 = liked, 0 = not liked └─ cooked → 1 = attempted cook, 0 = not attempted ``` </pre>
🔄 ETL Pipeline (etl_pipeline.py)
<pre> ``` 1️⃣ EXTRACT - Connects to Firestore using firebase_config.py - Fetches collections: recipes, users, interactions - Saves raw data to CSV 2️⃣ TRANSFORM - Removes duplicates - Converts timestamps to date - Standardizes difficulty labels - Converts viewed/liked/cooked → 0/1 - Removes blank or malformed rows 3️⃣ VALIDATE (validate_data.py) - Checks for missing/null values - Broken foreign keys - Invalid difficulty fields - Incorrect datatypes - Empty ingredient/step lists 4️⃣ LOAD - Outputs final normalized CSV files: recipe.csv, ingredients.csv, steps.csv, interactions.csv ``` </pre>
📊 Analytics (analytics.py)
<pre> ``` Run: python analytics.py Generates insights: - Most common ingredients - Average preparation time - Difficulty distribution - Top viewed recipes - Top liked recipes - Correlation: prep_time vs likes - User engagement metrics Visual charts are automatically saved inside: screenshots/ ``` </pre>
📈 Example Insights
<pre> ``` Insight | Example Output ---------------------------|---------------- Average prep time | 22 minutes Most common ingredient | Salt Most liked recipe | r001 Most viewed recipe | r001 Strongest correlation | prep_time vs likes ``` </pre>
📸 Analytics Screenshots
<pre> ``` Add your screenshots manually inside the screenshots/ folder and link them like this: Top Ingredients: ![Top Ingredients](screenshots/top_ingredients.png) Difficulty Distribution: ![Difficulty Distribution](screenshots/difficulty_distribution.png) Most Viewed Recipes: ![Most Viewed](screenshots/most_viewed.png) Most Liked Recipes: ![Most Liked](screenshots/most_liked.png) ``` </pre>
🧪 How to Run This Project
<pre> ``` 1️⃣ Install Dependencies pip install pandas matplotlib firebase-admin seaborn plotly If permission issues: pip install --user pandas matplotlib seaborn plotly 2️⃣ Add Firebase Admin Key Place admin_key.json inside the project folder 3️⃣ Run ETL python etl_pipeline.py 4️⃣ Run Data Validation (optional) python validate_data.py 5️⃣ Run Analytics python analytics.py Charts will be saved under: screenshots/ ``` </pre>
⚠️ Known Limitations
<pre> ``` - Firestore is not optimized for heavy relational workloads - ETL runs in batch mode, not real-time - CSV export cannot store nested JSON perfectly - Analytics limited to available interaction types (no ratings/comments) ``` </pre>
🚀 Future Enhancements
<pre> ``` - Convert this pipeline into an Apache Airflow DAG - Store cleaned data in BigQuery instead of CSV - Build a full Power BI / Tableau dashboard - Add recipe ratings, comments, user segmentation - Add real-time streaming using Firebase triggers - Dockerize the entire pipeline ``` </pre>
🔚 Conclusion
<pre> ``` This project delivers a complete end-to-end ETL and analytics pipeline built on Firebase and Python. It converts raw Firestore data into clean, validated CSV datasets and generates meaningful insights with visual charts. The structure is modular, easy to extend, and serves as a strong foundation for real-world data engineering workflows. ``` </pre>
