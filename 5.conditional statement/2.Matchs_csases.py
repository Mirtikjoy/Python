country_name = input("Please enter your country name: ")
# if country_name == "United states Of America":
#     print("USA  ")
# elif country_name == "United Kingdom":
#     print("UK  ")
# elif country_name == "United Arab Emirates":
#     print("UAE  ")
# elif country_name == "Canada":
#     print("CN")
# elif country_name == "India":
#     print("IN")
# else:
#     print("country name not found")


match country_name:
    case "United states Of America":
        print("USA")
    case "United Kingdom":
        print("UK")
    case "United Arab Emirates":
        print("UAE")
    case "Canada":
        print("CN")
    case "India":
        print("IN")
    case _:
        print("country name not found")