#equivalent to switch statement in java
value = 20
match value:
    case 10:
        print("Value is 10")
    case 20:
        print("You are correct! Value is 20")
    case 30|40:
        print("Value is 30 or 40")
    case _:
        print("Value is something else")