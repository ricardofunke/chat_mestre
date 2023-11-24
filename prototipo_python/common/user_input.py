def exploration_options():
    option = input("Type the option number (or any key to exit): ")
    match option:
        case '1' | '2' | '3' | '4':
            return option
        case _:
            return None


def battle_options():
    print("Option 1: Fight")
    print("Option 2: Flee")
    option = input("Type the option number (or any key to exit): ")
    match option:
        case '1':
            return 'fight'
        case '2':
            return 'flee'
        case _:
            return None
