def clean_email(email):
    cleamup_mail = email.strip().lower()
    username, domain = cleamup_mail.split("@")
    return {"username" :username ,
            "domain": domain}

print(clean_email("mmieritk@gmail.com"))