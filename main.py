def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_uart_data_received():
    basic.show_string("got")
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

def on_button_pressed_b():
    bluetooth.start_accelerometer_service()
    bluetooth.start_button_service()
    bluetooth.start_io_pin_service()
    bluetooth.start_led_service()
    bluetooth.start_temperature_service()
    bluetooth.start_magnetometer_service()
input.on_button_pressed(Button.B, on_button_pressed_b)

for index in range(1):
    soundExpression.giggle.play_until_done()