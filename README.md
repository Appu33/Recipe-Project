       ┌───────────────┐
       │   Firebase    │
       │   Firestore   │
       │  (Users,      │
       │   Recipes,    │
       │  Interactions)│
       └─────┬─────────┘
             │ Extract / Seed Data
             ▼
  ┌─────────────────────────┐
  │   Seed Scripts (Python) │
  │ seed_users.py           │
  │ seed_recipes.py         │
  │ seed_interactions.py    │
  └─────────┬───────────────┘
            │ Extract Data
            ▼
      ┌───────────────┐
      │  ETL Pipeline │
      │ (etl_pipeline.py) │
      │ Transform & Load │
      └─────┬─────────┘
            │ Export CSV
            ▼
      ┌───────────────┐
      │   CSV Files   │
      │ recipe.csv    │
      │ ingredients.csv │
      │ steps.csv     │
      │ interactions.csv │
      └─────┬─────────┘
            │ Data Validation
            ▼
      ┌───────────────┐
      │ validate_data │
      │     .py       │
      │ Valid/Invalid │
      │ Records Report│
      └─────┬─────────┘
            │ Analytics & Insights
            ▼
      ┌───────────────┐
      │ analytics.py  │
      │ Visualizations│
      │ Bar / Pie /   │
      │ Ingredient    │
      │ Frequency Plots│
      └───────────────┘
