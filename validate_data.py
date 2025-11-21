import csv

def validate_recipes():
    valid = []
    invalid = []

    with open("recipe.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            errors = []
            if not row["id"] or not row["name"]:
                errors.append("Missing id or name")
            if int(row["prep_time"]) <= 0:
                errors.append("Prep time must be positive")
            if row["difficulty"] not in ["Easy", "Medium", "Hard"]:
                errors.append("Invalid difficulty")
            
            if errors:
                invalid.append({"row": row, "errors": errors})
            else:
                valid.append(row)
    
    print(f"Valid: {len(valid)}, Invalid: {len(invalid)}")
    if invalid:
        for i in invalid:
            print(i)
    return valid, invalid

if __name__ == "__main__":
    validate_recipes()
