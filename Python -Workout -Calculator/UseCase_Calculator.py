
import re;
from functools import reduce;

print("============ Calculator Program ============== ")

# The function to chose the calculator options , Dictionary data type used in function
def CalOpt(i):
    Opt = {
        1: 'Add',
        2: 'Subtract',
        3: 'multiply'

    }
    return Opt.get(i, "Invalid input")


# The function to call the CalOpt function and validate the user option  call the CalOpt
# if the user input option is not valid then will call the CalOpt function again to get details .
def options():
    print("Please enter any option below \n Enter 1 for Addition \n Enter 2 for subtraction \n Enter 3 for multiply \n")
    options = input("Enter your option :")
    UserInput = CalOpt(int(options))
    if UserInput == "Invalid input":
        print('Please enter valid option')
        options = input("Enter your option :")
        UserInput = CalOpt(options)
        ip = input("Enter numeric list for calculation :")
    else:
        ip = input("Enter numeric list for calculation :")
        # UserInput = CalOpt(int(options))
    return UserInput, ip


# The class to validate the user input
# if the user input is not valid (contain non-numeric value except (comma)), will break the flow .
class InputValidator:

    def __init__(self, inputs, opts):
        self.inputs = inputs
        self.options = opts

    def Is_input_Valid(self):
        numberstring = self.inputs
        IS_Valid = "valid"
        IS_NotValid = "notvalid"
        regex = r"[a-zA-z\s/#$%^*&():;'.@!`~]{1,}"
        if bool(re.search(regex, numberstring)):
            return numberstring, IS_NotValid

        else:
            print("The Entered details are {} ,So the input need to be converted to list {} for Iteration".format(IS_Valid, numberstring))
            iteratorip =re.split(",", numberstring)
            for no in range(0, len(iteratorip)):
                if iteratorip[no].isnumeric():
                    iteratorip[no] = int(iteratorip[no])
                else:
                    print("The entered details {} are Not valid,Calculator only accept numeric value ".format(numberstring))
                    return numberstring, IS_NotValid
                    break

            print("The Entered details are converted as a list {} for Iteration".format(iteratorip))
            return iteratorip, IS_Valid


try:

    opt, inputnumber = options()
    IpValObj = InputValidator(inputnumber, opt)
    input, IS_validflg = IpValObj.Is_input_Valid()

    if IS_validflg == "valid":
        reduce_numbers = input

        if opt == "Add":
            result = reduce((lambda x, y: x + y), reduce_numbers)
            print("{} - Result {}".format(opt, result))
        elif opt == "Subtract":
            result = reduce((lambda x, y: x - y), reduce_numbers)
            print("{} - Result {}".format(opt, result))
        elif opt == "multiply":
            result = reduce((lambda x, y: x * y), reduce_numbers)
            print("{} - Result {}".format(opt, result))

    else:
        print("The inputs are not valid,Please separate the number with only comma(,) and enter only numeric value")

except Exception as ex:
    print("error details {}".format(ex))

