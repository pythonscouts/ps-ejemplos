current_user = "juan"
user_name = current_user and current_user.title()
print(user_name)
current_user = None
user_name = current_user and current_user.title()
print(user_name)
