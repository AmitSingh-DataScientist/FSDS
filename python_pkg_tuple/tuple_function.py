# Importing Logging
import logging
logging.basicConfig(filename="tuple_log.log", level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

# Creating Class Tuple in which I will have all the method to increase the reusability
class tuple_module:
    def __init__(self,t):
        self.t=t

    # To count number of occurrence of an element in the given the tuple
    def tuple_count(self):
        try:
            a = eval(input("Enter an item to count no. of occurrence in the given tuple : "))
            self.t.count(a)
            logging.info("Executed Successfully")
            return self.t.count(a)
        except Exception as e:
            logging.exception("Exception Occurred : " + str(e))

    # To see the position of an element in the given Tuple
    def tuple_index(self):
        try:
            a = eval(input("Enter an element position to see the value in the given tuple : "))
            self.t.index(a)
            logging.info("Executed Successfully")
            return self.t.index(a)
        except Exception as e:
            logging.exception("Exception Occurred " + str(e))
