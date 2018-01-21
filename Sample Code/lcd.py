#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import sys
import datetime
import Adafruit_CharLCD as LCD

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

LockStat = 1

DoorStat = 2

time.sleep(0.005)

while True:
  lcd.message("Time\n" + datetime.datetime.now().strftime("%I:%M%p"))

  time.sleep(5.0)

  lcd.clear()

  lcd.message("Date\n" + datetime.date.today().strftime("%b %d, %Y"))

  time.sleep(5.0)

  while True:
    lcd.clear()
    lcd.message("Input your PIN\n")
    lcd.blink(True)

    PIN = raw_input()
  
    try:
      int(PIN)
    except ValueError:
      lcd.message("Not a number!")
      time.sleep(2)
      continue

    else:
      if(str(PIN) == "12345"):
        lcd.clear()
        lcd.blink(False)
        lcd.message("Access Granted\n*****")   
        break
      if(str(PIN)=="0"):
	lcd.clear()
	lcd.blink(False)
	lcd.message("Goodbye")
	time.sleep(2)
	lcd.clear()
	sys.exit(0)
      else:
        lcd.message("Incorrect PIN")
        time.sleep(2)
	continue

  time.sleep(3.0)

  lcd.clear()
  lcd.message("Welcome:\nStanley")

  time.sleep(2.0)

  lcd.clear()

  if(LockStat == 1):
    lcd.message("Lock: Unlocked")
  elif(LockStat == 0 ):
    lcd.message("Lock: Locked")

  time.sleep(2.0)
  lcd.clear()

  if(DoorStat == 0):
    lcd.message("Door: Closed")

  elif(DoorStat == 1):
    lcd.message("Door: Opening")
  
  elif(DoorStat == 2):
    lcd.message("Door: Open")

  time.sleep(2.0)

  lcd.clear()  
