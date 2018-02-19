
def shutdown(s):
    if s == "yes":
        return print("shutting down")
    elif s == "no":
        return print("Shutdown aborted")
    else:
        return print("sorry")




s= "no"
shutdown(s)
