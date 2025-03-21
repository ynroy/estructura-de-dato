def greet(name):
    """Greets the user with a personalized message.

    Args:
        name: The name of the user to greet.

    Returns:
        A string containing the greeting message.
    """

    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, world!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)