while True:
    user = input("you: ")

    if user.lower() in ["bye", "exit", "quit"]:
        print("bot: goodbye")
        break

    elif user.lower() == "hi":
        print("bot: hello")

    elif user.lower() == "how are you":
        print("bot: fine, what about you")

    elif user.lower() == "i am depressed":
        print("bot: what's happened?")

    else:
        print("bot:goodbye")