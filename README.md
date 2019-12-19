# nRF-Controller Reference
The nRF-Controller is a tool used to test a Thread Mesh Network. It uses the OpenThread CLI to make Benchmark tests
on a the Network. To start testing write your tests inside the Workflow.py file.

## Controller Command List
* [Controller](#Controller)
* [ping](#ping)
* [console](#console)
 
## Controller Command Details

### Controller
initialize the Controller giving it a valid Port to connect to.

### ping
Writes the results of your given ping execution into a csv file with the given path. the default file is located at 
"results/result.csv". You may change the value of the ip-Address, size, number of executions, the interval, and the 
path of the results file.

 
     def ping(self, ipaddr="ff03::1", size=8, count=1, interval=1, file_name="results/result.csv"):


### console
call to open a console on the given Port. 