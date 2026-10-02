from abc import ABC

class Appliance(ABC):
    def turn_on ():
        pass




class Robot(ABC):
    def movement ():
        pass



class WashingMachine(Appliance):
    def turn_on():
        control = input("Push the button: ")
        if control == "ON":
            return "Turning on Washing Machine"
        elif control == "OFF":
            return "Turning off Washing Machine"
        else:
            return "Wrong input"
        


class DeliveryRobot(Robot):
    def movement():
        control = input("Push the button: ")
        if control == "Right":
            return "Delivery Robot moving to Right"
        elif control == "Left":
            return "Delivery Robot moving to Left"
        else:
            return "Wrong input"



           
w = WashingMachine()
print(WashingMachine.turn_on())


d2 = DeliveryRobot()
print(DeliveryRobot.movement())


