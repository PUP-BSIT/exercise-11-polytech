from colorcycle import hex_to_rgb

def hex_to_rgb_colors():
    print("[HEX to RGB Converter]")
    hex_colors = []

    count = int(input("How many HEX colors would you like to convert? "))

    for i in range(count):
        user_input = input(f"Enter HEX color #{i + 1} (e.g., #ff5733): ")
        hex_colors.append(user_input)

    for hex_color in hex_colors:
        rgb = hex_to_rgb(hex_color)
        if rgb:
            print(f"HEX: {hex_color} -> RGB: {rgb}")
        else:
            print(f"Invalid HEX color: {hex_color}")

