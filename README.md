# 🍽️ Firebase Recipe Project

<p align="center">
  <strong>Candidate:</strong> Apeksha Jadhav &nbsp;|&nbsp;
  <strong>Tools:</strong> Python, Firebase, Pandas, Matplotlib, Seaborn &nbsp;|&nbsp;
  <strong>Date:</strong> November 2025
</p>

---

## 📌 Table of Contents
1. [Overview](#1-overview)
2. [Folder Structure](#2-folder-structure)
   - [Scripts and Files](#21-scripts-and-files)
   - [Data & Config](#22-data--config)
3. [Data Model](#3-data-model)
   - [Users](#31-users)
   - [Recipes](#32-recipes)
   - [Interactions](#33-interactions)
4. [ETL Pipeline](#4-etl-pipeline)
   - [Extract](#41-extract)
   - [Transform](#42-transform)
   - [Load](#43-load)
5. [Data Validation](#5-data-validation)
6. [Analytics & Insights](#6-analytics--insights)
7. [How to Run](#7-how-to-run)
8. [Notes / Limitations](#8-notes--limitations)
9. [Conclusion](#9-conclusion)

---

## 1. Overview
This project implements a **data pipeline using Firebase Firestore** to manage and analyze **recipe, user, and interaction data**.

It **extracts, transforms, validates, and visualizes** data to generate actionable insights on recipes and user engagement.

The pipeline demonstrates **end-to-end data engineering skills**, including:
- ⚙️ **ETL (Extract, Transform, Load)**
- ✅ **Data Validation**
- 📊 **Analytics & Visualization**

---

## 2. Folder Structure

### 2.1 Scripts and Files
| File | Description |
|------|-------------|
| `analytics.py` | Performs analytics and generates visualizations 📊 |
| `etl_pipeline.py` | ETL pipeline for recipes, ingredients, steps, and interactions ⚙️ |
| `firebase_config.py` | Firebase configuration 🔑 |
| `seed_recipes.py` | Seed recipe data into Firebase 🍲 |
| `seed_users.py` | Seed user data 👤 |
| `seed_interactions.py` | Seed interaction data 👍 |
| `validate_data.py` | Data validation script ✅ |

### 2.2 Data & Config
| File/Folder | Description |
|-------------|-------------|
| `recipe.csv` | Exported recipes data 📝 |
| `ingredients.csv` | Exported ingredients data 🌿 |
| `steps.csv` | Exported recipe steps 🔪 |
| `interactions.csv` | Exported user interactions 👥 |
| `admin_key.json` | Firebase service account key 🔐 |
| `screenshots/` | Folder to store charts and visualizations 📸 |

---

## 3. Data Model

### 3.1 Users
**Fields:** `user_id`, `name`, `email`, `age`, `gender`, `created_at` 👤  

### 3.2 Recipes
**Fields:** `recipe_id`, `name`, `description`, `ingredients`, `steps`, `difficulty`, `created_by` 🍲  

### 3.3 Interactions
**Fields:** `interaction_id`, `user_id`, `recipe_id`, `type` (view, like, cook), `timestamp`, `rating` 👍  

**Relationship:** Users interact with Recipes through **Interactions** 🔗  

---

## 4. ETL Pipeline

### 4.1 Extract
Retrieve data from Firebase Firestore collections: `users` 👤, `recipes` 🍲, `interactions` 👍  

### 4.2 Transform
- Normalize data into separate tables: **recipes, ingredients, steps** 📊  
- Clean fields and standardize **difficulty** and **timestamps** 🕒  

### 4.3 Load
Export transformed data into CSV files:
- `recipe.csv` 🍲  
- `ingredients.csv` 🌿  
- `steps.csv` 🔪  
- `interactions.csv` 👥  

**Tools Used:** Python 🐍, `firebase_admin`, `pandas`, `matplotlib`, `seaborn`  

---

## 5. Data Validation

### 5.1 Validation Rules
1. ✅ Required fields must be present  
2. 🔢 Numeric fields must be positive  
3. 📝 Arrays for ingredients and steps must not be empty  
4. 🌟 Difficulty must be Easy, Medium, or Hard  

### 5.2 Validation Script
`validate_data.py` generates a **report showing valid and invalid records with reasons** 🧐  

---

## 6. Analytics & Insights

### 6.1 Sample Insights
| # | Insight | Emoji |
|---|---------|-------|
| 1 | Top recipes based on likes and cook attempts | 🏆 |
| 2 | Most common ingredients across recipes | 🌿 |
| 3 | Average preparation time by difficulty | ⏱️ |
| 4 | Difficulty distribution of recipes | 📊 |
| 5 | Correlation between prep time and likes | 🔄 |
| 6 | Most frequently viewed recipes | 👀 |
| 7 | Ingredients associated with high engagement | 💡 |
| 8 | Users with highest interactions | 👥 |
| 9 | Interaction type distribution (views, likes, cooks) | 📈 |
| 10 | Recipes with highest average rating | 🥇 |

Visualizations include **bar charts, pie charts, and ingredient frequency plots** 📸  

---

## 7. How to Run

### 7.1 Install Dependencies
```bash
pip install -r requirements.txt
7.2 Seed Firebase Data (Optional)
bash
Copy code
python seed_users.py
python seed_recipes.py
python seed_interactions.py
7.3 Run ETL Pipeline
bash
Copy code
python etl_pipeline.py
7.4 Validate Data
bash
Copy code
python validate_data.py
7.5 Generate Analytics
bash
Copy code
python analytics.py
8. Notes / Limitations
🆔 Recipe IDs in Firebase are auto-generated

👀 User interactions are preserved even if recipes are deleted

⏱️ Analytics are batch-oriented, not real-time

📸 Charts are stored in the screenshots/ folder

9. Conclusion
This project demonstrates a complete Firebase-based data engineering workflow, including:

🗂️ Data modeling and normalization

⚙️ ETL pipeline implementation

✅ Data quality validation

📊 Analytics and visualization insights

The pipeline provides meaningful insights into recipe management and user engagement, suitable for real-world applications 🌟

<p align="center">Made with ❤️ by Apeksha Jadhav</p> ```
