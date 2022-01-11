import argparse
from array import *

parser = argparse.ArgumentParser(description='Converts frequency to period')

#+----------------------------------------------------------+
#|      Hz	            kHz	        MHz	        GHz         |                 
#| s	1	            .001	    .000_001	0.000000001 |
#| ms	1000	        1	        .001	    0.000001    |
#| us	1000000	        1000	    1	        .001        |
#| ns	1000000000	    1000000	    1000	    1           |
#| ps	1000000000000	1000000000	1000_000	1000        |
#+----------------------------------------------------------+

freq_to_period = [  \
    [ 1             , .001          , .000001   , .000000001],\
    [ 1000          , 1             , .001      , .000001   ],\
    [ 1000000       , 1000          , 1         , .001      ],\
    [ 1000000000    , 1000000       , 1000      , 1         ],\
    [ 1000000000000 , 1000000000    , 1000000   ,1000       ] ] 
# Constants 
S_POS = 0
MS_POS = 1
US_POS = 2
NS_POS = 3
PS_POS = 4
HZ_POS = 0
KHZ_POS = 1
MHZ_POS = 2
GHZ_POS = 3

# Check that the input frequency is either an integer or a float
def check_freq_input_is_number(input):
    try:
        val = int(input)
    except ValueError:
        try:
            val = float(input)
        except ValueError:
            print("Input Frequency is not a number")

# Input arguments
parser.add_argument('--FREQ', metavar='FREQ', required=True, type=float, help='Sets the clock frequency.', default=0)
parser.add_argument('--FREQ_UNIT', metavar='FREQ_UNIT', required=False, type=str, help='Sets the clock frequency unit (GHz, MHz, kHz, Hz) (Default: MHz)', default='MHz')
parser.add_argument('--PERIOD_UNIT', metavar='PERIOD_UNIT', required=False, type=str, help='Sets the period unit (ps, ns, ms, s) (Default: ns).', default='ns')

args = parser.parse_args()

# Store arguments to local variables and change to upper case to avoid case-sensitive
freq_unit = args.FREQ_UNIT
freq_unit = freq_unit.upper()
period_unit = args.PERIOD_UNIT
period_unit = period_unit.upper()
in_freq = args.FREQ

# Check user input frequency unit
if(freq_unit == "GHZ"):
    FREQ_POS = GHZ_POS 
    freq_str = "GHz"   
elif(freq_unit == "MHZ"):
    FREQ_POS = MHZ_POS    
    freq_str = "MHz"   
elif(freq_unit == "KHZ") :
    FREQ_POS = KHZ_POS    
    freq_str = "kHz"   
elif(freq_unit == "HZ") :
    FREQ_POS = HZ_POS    
    freq_str = "Hz"   
else :
    print("ERROR - NON SUPPORTED FREQUENCY UNIT - MUST BE EITHER GHz, MHz, kHz, or Hz")
    exit(1)

# Check user output period unit
if(period_unit == "NS") :
    PERIOD_POS = NS_POS
    period_str = "ns"   
elif(period_unit == "PS") :
    PERIOD_POS = PS_POS
    period_str = "ps"   
elif(period_unit == "MS") :
    PERIOD_POS = MS_POS
    period_str = "ms"   
elif(period_unit == "S") :
    PERIOD_POS = S_POS
    period_str = "s"   
else :
    print ("ERROR - NON SUPPORTED PERIOD UNIT - MUST BE EITHER ps, ns, ms, or s")
    parser.print_help()
    exit(1)

# Calculate input frequency to output period
out_per = (1/int(in_freq)) * freq_to_period[PERIOD_POS][FREQ_POS]
# Print input frequency and output period
print("Frequency: {} {} Period: {} {}".format(in_freq,freq_str,out_per,period_str))
exit(0)

