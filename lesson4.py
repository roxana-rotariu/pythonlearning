class User:
    def __init__(self, name, age, active=True):
        self.name = name
        self.age = age
        self.active = active

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "active": self.active
        }
    
    def __str__(self):
        return f"{self.name} ({self.age} years old)"
        
class UserManager:
    def __init__(self, users):
        self.users = users

    def get_active_usernames(self):
        return [u.name.upper() for u in self.users if u.active]

    def get_sorted_by_age(self, descending=False):
        return sorted(self.users, key=lambda u: u.age, reverse=descending)

    def get_stats(self):
        ages = [u.age for u in self.users]
        return {
            "average_age": sum(ages) / len(ages),
            "min_age": min(ages),
            "max_age": max(ages),
            "active_count": sum(u.active for u in self.users)
        }
    
if __name__ == "__main__":
    users = [
        User("Alice", 30),
        User("Bob", 25, active=False),
        User("Charlie", 35),
        User("Diana", 28)
    ]
    manager = UserManager(users)

    print(manager.get_active_usernames())
    print(manager.get_sorted_by_age())
    print(manager.get_stats())
