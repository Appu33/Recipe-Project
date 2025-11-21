import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
recipes = pd.read_csv("recipe.csv")
ingredients = pd.read_csv("ingredients.csv")
interactions = pd.read_csv("interactions.csv")

# 1. Most common ingredients (Bar Chart)
top_ingredients = ingredients["name"].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_ingredients.values, y=top_ingredients.index, palette="viridis")
plt.title("Top 10 Most Common Ingredients")
plt.xlabel("Count")
plt.ylabel("Ingredient")
plt.show()

# 2. Difficulty distribution (Pie Chart)
difficulty_counts = recipes["difficulty"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(difficulty_counts, labels=difficulty_counts.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Recipe Difficulty Distribution")
plt.show()

# 3. Most liked recipes (Horizontal Bar Chart)
likes_summary = interactions.groupby("recipe_id")["liked"].sum().sort_values(ascending=False)
top_liked_recipes = likes_summary.head(5)
plt.figure(figsize=(10,5))
sns.barplot(x=top_liked_recipes.values, y=top_liked_recipes.index, palette="coolwarm")
plt.title("Top 5 Liked Recipes")
plt.xlabel("Number of Likes")
plt.ylabel("Recipe ID")
plt.show()

# 4. Correlation prep_time vs likes (Scatter Plot)
like_counts = interactions.groupby("recipe_id")["liked"].sum()
prep_like = pd.merge(recipes[["id", "prep_time"]], like_counts, left_on="id", right_index=True)
plt.figure(figsize=(8,5))
sns.scatterplot(data=prep_like, x="prep_time", y="liked")
plt.title("Prep Time vs Likes")
plt.xlabel("Preparation Time (minutes)")
plt.ylabel("Number of Likes")
plt.show()

# 5. Average prep time (Simple annotation)
avg_prep_time = recipes["prep_time"].mean()
print(f"Average Preparation Time: {avg_prep_time:.2f} minutes")
