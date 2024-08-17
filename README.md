# Life Size Fuecoco Robot
This is a fully 3d printed robotic Fuecoco Pokemon. It can be controlled over wifi using a custom bulit contoller or a website

This was a college project for Immersive Software Engineering CS4445 and for a cosplay for Dubin Comic Con 2024.

The full project can be found on the college branch, it will include extra things like the website, interfacing with aws and a full report.

This branch has everything needed to 3d print and assemble the robot and control it using the custom controller.

## 3D Printing & laser cutting
This was printed using an Ender3 v2.
The model has been split up to fit in the 220mm * 220mm * 250mm build volume of the Ender3 v2
The orginal fuecoco model was found [here](#)

All the STL files can be found [here](#)

The top of the conrollet was laser cut from 3mm clear acrylic so the LEDs could shine through
This could be 3d printed if a laser cutter is not accessible

note the head has weird slots on the back, ingnore them and glue magnets instead

## Assembly

- 3d print all the parts
- do a lot of sanding and filling
- glue the parts together
- do more sanding and filling
- spray paint
- do more sanding and filling
- do the final coat of spray paint 
- assemble the electronics (see wiring diagram and code setup)
- put the electronics in the pokemon
- glue in the electornics
- glue on the magnets

## Wiring Diagram
tbd
solder pico headers up


## Code Setup
I used MicroPython on the Raspberry Pi Pico W
The code for the pokemon can be found [here](#)
Copy it over from the computer to the Raspberry Pi Pico W
Change the wifi ssid and password in the code
Run the code
The controller and fuecoco need to be on the same wifi network
fuecoco runs an api and the the controller sends requests to the api. When the fuecoco receives a request it moves the motors accordingly
