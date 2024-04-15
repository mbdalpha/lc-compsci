
def tennis_model(outlook, humidity, wind):
    if outlook == "sunny":
        if humidity == "high" :
            return False
        else:
            return True

    elif outlook == "rain":
        if wind == "strong":
            return False
        else:
            return True

    else:
        return True


print(tennis_model("overcast", "high" , "weak"))
print(tennis_model("sunny", "high" , "weak"))