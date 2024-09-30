# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Converts a date in year/month/day/hour/minute/second format to the ractional Julian date
# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
# Output:
#  The corresponding fractional Julian date
#
# Written by Austin Zary
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# initialize script arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')

# parse script arguments
if len(sys.argv)==7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 ymdhms_to_jd.py year month day hour minute second'\
    )
    exit()

# write script below this line
## Calculate JDfractional
# Line 1:
div1 = (month-14.0)/12.0
if div1 > 0:
    div1 = math.floor(div1)
elif div1 < 0:
    div1 = math.ceil(div1)

div2 = 1461.0*(year + 4800.0 + div1)/4.0
if div2 > 0:
    Line1 = math.floor(div2)
elif div2 < 0:
    Line1 = math.ceil(div2)

# Line 2:
div3 = (month-14.0)/12.0
if div3 > 0:
    div3 = math.floor(div3)
elif div3 < 0:
    div3 = math.ceil(div3)

div4 = 367.0*(month - 2.0 - 12.0*div3)/12.0
if div4 > 0:
    Line2 = math.floor(div4)
elif div4 < 0:
    Line2 = math.ceil(div4)

# Line 3:
div5 = (year + 4900.0 + div3)/100.0
if div5 > 0:
    div5 = math.floor(div5)
elif div5 < 0:
    div5 = math.ceil(div5)

div6 = -3.0*div5/4.0
if div6 > 0:
    Line3 = math.floor(div6)
elif div6 < 0:
    Line3 = math.ceil(div6)

# Adding Lines:
JD = day -32075 + Line1 + Line2 + Line3

# Calculate Fractional Day
D = (second + 60.0 * (minute + 60.0*hour))/86400.0

# Final Julian Fractional Date Calculation
JDfractional = JD - 0.5 + D

print(JDfractional)