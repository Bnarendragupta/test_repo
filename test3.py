import sys

# Define your variables
a = 1
b = 2
c = 2
d = 2
# Check conditions
if a == b and c == d:
    # If both conditions are true, exit with status 0 (success)
    sys.exit(0)
else:
    # If either condition is false, exit with status 1 (failure)
    sys.exit(1)
