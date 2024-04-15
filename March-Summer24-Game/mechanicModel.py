def mechanic_model(mov_current, mov_ideal):
    if mov_current == mov_ideal:
        return "No problem, do nothing"
    elif mov_ideal == "y":
        return "Apply lubricant"
    else:
        return "Apply tape"


print(mechanic_model("n", "n"))