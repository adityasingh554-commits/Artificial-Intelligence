rooms={
    "A":"Dirty",
    "B":"Dirty"
}


location = "A"


while True:
    print("\n Location: ",location)
    print("Room A: ",rooms["A"])
    print("Room B: ",rooms["B"])


    if rooms[location] == "Dirty":
        print("Action: Suck")
        rooms[location] = "Clean"

    else:
        if location == "A":
            print("Action: Move Right")
            location = "B"

        else:
            print("Action: Move Left")
            location = "A"

        if rooms["A"] == "Clean" and rooms["B"] == "Clean":
            print("Both rooms are clean")
            print("Vaccum compelete")
            break