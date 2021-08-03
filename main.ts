input.onButtonPressed(Button.A, function () {
    fan_switch = 1
})
input.onButtonPressed(Button.B, function () {
    fan_switch = 0
})
let fan_switch = 0
for (let index = 0; index < 1; index++) {
    soundExpression.hello.playUntilDone()
}
let angle = 0
fan_switch = 0
let servo_direction = 0
startbit.startbit_Init()
basic.forever(function () {
    if (fan_switch) {
        startbit.startbit_setFanSpeed(startbit.startbit_fanPort.port2, 100)
        if (servo_direction == 0) {
            angle = angle + 2
            if (angle >= 270) {
                servo_direction = 1
            }
        } else {
            angle = angle - 2
            if (angle <= 0) {
                servo_direction = 0
            }
        }
        startbit.setServo(startbit.startbit_servorange.range2, 1, angle, 20)
    } else {
        startbit.startbit_setFanSpeed(startbit.startbit_fanPort.port2, 0)
    }
})
