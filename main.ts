function CtoF (num: number, num2: number) {
    F_Temp = temp * 2
    F_Temp += 30
    return F_Temp
}
radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
let temp = 0
let F_Temp = 0
radio.setGroup(1)
basic.forever(function () {
    temp = input.temperature()
    CtoF(1, 1)
    radio.sendNumber(F_Temp)
    basic.showNumber(F_Temp)
})
