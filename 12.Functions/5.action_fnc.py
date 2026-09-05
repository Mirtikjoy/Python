
def write_log(message):
    with open(r"c:/Users/Mirtik Joy Molsom/OneDrive/Desktop/Python/12.Functions/app.log", "a") as file:
        file.write(message + "\n")


write_log("App Started")
write_log("user login")