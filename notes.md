Creating a new stetch
arduino-cli sketch new sensorB_pressure

Compiling a sketch
arduino-cli compile --fqbn esp32:esp32:esp32 esp32_1built_in

Uploading a sketch
arduino-cli upload --port /dev/cu.usbmodem2401 -b arduino:mbed_nano:nano33ble sensorA_temp

For ESP32:
--fbqn esp32:esp32:esp32

-------

See installed libraries:
arduino-cli lib list

Install a library:
arduino-cli lib install <lib-name>
