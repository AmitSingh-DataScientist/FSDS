# Importing Logging
import logging
logging.basicConfig(filename="set_log.log", level=logging.DEBUG, format ='%(asctime)s %(levelname)s %(message)s')

# Creating Class Set in which I will have all the method to increase the reusability
class set_module:
    def __init__ (self,s):
        self.s = s

    # Add an element to Set
    def set_add(self):
        try:
            a=eval(input("Please enter a value to add in Set : "))
            self.s.add(a)
            logging.info("Executed Successfully")
            return self.s
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))

    # Remove an element from Set, if not in set then it through an error
    def set_remove(self):
        try:
            a = eval(input("Please enter a value to remove from Set : "))
            self.s.remove(a)
            logging.info("Executed Successfully")
            return self.s
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))

    # Remove an element from Set, if not in set then it will do nothing
    def set_discard(self):
        try:
            a=eval(input("Please enter a value to discard from Set : "))
            self.s.discard(a)
            logging.info("Executed Successfully")
            return self.s
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))
