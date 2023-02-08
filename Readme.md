# DSCC Validator script

This script is provided as-is and is meant to be used to check connectivity to DSCC and InfoSight.

### Requirements
This script was built using Python 3.10.8, but it should work on other versions. <br>
There are no dependendencies on external libraries.

#### Basic usage:  
python3 dscc_validator.py \<instance_name\> \<platform\> <br>
\<instance_name\> - (Mandatory) Defines the DSCC instance to be checked, current valid values are: us1, eu1, jp1 <br>
\<platform\> - (Optional) Can be added to check for InfoSight connectivity, current options are: nimble, primera <br>
\* nimble: Used for Nimble, Alletra 5000 and Alletra 6000
\* primera: Used for Primera and Alletra 9000

