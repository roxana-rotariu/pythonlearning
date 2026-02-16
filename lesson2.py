from typing import List, Dict

def process_users(users: List[Dict[str, object]], *, uppercase=False, only_active=False) -> List[str]:
    return [
        user["username"].upper() if uppercase else user["username"]
        for user in users
        if not only_active or user["active"]
    ]

if(__name__ == "__main__"):
    users = [
        {"username": "samuel", "active": True},
        {"username": "caro", "active": False},
        {"username": "susan", "active": True},
    ]
    print(process_users(users, uppercase=True))
    print(process_users(users, only_active=True))
    print(process_users(users, uppercase=True, only_active=True))