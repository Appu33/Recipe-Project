from firebase_config import db

# Candidate's main recipe
my_recipe = {
    "id": "r001",
    "name": "Paneer Butter Masala",
    "ingredients": [
        {"name": "Paneer", "quantity": "200g"},
        {"name": "Butter", "quantity": "50g"},
        {"name": "Tomato", "quantity": "3"},
        {"name": "Cream", "quantity": "50ml"}
    ],
    "steps": [
        "Heat butter in a pan",
        "Add tomato puree and cook",
        "Add paneer cubes",
        "Add cream and simmer"
    ],
    "prep_time": 30,
    "difficulty": "Medium"
}

# 20 synthetic recipes
synthetic_recipes = []
for i in range(2, 22):
    synthetic_recipes.append({
        "id": f"r{i:03}",
        "name": f"Recipe {i}",
        "ingredients": [
            {"name": "Ingredient1", "quantity": "100g"},
            {"name": "Ingredient2", "quantity": "50g"}
        ],
        "steps": ["Step 1", "Step 2", "Step 3"],
        "prep_time": 20 + i,
        "difficulty": "Easy" if i % 2 == 0 else "Medium"
    })

# Function to insert recipes
def insert_recipes():
    all_recipes = [my_recipe] + synthetic_recipes
    for recipe in all_recipes:
        db.collection("recipes").document(recipe["id"]).set(recipe)
    print("Recipes added successfully.")

if __name__ == "__main__":
    insert_recipes()
