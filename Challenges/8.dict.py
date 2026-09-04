user = {
    "id":1,
    "names" : "mirtik joy molsom", 
    "age" : 21, 
    "city" : "bangaluru"
    }


new_User = {
    key.capitalize() : Value.capitalize()
    for key, Value in user.items()
    if isinstance(Value,str)
}

print(new_User)

