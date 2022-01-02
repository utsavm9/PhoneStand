# PhoneStand
Face-tracking Phone Stand using Arduino, ESP32 and cameras.

We wanted to create a phone stand which rotates to keep the user’s face at the center of the screen.

![](https://raw.githubusercontent.com/utsavm9/PhoneStand/main/images/stand.png)
![](https://raw.githubusercontent.com/utsavm9/PhoneStand/main/images/group.jpg)

# Hardware
* [Arduino Nano 33 BLE Sense](https://store-usa.arduino.cc/products/arduino-nano-33-ble-sense-with-headers)
* [ESP32-DEVKITC-32D](https://www.digikey.com/en/products/detail/ESP32-DEVKITC-32D/1965-1000-ND/9356990?itemSeq=375828193)
* [ESP32-CAM WiFi](https://www.amazon.com/dp/B07T2RYTJF)
* [Stepper Motor](https://www.amazon.com/dp/B0787BQ4WH)
* [Stepper Motor Driver](https://www.amazon.com/dp/B07BND65C8/)

We found that [OmniVision OV7670](https://www.amazon.com/dp/B07S66Y3ZQ) camera module had too low frame rate when used with Arduino Nano.

# Files
Files relevant in the final demo
* `arduino/`
    * `serialInput`: Receive turn command from Serial and turn the motor accordingly
    * `Makefile`: Arduino CLI Commands for flashing sketches
* `esp32/`
    * `BasicWebServer`: Sketch for ESP32 CAM to connect to my home WiFi and stream the camera input
* `python/`
    * `face-detection.ipynb`: Notebook to debug face detection pipeline
    * `process.py`: Takes input stream from my ESP32CAM URL, and outputs to my Serial whether to turn left or right for the phone stand


Other files:
* `arduino/`:
    * `drawimage`: A [Processing](https://processing.org/) sketch for displaying OmniVision camera input coming from Serial via `rawbytes` sketch
    * `omnivision`: Print the raw input from the camera as hex for debugging
    * `originalMotor`: Sketch to turn the motor through a driver
    * `rawbytes`: Print raw bytes to my serial port for Processing to take and show the image.