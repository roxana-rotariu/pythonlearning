from client import JsonPlaceholderClient

client = JsonPlaceholderClient()

# GET post cu id=1
post = client.get_post(1)
print("GET post 1:", post)

# POST nou
new_post = client.create_post({
    "title": "Hello",
    "body": "This is Roxana",
    "userId": 1
})
print("Created post:", new_post)
