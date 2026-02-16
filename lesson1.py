from typing import List, Dict

def get_active_usernames(users: List[Dict[str, object]]) -> List[str]:
    return [user['name'].capitalize() for user in users if user.get('active')]

if(__name__ == "__main__"):
    users = [
        {'name': 'alice', 'active': True},
        {'name': 'bob', 'active': False},
        {'name': 'charlie', 'active': True}
        ]
    result = get_active_usernames(users)
    print(result)