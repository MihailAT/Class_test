import class_Car
import sys
import os

#print("path  initially =\n", sys.path)
                #sys.path.append("..")
sys.path.append(os.path.abspath("c:/Users/User/PYTHON_utils"))      #perhaps __init__.py still not invlved???????
sys.path.append(os.path.abspath("c:/Users/User/MISHA_PYTHON"))
import ML_utils
import test_include
                    #import Utilities_ML-----------------------the main issue is the recognition of the old file..... not py file but .pynb file???
crv= class_Car.Car(1, "Toyota", 2020)
crv.start_engine()
ML_utils.test_utilities("april 24")
test_include.test_print("2023")
tesla=class_Car.Electric_Car(105, 4, "Tesla", 2023)
hyundai=class_Car.Electric_Car(95, 2, "Hyundai", 2023)
tesla.start_engine()
hyundai.start_engine()
crv.details()
tesla.details()
print(crv)
elon_car=class_Car.Super_Car(123, 5, "Elon", 2027)
#besos_car=class_Car.Super_Car()

elon_car.train(24)
elon_car.charge()
#print(class_Car.Car.__dict__)
#print(class_Car.Car.__doc__)