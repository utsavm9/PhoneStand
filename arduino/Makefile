arduino: compile upload
esp: esp-compile esp-upload

program = serialInput
espprogram = esp32_ble
port = /dev/cu.usbmodem2301

compile:
	arduino-cli compile -b arduino:mbed_nano:nano33ble  $(program)

upload:
	arduino-cli upload  -b arduino:mbed_nano:nano33ble --port $(port) $(program)


esp-compile:
	arduino-cli compile -b esp32:esp32:esp32  $(espprogram)

esp-upload:
	arduino-cli upload  -b esp32:esp32:esp32 --port $(port) $(espprogram)
