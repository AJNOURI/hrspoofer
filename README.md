# About this Repo

This is a container based on [docker-library/python2.7](https://github.com/docker-library/python).

The main python script hrspoofer.py (http request spoofer), uses httplib to generate http requests with spoofed source ip address to simulate different client.  
The list of spoofed source IPs are simply secondary ip addresses assigned to the main container interface.

The script genip.py  generates a csv file with the pairs of ip addresses from the subnet of your choice and a random port from the ephemeral source port range (32768-61000). The script also generates the corresponding manual commands  

> ip address add \<X.X.X.X/X\> dev \<int\>

into a shell script to be executed to configure the secondary addresses.

**1- Generate the spoofed source IPs**

> ./genip.py   
>  
>  Usage: ./genip.py \<X.X.X.X/mask\> \<output_int\> \<output_file.csv\>  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X.X.X.X/mask          : the subnet from which you want to generate the ip addresses.  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output_int        : the egress interface receiving the generated secondary addresses.  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output_file.csv   : The resulting file containing ip,port.  

Example:  
> python genip.py 10.10.0.0/26 eth0 ip_port.csv > setip.sh

**2- Assign the IP's as secondary addresses**  
> bash setip.sh


**3- Generate http requests from there list of secondary addresses**
> ./hrspoofer.py   
>    
> Usage: ./hrspoofer.py \<destination host\> \<destination port\> \<requested_page\> \<file.csv\>  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination host/port  : Web server virtual IP and port to test  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requested page         : Keep empty if default index pages  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\<file.csv\>           : obtained using the script \>\>  genip.py \<\<   

Example:
> python hrspoofer.py 192.168.18.100 80 test.php ip_port.csv 

