# 🍽️ Firebase Recipe Project

<p align="center">
  <strong>Candidate:</strong> Apeksha Jadhav &nbsp;|&nbsp;
  <strong>Date:</strong> November 2025
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" alt="Python Version"/>
<img src="https://img.shields.io/badge/Pandas-2.0.3-lightgrey?style=for-the-badge&logo=pandas" alt="Pandas Version"/>
<img src="https://img.shields.io/badge/Firebase-9.23.0-orange?style=for-the-badge&logo=firebase" alt="Firebase Version"/>
</p>

---

## 🌟 Overview
This project implements a **complete Firebase-based data engineering workflow** for managing and analyzing **recipe, user, and interaction data**.  

**Key Features:**  
- ⚙️ **ETL Pipeline:** Extract, transform, and load data from Firebase  
- ✅ **Data Validation:** Ensure completeness and correctness of the data  
- 📊 **Analytics & Visualization:** Generate actionable insights  
- 🍲 **Recipe Management:** Includes candidate’s own recipes and synthetic data  
- 👥 **User Interactions:** Tracks views, likes, and cook attempts  

**Goal:** Demonstrate end-to-end data engineering skills, from **data modeling and ETL** to **analytics and visualization**, using Firebase as the source system.

---

## 📌 Table of Contents
1. [Folder Structure](#folder-structure)
2. [Data Model](#data-model)
3. [ETL Pipeline](#etl-pipeline)
4. [Data Validation](#data-validation)
5. [Analytics & Insights](#analytics--insights)
6. [How to Run](#how-to-run)
7. [Notes / Limitations](#notes--limitations)
8. [Conclusion](#conclusion)
9. [Files and Screenshots](#files-and-screenshots)

---

## 1. 📁 Folder Structure

### 1.1 Scripts and Files
| File | Description |
|------|-------------|
| `analytics.py` | Performs analytics and generates visualizations 📊 |
| `etl_pipeline.py` | ETL pipeline for recipes, ingredients, steps, and interactions ⚙️ |
| `firebase_config.py` | Firebase configuration 🔑 |
| `seed_recipes.py` | Seed recipe data into Firebase 🍲 |
| `seed_users.py` | Seed user data 👤 |
| `seed_interactions.py` | Seed interaction data 👍 |
| `validate_data.py` | Data validation script ✅ |

### 1.2 Data & Config
| File/Folder | Description |
|-------------|-------------|
| [`recipe.csv`](recipe.csv) | Exported recipes data 📝 |
| [`ingredients.csv`](ingredients.csv) | Exported ingredients data 🌿 |
| [`steps.csv`](steps.csv) | Exported recipe steps 🔪 |
| [`interactions.csv`](interactions.csv) | Exported user interactions 👥 |
| `admin_key.json` | Firebase service account key 🔐 |
| [`screenshots/`](screenshots/) | Folder to store charts and visualizations 📸 |

---

## 2. 🗂️ Data Model

### Users
**Fields:** `user_id`, `name`, `email`, `age`, `gender`, `created_at` 👤  

### Recipes
**Fields:** `recipe_id`, `name`, `description`, `ingredients`, `steps`, `difficulty`, `created_by` 🍲  

### Interactions
**Fields:** `interaction_id`, `user_id`, `recipe_id`, `type` (view, like, cook), `timestamp`, `rating` 👍  

**Relationship:** Users interact with Recipes through **Interactions** 🔗  

---

## 3. ⚙️ ETL Pipeline

### Workflow
- **Extract:** Retrieve data from Firebase Firestore collections (`users`, `recipes`, `interactions`) 👤🍲👍  
- **Transform:** Normalize data into **recipes, ingredients, steps** tables 📊, clean fields, standardize difficulty and timestamps 🕒  
- **Load:** Export to CSV files: [`recipe.csv`](recipe.csv), [`ingredients.csv`](ingredients.csv), [`steps.csv`](steps.csv), [`interactions.csv`](interactions.csv) 👥  

**Tools Used:** Python 🐍, `firebase_admin`, `pandas`, `matplotlib`, `seaborn`  

---

### ETL Progress
ETL Pipeline [██████████] 100%
Data Cleaning [█████████ ] 90%
Normalization [████████ ] 80%
CSV Export [██████████] 100%

yaml
Copy code

---

## 4. ✅ Data Validation

### Validation Rules
- ✅ Required fields must be present  
- 🔢 Numeric fields must be positive  
- 📝 Arrays for ingredients and steps must not be empty  
- 🌟 Difficulty must be Easy, Medium, or Hard  

### Validation Report
`validate_data.py` generates a **report of valid and invalid records** 🧐  

---

## 5. 📊 Analytics & Insights

### Sample Insights
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

**Visualizations:** Bar charts, pie charts, ingredient frequency plots 📸  

---

## 6. 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Seed Firebase Data (Optional)
python seed_users.py
python seed_recipes.py
python seed_interactions.py

# Run ETL Pipeline
python etl_pipeline.py

# Validate Data
python validate_data.py

# Generate Analytics
python analytics.py
7. ⚠️ Notes / Limitations
🆔 Recipe IDs in Firebase are auto-generated

👀 User interactions are preserved even if recipes are deleted

⏱️ Analytics are batch-oriented, not real-time

📸 Charts generated by analytics are stored in the screenshots/ folder

⚡ Some recipes or interactions may be synthetic for testing purposes

8. 📝 Conclusion
This project demonstrates a complete Firebase-based data engineering workflow, showcasing:

🗂️ Data Modeling & Normalization: Structured recipes, ingredients, steps, users, and interactions

⚙️ ETL Pipeline: Efficiently extracting, transforming, and loading data

✅ Data Quality Validation: Ensuring data integrity and consistency

📊 Analytics & Visualization: Generating actionable insights to understand user engagement and recipe popularity

This workflow can be extended for real-time analytics or integrated with a frontend for dynamic recipe recommendations.

Candidate: Apeksha Jadhav
Tools Used: Python, Firebase, Pandas, Matplotlib, Seaborn
Date: November 2025

9. 📂 Files and Screenshots
Data Files
recipe.csv

ingredients.csv

steps.csv

interactions.csv

Screenshots
Charts generated are stored in the screenshots/ folder:

Bar charts

Pie charts

