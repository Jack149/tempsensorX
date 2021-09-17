temp = 0

def on_forever():
    global temp
    temp = input.temperature()
    basic.show_number(temp)
basic.forever(on_forever)
