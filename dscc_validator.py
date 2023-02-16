# Dependency imports

# Import modules to check DNS resolution
import dns
import dns.resolver

# Import module to check for connectivity to the specified URLs / Ports
import socket

# Import module to read CLI parameters
import sys

# Silence warnings about deprecations
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Function definitionss

# Function to query DNS resolution, takes an URL as parameter
# During execution it prints the resolved IPs if successful and the DNS error on specific failures (Not all DNS error codes are tested)
# Returns True if resolution succeded and False if it failed
def dns_check(url):
    
    A_records = []

    try:
        result = dns.resolver.query(url, "A")
        for IPval in result:
            A_records.append(IPval.to_text())
        dns_pass = True

        print("DNS reolution to " + url + " is working!")
        print("The resolved IPs are: " + str(A_records))
        
    except dns.resolver.NXDOMAIN:
        print("DNS resolution for URL " + url + " failed. (NOT-FOUND)")
        dns_pass = False
    except dns.resolver.Timeout:
        print("DNS resolution for URL " + url + " failed. (TIMEOUT)")  
        dns_pass = False
    except dns.resolver.NoNameservers as e:
        print("DNS resolution for URL " + url + " failed. (NO NAMESERVERS)")
        #print(str(e))
        dns_pass = False
    except dns.resolver.NoAnswer:
        print("DNS resolution for URL " + url + " failed. (NO ANSWER)")
        dns_pass = False

    return dns_pass

# Function to check if connectivity to an URL on a specific port is working
# During execution it prints if the connection was successful or not
# Returns True if connection succeds and False if it fails    
def port_check(url, port):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    result = sock.connect_ex((url,int(port)))
    if(result == 0):
        print("Connection to " + url + " was successful on port " + str(port))
        print()
        port_pass = True
    else:
        print("Connection to " + url + " on port " + str(port) + " failed!")
        print("Please check your firewall configuration.")
        print()
        port_pass = False

    return port_pass

# Define valid arguments
# Available DSCC instances
dscc_valid_instances = ["us1", "eu1", "jp1"]
# Array type or service (BRS at the moment)
platform_valid = ["nimble", "primera", "5000", "6000", "9000", "brs"]

# Define default argument values 
dscc_instance = "default"
platform = "default"

# Initialize error type variable
input_error = "none"

# Read CLI arguments and set them to the appropriate variables
if(len(sys.argv) == 1):
    input_error = "quantity"
elif(len(sys.argv) == 2):
    dscc_instance = sys.argv[1]
    # Set dscc_instance to help just to print usage information
    if(sys.argv[1] == "help"):
        input_error = "quantity"
elif(len(sys.argv) == 3):
    dscc_instance = sys.argv[1]
    platform = sys.argv[2]

# Check if arguments are valid and set error type if applicable
if(dscc_instance != "default"):
    if(dscc_instance not in dscc_valid_instances and dscc_instance != "help"):
        input_error = "invalid instance"

if(platform != "default"):
    if(platform not in platform_valid):
        input_error = "invalid platform"

# Print error message and exit
if(input_error != "none"):
    if(input_error == "quantity"):
        print()
        if(dscc_instance != "help"):
            print("Arguments missing....")
        print() 
        print("Usage: dscc_validator.exe <instance_name> <platform>.")
        print("Mandatory argument: Valid options for <instance_name> are 'us1', 'eu1', 'jp1'")
        print("Optional argument to check for InfoSight connectivity or Backup and Recovery Service connectivity: Valid options for <platform> are:")
        print("'5000' applies for Alletra 5000")
        print("'6000' applies for Alletra 6000")
        print("'9000' applies for Alletra 9000")
        print("'nimble' applies for Nimble")
        print("'primera' applies for Primera")
        print("'brs' applies for Backup and Recovery Service")
        print()
    if(input_error == "invalid instance"):
        print()
        print("Invalid instance entered....") 
        print("Valid options for <instance_name> are 'us1', 'eu1', 'jp1'")
        print()
    if(input_error == "invalid platform"):
        print()
        print("Invalid platform entered....")
        print("Valid options for <platform> are:")
        print("'5000' applies for Alletra 5000")
        print("'6000' applies for Alletra 6000")
        print("'9000' applies for Alletra 9000")
        print("'nimble' applies for Nimble")
        print("'primera' applies for Primera")
        print("'brs' applies for Backup and Recovery Service")
        print()
    
    sys.exit("Please try again...")

# Define URLs for DSCC
device_url = "device.cloud.hpe.com"
tunnel_url =  "tunnel-" + dscc_instance + ".data.cloud.hpe.com"
brs_do_url = "midway.ext.hpe.com"
if(platform != "brs"):
    urls = [device_url, tunnel_url]
else:
    urls = [tunnel_url, brs_do_url]
port = 443

localhostname = socket.gethostname()
localip = socket.gethostbyname(localhostname)

# Script headers
print()
print("*********************************************************************")
print("*          Checking communication to DSCC from "+ localip + "       *")
print("*********************************************************************")
print()

dnsresult = dns.resolver.query("hpe.com", "A")
dnsserver = dnsresult.nameserver

print("The DNS server used for name resolution is: " + dnsserver) 
print()

# Test for DSCC connectivity
for url in urls:
    # Conditional to skip connectivity test if DSN resolution fails
    dns_result_dscc = dns_check(url)
    if(dns_result_dscc == True):
        port_d = port_check(url, port)

# Define URLs for InfoSight
if(platform != "default" and platform != "brs"):
    if(platform == "nimble" or platform == "5000" or platform == "6000"):
        urls = ["nsdiag.nimblestorage.com", 
            "update.nimblestorage.com", 
            "nsalerts.nimblestorage.com",
            "nsstats.nimblestorage.com", 
            "hogan.nimblestorage.com"]
        
    elif(platform == "primera" or platform == "9000"):
        urls = ["p1lg501824.it.hpe.com",
        "p1lg501825.it.hpe.com",
        "p1lg501826.it.hpe.com",
        "p1lg503763.it.hpe.com",
        "p1lg503764.it.hpe.com",
        "p2lg501868.it.hpe.com",
        "p2lg501869.it.hpe.com",
        "p2lg501870.it.hpe.com",
        "p2lg504047.it.hpe.com",
        "p2lg504048.it.hpe.com"]

    print()
    print("**************************************************************************")
    print("*         Checking communication to InfoSight from " + localip + "        *")
    print("**************************************************************************")
    print()
    # Test for InfoSight connectivity
    for url in urls:
        dns_result_infogight = dns_check(url)
        # Conditional to skip connectivity test if DSN resolution fails
        if(dns_result_infogight == True):
            if(url == "hogan.nimblestorage.com"):
                port = 2222
            else:
                port = 443
            port_d = port_check(url, port)




    

        