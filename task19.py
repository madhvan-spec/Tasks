def register_user(username, age):
    if not isinstance(username, str):
        raise ValueError("Username must be a string.")

    if len(username.strip()) == 0:
        raise ValueError("Username cannot be empty.")

    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")

    if age <= 0:
        raise ValueError("Age must be a positive number.")

    return f"User '{username}' registered, age {age}."


try:
    print(register_user("Madhvan", 21))
    # print(register_user("", 20)) 
    print(register_user("Madhvan",""))
except ValueError as e:
    print("Input Error:", e)
