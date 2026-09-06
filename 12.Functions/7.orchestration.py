def write_log(message):
    with open(r"c:/Users/Mirtik Joy Molsom/OneDrive/Desktop/Python/12.Functions/email.log", "a") as file:
        file.write(message + "\n")

def is_emal_valid(mail):
    valid = "@" in mail and "." in mail
    return valid

def clean_email(mail):
    clean_up = mail.strip()
    username,domain = clean_up.split("@")
    return {"username" :username,"domain":domain}


write_log("app started")
mail = input("please enter your email address: ")

def process_user_email(mail):
    if not is_emal_valid(mail):
        write_log("Invalid email ")
    else:
        Clean = clean_email(mail)
        write_log(f"process email {Clean}")
    write_log("app stopped")

process_user_email(mail)
