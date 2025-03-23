#include <LiquidCrystal.h>
// RS, EN, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
const int buttonPin = 7;  // Button connected to pin 7
int buttonState = 0;  
void setup() {
 lcd.begin(16, 2);
 lcd.print("Press Button");
 pinMode(buttonPin, INPUT_PULLUP);  // Use internal pull-up resistor
}
void loop() {
 buttonState = digitalRead(buttonPin);  // Read button state
 if (buttonState == LOW) {  // Button is pressed (LOW due to pull-up)
   lcd.clear();
   lcd.print("Button Pressed!");
   delay(500);  // Simple debounce
 } else {
   lcd.clear();
   lcd.print("Press Button");
 }
 delay(100);  // Prevent rapid LCD updates
}