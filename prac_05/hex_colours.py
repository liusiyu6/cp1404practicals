COLOR_CODES = {"Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2", "Beige": "#f5f5dc", "Bittersweet": "#fe6f5e",
               "Aquamarine1": "#7fffd4", "Azure1": "#f0ffff", "Brick Red": "#cb4154", "Canary": "#ffff99",
               "Chartreuse1": "#7fff00", "DarkOrchid": "#9932cc"}

print("Available colors:", ", ".join(COLOR_CODES.keys()))

# Main program loop
color_name = input("\nEnter color name: ").strip()
while color_name != "":
    # Case-insensitive search
    found = False
    for name, code in COLOR_CODES.items():
        if name.lower() == color_name.lower():
            print(f"{name}: {code}")
            found = True
            break

    if not found:
        print("Invalid color name")

    color_name = input("\nEnter color name: ").strip()
