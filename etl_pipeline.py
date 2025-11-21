from firebase_config import db
import csv

def export_recipes():
    recipes = db.collection("recipes").stream()
    with open("recipe.csv", "w", newline="") as f_r, \
         open("ingredients.csv", "w", newline="") as f_i, \
         open("steps.csv", "w", newline="") as f_s:

        recipe_writer = csv.DictWriter(f_r, fieldnames=["id", "name", "prep_time", "difficulty"])
        recipe_writer.writeheader()

        ingredient_writer = csv.DictWriter(f_i, fieldnames=["recipe_id", "name", "quantity"])
        ingredient_writer.writeheader()

        steps_writer = csv.DictWriter(f_s, fieldnames=["recipe_id", "step_number", "instruction"])
        steps_writer.writeheader()

        for r in recipes:
            r_data = r.to_dict()
            recipe_writer.writerow({
                "id": r_data["id"],
                "name": r_data["name"],
                "prep_time": r_data["prep_time"],
                "difficulty": r_data["difficulty"]
            })
            for ing in r_data["ingredients"]:
                ingredient_writer.writerow({
                    "recipe_id": r_data["id"],
                    "name": ing["name"],
                    "quantity": ing["quantity"]
                })
            for idx, step in enumerate(r_data["steps"], 1):
                steps_writer.writerow({
                    "recipe_id": r_data["id"],
                    "step_number": idx,
                    "instruction": step
                })

def export_interactions():
    interactions = db.collection("interactions").stream()
    with open("interactions.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["recipe_id", "user_id", "viewed", "liked", "rating"])
        writer.writeheader()
        for r in interactions:
            r_data = r.to_dict()
            for interaction in r_data["interactions"]:
                writer.writerow({
                    "recipe_id": r.id,
                    "user_id": interaction["user_id"],
                    "viewed": interaction["viewed"],
                    "liked": interaction["liked"],
                    "rating": interaction["rating"]
                })

if __name__ == "__main__":
    export_recipes()
    export_interactions()
    print("ETL Completed! CSV files generated.")
