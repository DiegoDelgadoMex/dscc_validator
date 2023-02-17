# DSCC Validator script

This script is provided as-is and is meant to be used to check connectivity to DSCC and InfoSight. <br>
<br>
Currently the following checks are supported: <br>
- Array connectivity for Alletra 5000, Alletra 6000, Alletra 9000, Nimble and Primera
- Backup and Recovery Service

### Requirements
This script was built using Python 3.10.8, but it should work on other versions. <br>
There are no dependendencies on external libraries. <br>
The script should be executed on a system on the network that will be used for array management. 

#### Basic usage:  
python dscc_validator.py \<instance_name\> \<platform\> <br>
<br>
\<instance_name\> - (Mandatory) Defines the DSCC instance to be checked, current valid values are: us1, eu1, jp1 <br>
\<platform\> - (Optional) This option is used to validate InfoSight connectivity for Block Storage platforms or to check connectivity to DSCC for additional services like Backup and Recovery Service. Available options are: <br>  

<br>
* *5000*: Used for Alletra 5000 <br>
* *6000*: Used for Alletra 6000 <br>
* *9000*: Used for Alletra 9000 <br>
* *nimble*: Used for Nimble <br>
* *primera*: Used for Primera <br>
* *brs*: Used for Backup and Recovery Service <br>
<br>
There's some simple help information in the script that can be read running the script as follows: <br>
python dscc_validator.py help

#### Windows executable
A Windows executable is provided for systems that don't have Python installed, the usage is the same as the Pyhton script, but you don't need to run the python command. <br>
<br>
dscc_validator.exe \<instance_name\> \<platform\> <br>
<br>
\<instance_name\> - (Mandatory) Defines the DSCC instance to be checked, current valid values are: us1, eu1, jp1 <br>
\<platform\> - (Optional) This option is used to validate InfoSight connectivity for Block Storage platforms or to check connectivity to DSCC for additional services like Backup and Recovery Service. Available options are: <br>  

<br>
_5000_: Used for Alletra 5000 <br>
*6000*: Used for Alletra 6000 <br>
*9000*: Used for Alletra 9000 <br>
*nimble*: Used for Nimble <br>
*primera*: Used for Primera <br>
*brs*: Used for Backup and Recovery Service <br>

***Notice:*** This executable was created with PyInstaller and is not digitally signed; some antithreat programs might flag it as unsafe

#### Troubleshooting
The instructions show python as the command, but you should use the correct python command for your environment (python, python27, python3 for example)

