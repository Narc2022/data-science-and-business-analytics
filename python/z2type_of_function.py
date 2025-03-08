def greet(name):
    print(f"Hi {name}")


# 1- Perform a task
# 2- Return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Sachin")
file = open("content.txt", "w")
file.write(message)
