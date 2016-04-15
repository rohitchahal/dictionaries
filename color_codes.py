color_codes = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc",
               "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4",
               "aquamarine2": "#76eec6",
               "aquamarine4": "#458b74", "azure1": "#f0ffff"}
for color_name in color_codes:
    print(color_name, ' ', end='')
print()
color_name = input("enter a color name from the above list:")

while color_name != '':
    if color_name in color_codes:
        print("hexadecimal code for color", color_name, "is", color_codes[color_name])
    else:
        print("invalid color name")
    color_name = input("enter a color name:")
