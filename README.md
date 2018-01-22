# LCD (Liquid Crystal Display) and Numeric Keypad

## TABLE OF CONTENTS
1. [INTRODUCTION](#introduction)
2. [COST OF MATERIALS](#cost-of-materials)
3. [TIME NEEDED](#time-needed)
4. [ASSEMBLY](#assembly)
5. [POWER UP](#power-up)
6. [FURTHER TESTING](#further-testing)

### INTRODUCTION
The LCD/Numeric Keypad is a little handy device you can make in a short period of time, and has tons of applications. If used hand in hand with other devices, it’s possible to have the other devices relay information to the LCD. At the same time, the numeric keypad can act as a user’s input device so they could, in theory, manipulate the status of their other devices.
	To help visualize this, one possible application of this project is the Locker Automation System which my team intends to produce for next semester’s project. The system will need a way for users to check the status of their devices via the LCD and unlock the smart lock and door via the numeric keypad. This is just one example of many other applications you can use this project on.

### COST OF MATERIALS
Listed below are the components you will need and some suggested links to online stores you may order them from.  Note that availability of these components and prices are as of January, 2018 and may be subject to change. All prices are in Canadian Dollar (CAD).  


Raspberry Pi Kit 
- CAD 79.95 [link to item here](https://www.buyapi.ca/product/raspberry-pi-3-b-starter-kit/) 
- Includes Raspberry Pi 3 B, Case, Power Supply, Ethernet Cable

Breadboard
- CAD 5.99 [link to item here](https://www.amazon.ca/OSEPP-Breadboard-400-Points-Components-LS-00018/dp/B00EFZV2CG/)

HD44780 LCD 
- CAD 6.76 [link to item here](https://www.amazon.ca/HD44780-Module-White-Characters-Backlight/dp/B008XS133E/)

USB Numeric Keypad
- CAD 14.99 [link to item here](https://www.amazon.ca/DLAND-Ergonomic-Numerical-external-Keyboard/dp/B017VH9BE0/)

Male-to-female jumper cable set
- CAD 2.95 [link to item here](https://www.buyapi.ca/product/diy-jumper-wires-for-raspberry-pi-30cm/)

Male-to-male jumper cable set
- CAD 2.95 [link to item here](https://www.buyapi.ca/product/multicolored-40-pin-dupont-breadboard-jumper-wires-male-to-male-20cm/)

Optional: 10k potentiometer CAD 11.99 (https://www.amazon.ca/gp/product/B0713QQXX8/)

Note: 
- Prices do not include shipping.

- Instead of buying an LCD via Amazon, another option would be to procure your own LCD from an old device that has it. In my case, I looked through A1 Electronics (see resources for physical address) for spare LCDs from old inverters and the like. It cost around CAD5.00.

### TIME NEEDED

Ordering your components: (5-7 days)

-	Ordering from the vendors listed above took around probably close to a week to complete. 
Preparing your devices (1-2 days)
-	Setting up the Raspberry Pi is quick, probably around half a day, even quicker if you just flash the image I will be uploading to my repository. 

-	If you use a brand new LCD instead of one from an old device (which is most likely soldered on to another board), it should take no less than 15 minutes to figure out the wiring (I will be providing diagrams of the wiring later). Otherwise, you will need to test which pin is which as the boards may possibly have different wiring. Researching your specific LCD might take longer than a day.

-	Optional: Designing a PCB will probably help when you’re moving on to production as it removes the need for the breadboard and the jumper wires. The standard HD44780 fits in most Raspberry Pi cases so making a hole in the case that comes with the Buyapi.ca kit might be enough. 

Writing code
-	Depending on the kind of functionality you intend to apply to your LCD and Numeric keypad, and as such time allotted can take longer. 

### Assembly (LCD):
#### Hardware Side: 

In assembling your LCD and numeric keypad, PiMyLifeUp.com has a fritzing diagram you can refer to. This is their recommended pinouts. Additionally if you do not have a 10k potentiometer or choose not to buy them you may opt to wire pin 3 (V0) directly to ground for maximum contrast.

![Fritzing Diagram](https://raw.githubusercontent.com/StanGo25/Display/master/Media/figure1.png)

One other thing to note is that in selecting your LCD be absolutely certain that it’s a HD44780, as other LCDs are designed around Arduino signals and thus will not display anything even if you connect the pins right.

If you chose to get an LCD from A1 Electronics and it looks like this, it is recommended that you follow /u/devicemodder in his reddit post for the pinouts of this specific board. Fritzing diagram is being made to account for this and will be up on the project repository soon. 

![A1 LCD](https://raw.githubusercontent.com/StanGo25/Display/master/Media/figure2.png)

![Thread](https://raw.githubusercontent.com/StanGo25/Display/master/Media/figure3.png)

- Note that /u/devicemodder has also included pinouts for the speaker, LED and buttons on the board as well.

#### Software Side

-	To start off, confirm that your Raspberry Pi OS has been installed by powering it up, plug it in to a monitor and a keyboard to navigate the command line

-	Afterwards, check to see if Python 2.7 above is installed (using the command python –version)

-	If it isn’t, open up the command line and input the following command:

 sudo apt-get update
 
 sudo apt-get install python

-	Then, you will want to install Adafruit’s libraries to make it easier.

- Input the following command: 

	git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git

-	After that, navigate to the directory you cloned (using cd ./Adafruit_Python_CharLCD.git), then install using sudo python setup.py install

-	From there, you can get started on writing code for your LCD.

- In the directory, there are a few sample scripts you can try out for yourself, do remember to change the defined GPIOs and change them to the ones you wired. If you followed the diagram earlier, it should look like this:

lcd_rs            = 25 
lcd_en            = 24
lcd_d4            = 23
lcd_d5            = 17
lcd_d6            = 18
lcd_d7            = 22
lcd_backlight     = 4
lcd_columns       = 16
lcd_rows          = 2


#### Assembly (Numeric Keyboard)
-	First, take the numeric keypad out of the box.
-	Then plug it into one of the USB ports
-	If you plug it in the wrong way, flip it over and plug it in again.
- If that still doesn't work, flip it over again. 
-	Test all the keys to confirm that it’s working as intended.

#### Sample Code:
Try out this code to get started. It displays the date and time and prompts the user to input digits into the numeric keypad:

Can be found in the repository [here](https://github.com/StanGo25/Display/blob/master/Sample%20Code/lcd.py)

### POWER UP
If you managed to connect the LCD and the Numeric Keypad to the Pi without a problem, your device should now look something like this:
![Powered Up](https://raw.githubusercontent.com/StanGo25/Display/master/Media/figure4.png)
![Powered Up2](https://raw.githubusercontent.com/StanGo25/Display/master/Media/figure5.png)


### FURTHER TESTING
Moving forward, I plan on designing a PCB for the LCD to lessen the number of wires going around at the moment. Afterwards, a case to fit within the constraints of where the device is to be actually installed (a Locker in this case). Also research must be looked into for a proper portable power adapter for if there’s a power outage.
