import os

def run_tests():

    print("Now Running Signup Tests")
    os.system("behave features/signup.feature")


    print("Running Login Tests After signup test")
    os.system("behave features/login.feature")

if __name__ == "__main__":
    run_tests()
