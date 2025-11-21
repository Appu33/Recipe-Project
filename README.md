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

<p align="center">
<img src="https://img.shields.io/badge/ETL-%E2%9A%99-blue?style=for-the-badge" alt="ETL"/>
<img src="https://img.shields.io/badge/Analytics-%F0%9F%93%8A-yellow?style=for-the-badge" alt="Analytics"/>
<img src="https://img.shields.io/badge/Validation-%E2%9C%85-green?style=for-the-badge" alt="Validation"/>
<img src="https://img.shields.io/badge/Data%20Model-%F0%9F%97%82-orange?style=for-the-badge" alt="Data Model"/>
</p>

**Key Features:**  
- ⚙️ **ETL Pipeline:** Extract, transform, and load data from Firebase  
- ✅ **Data Validation:** Ensure completeness and correctness of the data  
- 📊 **Analytics & Visualization:** Generate actionable insights  
- 🍲 **Recipe Management:** Includes candidate’s own recipes and synthetic data  
- 👥 **User Interactions:** Tracks views, likes, and cook attempts  

**Goal:** Demonstrate end-to-end data engineering skills, from **data modeling and ETL** to **analytics and visualization**, using Firebase as the source system.

---

## 📌 Table of Contents
1. [Overview](#-overview)  
2. [Folder Structure](#folder-structure)  
3. [Data Model](#data-model)  
4. [ETL Pipeline](#etl-pipeline)  
5. [Data Validation](#data-validation)  
6. [Analytics & Insights](#analytics--insights)  
7. [Complete 7-Step Process (Run + Notes + Conclusion)](#complete-7-step-process-run--notes--conclusion)  

---

<details>
<summary>2. 📁 Folder Structure</summary>

### Scripts and Files
| File | Description |
|------|-------------|
| `analytics.py` | Performs analytics and generates visualizations 📊 |
| `etl_pipeline.py` | ETL pipeline for recipes, ingredients, steps, and interactions ⚙️ |
| `firebase_config.py` | Firebase configuration 🔑 |
| `seed_recipes.py` | Seed recipe data into Firebase 🍲 |
| `seed_users.py` | Seed user data 👤 |
| `seed_interactions.py` | Seed interaction data 👍 |
| `validate_data.py` | Data validation script ✅ |

### Data & Config
| File/Folder | Description |
|-------------|-------------|
| `recipe.csv` | Exported recipes data 📝 |
| `ingredients.csv` | Exported ingredients data 🌿 |
| `steps.csv` | Exported recipe steps 🔪 |
| `interactions.csv` | Exported user interactions 👥 |
| `admin_key.json` | Firebase service account key 🔐 |
| `screenshots/` | Folder to store charts and visualizations 📸 |

</details>

<details>
<summary>3. 🗂️ Data Model</summary>

### Users
**Fields:** `user_id`, `name`, `email`, `age`, `gender`, `created_at` 👤  

### Recipes
**Fields:** `recipe_id`, `name`, `description`, `ingredients`, `steps`, `difficulty`, `created_by` 🍲  

### Interactions
**Fields:** `interaction_id`, `user_id`, `recipe_id`, `type` (view, like, cook), `timestamp`, `rating` 👍  

**Relationship:** Users interact with Recipes through **Interactions** 🔗  

</details>

<details>
<summary>4. ⚙️ ETL Pipeline</summary>

### Workflow
- **Extract:** Retrieve data from Firebase Firestore collections (`users`, `recipes`, `interactions`) 👤🍲👍  
- **Transform:** Normalize data into **recipes, ingredients, steps** tables 📊, clean fields, standardize difficulty and timestamps 🕒  
- **Load:** Export to CSV files: `recipe.csv` 🍲, `ingredients.csv` 🌿, `steps.csv` 🔪, `interactions.csv` 👥  

**Tools Used:** Python 🐍, `firebase_admin`, `pandas`, `matplotlib`, `seaborn`  

</details>

<details>
<summary>5. ✅ Data Validation</summary>

### Validation Rules
- ✅ Required fields must be present  
- 🔢 Numeric fields must be positive  
- 📝 Arrays for ingredients and steps must not be empty  
- 🌟 Difficulty must be Easy, Medium, or Hard  

### Validation Report
`validate_data.py` generates a **report of valid and invalid records** 🧐  

</details>

<details>
<summary>6. 📊 Analytics & Insights</summary>

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

**Visualizations:** bar charts, pie charts, ingredient frequency plots 📸  

</details>

<details>
<summary>7. 🚀 Complete 7-Step Process (Run + Notes + Conclusion)</summary>

<ol>
<li>
  <strong>Install Dependencies</strong><br>
  <code>pip install -r requirements.txt</code>
</li>

<li>
  <strong>Seed Firebase Data (Optional)</strong><br>
  <code>python seed_users.py</code><br>
  <code>python seed_recipes.py</code><br>
  <code>python seed_interactions.py</code>
</li>

<li>
  <strong>Run ETL Pipeline</strong><br>
  <code>python etl_pipeline.py</code>
</li>

<li>
  <strong>Validate Data</strong><br>
  <code>python validate_data.py</code>
</li>

<li>
  <strong>Generate Analytics</strong><br>
  <code>python analytics.py</code>
</li>

<li>
  <strong>Notes / Limitations</strong>
  <ul>
    <li>🆔 Recipe IDs in Firebase are <strong>auto-generated</strong></li>
    <li>👀 User interactions are <strong>preserved</strong> even if recipes are deleted</li>
    <li>⏱️ Analytics are <strong>batch-oriented</strong>, not real-time</li>
    <li>📸 Charts are stored in the <code>screenshots/</code> folder</li>
    <li>⚠️ Some recipes and interactions are <strong>synthetic</strong> for testing</li>
    <li>🐍 ETL and analytics are implemented in Python; scaling for large datasets may require optimization</li>
    <li>🔗 Data relationships must be maintained carefully to avoid orphaned records</li>
  </ul>
</li>

<li>
  <strong>Conclusion</strong>
  <p>This project demonstrates a <strong>full end-to-end Firebase-based data engineering workflow</strong>:</p>
  <ul>
    <li>🗂️ <strong>Data Modeling & Normalization:</strong> Structured recipes, ingredients, steps, users, and interactions</li>
    <li>⚙️ <strong>ETL Pipeline:</strong> Efficiently extracting, transforming, and loading data</li>
    <li>✅ <strong>Data Quality Validation:</strong> Ensuring integrity, consistency, and correctness</li>
    <li>📊 <strong>Analytics & Visualization:</strong> Generating actionable insights for recipe engagement</li>
  </ul>
  <p><strong>Future Scope:</strong> Can be extended to support <strong>real-time analytics</strong> or integrated with a frontend application for dynamic recipe recommendations.</p>
  <p align="center">Made with ❤️ by <strong>Apeksha Jadhav</strong></p>
</li>
</ol>
</details>
