from typing import List, Dict

def get_sorted_users_by_age(users: list[dict], descending: bool = False) -> list[dict]:
    return sorted(users, key=lambda u: u["age"], reverse=descending)

def get_active_usernames(users: list[dict]) -> list[str]:
    return [u["name"].upper() for u in users if u["active"]]

def get_stats(users: List[dict]) -> dict:
    ages = [u["age"] for u in users]
    return {
        "average_age": sum(ages) / len(ages),
        "min_age": min(ages),
        "max_age": max(ages),
        "active_count": sum(u["active"] for u in users)
    }

if __name__ == "__main__":
    users = [
        {"name": "roxana", "age": 30, "active": True},
        {"name": "alex", "age": 25, "active": False},
        {"name": "maria", "age": 35, "active": True},
        {"name": "john", "age": 20, "active": True},
    ]

    print(get_sorted_users_by_age(users))
    print(get_sorted_users_by_age(users, descending=True))
    print(get_active_usernames(users))
    print(get_stats(users))

    for i, user in enumerate(users, start=1):
        print(f"{i}. {user['name']}")