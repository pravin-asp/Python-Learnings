import webbrowser, sys

place = sys.argv[1]
print("https://www.google.com/maps/place/" + place)
webbrowser.open("https://www.google.com/maps/place/" + place)
