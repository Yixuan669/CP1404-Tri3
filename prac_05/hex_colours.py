COLOR_TO_CODE = { "aliceblue": "#f0f8ff","antiquewhite": "#faebd7", "aqua": "#00ffff", "beige": "#f5f5dc", "coral": "#ff7f50",
                  "darkgreen": "#006400", "gold": "#ffd700", "hotpink": "#ff69b4", "lavender": "#e6e6fa", "navy": "#000080" }

print(COLOR_TO_CODE)
color_name = input("Enter name: ").lower()
while color_name != "":
    try:
        color_code = COLOR_TO_CODE[color_name]
        print(f'{color_name} is {color_code}')
    except KeyError:
        print("Invalid short state")
    color_name = input("Enter name: ").lower()
