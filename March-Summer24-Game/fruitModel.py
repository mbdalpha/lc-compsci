def fruit_model(colour, size, shape, taste):
    if colour == "green":
        if size == "big":
            return "Watermelon"
        else:
            if size == "medium":
                return "Apple"
            else:
                return "Grape"

    else:
        if colour == "yellow":
            if shape == "round":
                if size == "big":
                    return "Grapefruit"
                else:
                    return "Lemon"
            else:
                return "Banana"

        else:
            if size == "small":
                if taste == "sweet":
                    return "Cherry"
                else:
                    return "Grape"
            else:
                return "Apple"

print(fruit_model("red", "medium", "round", "sour"))