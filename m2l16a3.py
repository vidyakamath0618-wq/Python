country_code = {"India":"0091",
                "australia":"0025",
                "nepal":"00977"}
#search dictionary for country code of India
print("country code for India -")
print(country_code.get("india", "not found"))
#search dictionary for country code of japan
print("country code for Japan -")
print(country_code.get("japan", "not found"))