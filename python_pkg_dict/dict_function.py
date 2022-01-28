# Importing Logging
import logging
logging.basicConfig(filename="dict_log.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Creating Class Dictionary in which I will have all the method to increase the reusability
class dict_module:
    def __init__ (self,d):
        self.d = d

    # To show keys of a Dictionary
    def dict_key(self):
        try:
            self.d.keys()
            logging.info("Executed Successfully")
            return self.d.keys()
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))

    # To show values of a Dictionary
    def dict_value(self):
        try:
            self.d.values()
            logging.info("Executed Successfully")
            return self.d.values()
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))

    # To return the value of a key from Dictionary
    def dict_get(self):
        try:
            a=eval(input("Enter a key to see the respective value from Dict : "))
            self.d.get(a)
            logging.info("Executed Successfully")
            return self.d.get(a)
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))

    # To delete a particular key from Dictionary, even it will delete the dict
    def dict_delete(self):
        try:
            a=eval(input("Enter a key to delete from Dict : "))
            del self.d[a]
            logging.info("Executed Successfully")
            return self.d
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))

# To update an element to of dict to base dict
    def dict_update(self,a):
        try:
            self.d.update(a)
            logging.info("Executed Successfully")
            return self.d
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))
