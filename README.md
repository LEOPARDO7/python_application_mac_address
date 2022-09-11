# Python Program For Finding Vendor Detials From MAC Address

## What is MAC Address?

A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. 
 As typically represented, MAC addresses are recognizable as six groups of two hexadecimal digits, separated by hyphens, colons, or without a separator.
 MAC addresses are primarily assigned by device manufacturers, and are therefore often referred to as the burned-in address, or as an Ethernet hardware address, hardware address, or physical address.
 
## Python Program Prerequisite 

We are using [https://macaddress.io/](https://macaddress.io/) site for MAC lookup address.
So go to the site and create an account. After login create an API token. 

After creation it will give you an URL use the url in your code.
$ https://api.macaddress.io/v1?apiKey=API_TOKEN&output=json&search=%s 

Don't forget to replace the API_TOKEN with the token you just created.

## How Code Works? 

We are importing python request module as the requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

With the help of request module and the URL we created in API we are fecting the vendor details from the site. 

First it taking the response after that we are converting it in JSON formate. 
Once you get the data in JSON formate grep the desired Output you want.
Here we are greping company name.

## Output On Console 

First the programm will ask you to input the number of MAC address you want to query.
Once you input the value it will ask for the MAC address. 
You have to input the MAC address here and you will get the output. 





