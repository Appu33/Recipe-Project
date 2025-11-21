from firebase_config import db
import random

user_ids = ["u001", "u002", "u003", "u004", "u005"]

def seed_interactions():
    recipes = db.collection("recipes").stream()
    for recipe in recipes:
        interactions = []
        for user in user_ids:
            interactions.append({
                "user_id": user,
                "viewed": random.choice([True, False]),
                "liked": random.choice([True, False]),
                "rating": random.randint(1, 5)
            })
        db.collection("interactions").document(recipe.id).set({"interactions": interactions})
    print("User interactions added successfully.")

if __name__ == "__main__":
    seed_interactions()
