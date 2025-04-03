def greet(name):
    return f"Hello, {name}! Welcome to Git testing."
def test_1(x):
    return x*x
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    x=input()
    print(greet(user_name))
    print(test_1(x))
