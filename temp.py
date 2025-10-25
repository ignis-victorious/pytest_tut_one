"""Capture log output."""
import Logging
logging. basicConfig(level=logging.DEBUG)
def function_which_logs(x: int, y: int) → float:
'"Divide x by y!'"" try:
result = x / y
except ZeroDivisionError:
logging error ("Zero division detected!")
return 0
else:
logging. info ("Returning &s divided by %",x, y)
return result
# print(function which_logs (120, 6))
# print(function_which_logs (120, 0))