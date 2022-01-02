const int dirPin = 16;
const int stepPin = 1;
const int stepsPerRevolution = 200;

int incomingByte = 0;  // for incoming serial data

void setup() {
	while (!Serial)
		;
	Serial.begin(9600);  // opens serial port, sets data rate to 9600 bps
	Serial.println("Begun");

	// Declare pins as Outputs
	pinMode(stepPin, OUTPUT);
	pinMode(dirPin, OUTPUT);
}

void loop() {
	digitalWrite(dirPin, HIGH);

	if (Serial.available() > 0) {
		// read the incoming byte:
		incomingByte = Serial.read();

		// say what you got:
		Serial.print("I received: ");
		switch (incomingByte) {
		case 'L':
			Serial.println("LEFT");
			// Set motor direction counter-clockwise
			digitalWrite(dirPin, HIGH);
			digitalWrite(stepPin, HIGH);
			delayMicroseconds(10);
			digitalWrite(stepPin, LOW);

			break;

		case 'R':
			Serial.println("RIGHT");
			// Set motor direction clockwise
			digitalWrite(dirPin, HIGH);
			digitalWrite(stepPin, HIGH);
			delayMicroseconds(10);
			digitalWrite(stepPin, LOW);

			break;

		case 'N':
			Serial.println("NOTHING");
			break;

		default:
			Serial.println("ERROR");
			break;
		}
	}
}
