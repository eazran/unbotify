# ?Interview question 1?

## Requirement
1. Please write a simple CLI application in the language of your choice that does the following:
Print the numbers from 1 to 10 in random order to the terminal.
Please provide a README, that explains detailed how to run the program on MacOS and Linux.

## Setup Prerequisites

In order to be platform compatible, this application in implemented in Python.

Linux and Mac operating systems come with Python out of the box

First, check if python already exists, run the following command on the terminal:
`python --version`

If the version of the installed Python is displayed , proceed to the next section.

Otherwise, install Python following the guide: 

Linux:
https://pimylifeup.com/installing-python-on-linux/

MacOs:
https://docs.python-guide.org/starting/install3/osx/


## Downloading the code

To download the script, press the green "clone or download" button on the top right of the github screen.

![Download Button](https://github.com/eazran/unbotify/blob/master/download_from_github.png?raw=true)

Extract the zip to a folder of your choice.

## Running the code

Open a terminal window and navigate to the folder in which you extracted the zip.

Execute the command:
`python print_random_ten.py`


# ?Interview question 2?

## Requirement
2.Imagine a server with the following specs:
- 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
- 64GB of ram
- 2 tb HDD disk space
- 2 x 10Gbit/s nics
The server is used for SSL offloading and proxies around 25000 requests per second.
Please let us know which metrics are interesting to monitor in that specific case and how would you do that? What are the challenges of monitoring this?

## Answer
First, collect metrics on the hardware infrastructure: CPU, Memory, Disk, Networking, system log files in "/var/log" folder.
Then, monitor the SSL and Proxy application server logs. On a linux server, these functions will be performed on a web server such as XGINX.

There are many monitoring tools that can perform this kind of monitoring: Amplify/AppDynamics/DataDog/Dynatrace/New Relic/Prometheus

The challenges of monitoring such a configuration is that the application behind such a proxy might not get all the details on the source of the client connection, as these were stripped in the process of SSL Offloading. As a result, monitoring this server without correlating the sessions to the application behind this proxy may complicate investigation of problems.