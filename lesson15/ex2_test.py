import json

# Creează obiect Python
data = {
    "name": "Roxana",
    "age": 30,
    "skills": ["Python", "FastAPI"]
}

# Salvează în data.json
with open("data.json", "w") as file:
    json.dump(data, file)

# Citește din data.json
with open("data.json", "r") as file:
    loaded_data = json.load(file)

# Afișează al doilea skill
print(loaded_data["skills"][1])
