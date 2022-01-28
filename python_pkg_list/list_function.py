# Importing Logging
import logging
logging.basicConfig(filename="list_log.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s ')

# Creating Class list in which i will have all the method to increase the reusability

class list_module:

    def __init__ (self,l):
        self.l = l
    # To return length of a list
    def list_len(self):
        try:
            logging.info("Executed successfully")
            return len(self.l)
        except Exception as e:
            logging.exception("Exception Occurred: " + str(e))

    # To append list at the end of the current list
    def list_append(self):
        try:
            self.l.append(eval(input("Enter a list value: ")))
            logging.info("Executed successfully")
            return self.l
        except Exception as e:
            logging.exception("Exception Occurred: " + str(e))

    # To remove item from list; by default remove last item
    def list_pop(self):
        try:
            logging.info("Executed successfully")
            return self.l.pop()
        except Exception as e:
            logging.exception("Exception Occurred: " + str(e))

    # To insert list at the specific position in the current list
    def list_insert(self):
        try:
            p = eval(input("Please enter a position to insert value in list : "))
            v = eval(input("Please enter a value or list to insert in list : "))
            self.l.insert(self.l[p],v)
            logging.info("Executed successfully")
            return self.l
        except Exception as e:
            logging.exception("Exception Occurred: " + str(e))

    # To reverse the list
    def list_reverse(self):
        try:
            logging.info("Executed successfully")
            return self.l[::-1]
        except Exception as e:
            logging.exception("Exception Occurred: " + str(e))

    # To count number of occurrence of an element in the given the list
    def list_count(self):
        try:
            a=eval(input("Enter an item to count no. of occurrence in the given list : "))
            self.l.count(a)
            logging.info("Executed successfully")
            return self.l.count(a)
        except Exception as e:
            logging.exception("Exception Occurred: " + str(e))

    # To extend list to the current list in iterable form
    def list_extend(self):
        try:
            self.l.extend(eval(input("Enter a list value : ")))
            logging.info("Executed successfully")
            return self.l
        except Exception as e:
            logging.exception("Exception Occurred: " + str(e))
