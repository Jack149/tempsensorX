def CtoF(num: number, num2: number):
    global F_Temp
    F_Temp = temp * 2
    F_Temp += 30
    return F_Temp

def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

temp = 0
F_Temp = 0
radio.set_group(1)
radio.set_transmit_power(7)

def on_forever():
    global temp
    temp = input.temperature()
    CtoF(1, 1)
    radio.send_number(F_Temp)
    basic.show_number(F_Temp)
basic.forever(on_forever)
