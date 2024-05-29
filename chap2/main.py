name = "ada lovelace"
print(name.title())
print(name)
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())

print(f"Hello {full_name.upper()} !")

print("   what do you know   ".lstrip())
print("   what do you know   ".rstrip())

print("https://www.duckduckgo.com/".removeprefix("https://").removesuffix("/"))