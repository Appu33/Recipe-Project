import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSVs
recipes = pd.read_csv("recipe.csv")
ingredients = pd.read_csv("ingredients.csv")
interactions = pd.read_csv("interactions.csv")

print("\n==================== UPGRADED ANALYTICS REPORT ====================\n")

# ----------------------- Table Insights -----------------------
# 1. Most common ingredients
top_ingredients = ingredients["name"].value_counts().head(10)
print("1. Top 10 Ingredients:")
print(top_ingredients, "\n")

# 2. Average preparation time
avg_prep = recipes["prep_time"].mean()
print(f"2. Average Preparation Time: {avg_prep:.2f} minutes\n")

# 3. Difficulty distribution
difficulty_dist = recipes["difficulty"].value_counts()
print("3. Difficulty Distribution:")
print(difficulty_dist, "\n")

# 4. Correlation Prep Time vs Likes
likes_summary = interactions.groupby("recipe_id")["liked"].sum()
prep_like = pd.merge(recipes[["id","prep_time"]], likes_summary, left_on="id", right_index=True)
correlation = prep_like["prep_time"].corr(prep_like["liked"])
print(f"4. Correlation Prep Time vs Likes: {correlation:.4f}\n")

# 5. Top 5 Most Viewed Recipes
top_viewed = interactions.groupby("recipe_id")["viewed"].sum().sort_values(ascending=False).head(5)
print("5. Top 5 Most Viewed Recipes:")
print(top_viewed, "\n")

# 6. Ingredients with high engagement
merged_ing = pd.merge(ingredients, likes_summary, left_on="recipe_id", right_index=True)
top_eng_ing = merged_ing.groupby("name")["liked"].sum().sort_values(ascending=False).head(10)
print("6. Ingredients with High Engagement:")
print(top_eng_ing, "\n")

# 7. Average calories per recipe
if "calories" in recipes.columns:
    avg_calories = recipes["calories"].mean()
    print(f"7. Average Calories per Recipe: {avg_calories:.2f} kcal\n")
else:
    print("7. Calories data not available.\n")

# 8. Top cuisines
if "cuisine" in recipes.columns:
    top_cuisines = recipes["cuisine"].value_counts().head(5)
    print("8. Top 5 Cuisines:")
    print(top_cuisines, "\n")
else:
    top_cuisines = pd.Series()

# 9. Top tags
if "tags" in recipes.columns:
    tags_series = recipes["tags"].dropna().apply(lambda x: x.split(","))
    tags_flat = [tag for sublist in tags_series for tag in sublist]
    top_tags = pd.Series(tags_flat).value_counts().head(5)
    print("9. Top 5 Tags:")
    print(top_tags, "\n")
else:
    top_tags = pd.Series()

# 10. Average session duration per recipe
if "session_duration" in interactions.columns:
    avg_session = interactions.groupby("recipe_id")["session_duration"].mean().sort_values(ascending=False).head(5)
    print("10. Top 5 Recipes by Avg Session Duration:")
    print(avg_session, "\n")

# ----------------------- Plots -----------------------
sns.set_style("whitegrid")

# 1️⃣ Top 10 Ingredients (bar)
plt.figure(figsize=(10,6))
sns.barplot(x=top_ingredients.values, y=top_ingredients.index, palette="viridis")
plt.title("Top 10 Ingredients")
plt.xlabel("Count")
plt.ylabel("Ingredient")
plt.show()

# 2️⃣ Difficulty Distribution (pie)
plt.figure(figsize=(6,6))
difficulty_dist.plot.pie(autopct="%1.1f%%", colors=sns.color_palette("pastel"), startangle=140)
plt.title("Difficulty Distribution")
plt.ylabel("")
plt.show()

# 3️⃣ Top 5 Liked Recipes (horizontal bar)
top_liked = interactions.groupby("recipe_id")["liked"].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(10,5))
sns.barplot(x=top_liked.values, y=top_liked.index, palette="coolwarm")
plt.title("Top 5 Liked Recipes")
plt.xlabel("Likes")
plt.ylabel("Recipe ID")
plt.show()

# 4️⃣ Top 5 Viewed Recipes (horizontal bar)
plt.figure(figsize=(10,5))
sns.barplot(x=top_viewed.values, y=top_viewed.index, palette="magma")
plt.title("Top 5 Viewed Recipes")
plt.xlabel("Views")
plt.ylabel("Recipe ID")
plt.show()

# 5️⃣ Prep Time vs Likes (scatter)
plt.figure(figsize=(8,5))
sns.scatterplot(data=prep_like, x="prep_time", y="liked", s=100, color="green")
plt.title("Prep Time vs Likes")
plt.xlabel("Preparation Time (minutes)")
plt.ylabel("Likes")
plt.show()

# 6️⃣ Average Calories per Difficulty (bar)
if "calories" in recipes.columns:
    avg_cal_diff = recipes.groupby("difficulty")["calories"].mean()
    plt.figure(figsize=(8,5))
    sns.barplot(x=avg_cal_diff.index, y=avg_cal_diff.values, palette="autumn")
    plt.title("Average Calories per Difficulty")
    plt.ylabel("Calories")
    plt.show()

# 7️⃣ Top Cuisines (bar)
if not top_cuisines.empty:
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette="Set2")
    plt.title("Top 5 Cuisines")
    plt.xlabel("Count")
    plt.ylabel("Cuisine")
    plt.show()

# 8️⃣ Top Tags (bar)
if not top_tags.empty:
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_tags.values, y=top_tags.index, palette="cool")
    plt.title("Top 5 Tags")
    plt.xlabel("Count")
    plt.ylabel("Tag")
    plt.show()

# 9️⃣ Average Session Duration per Recipe (bar)
if "session_duration" in interactions.columns:
    plt.figure(figsize=(10,5))
    sns.barplot(x=avg_session.values, y=avg_session.index, palette="cividis")
    plt.title("Top 5 Recipes by Avg Session Duration")
    plt.xlabel("Avg Session Duration (seconds)")
    plt.ylabel("Recipe ID")
    plt.show()

print("==================== END OF REPORT ====================\n")
