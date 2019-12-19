# nRF-Controller Reference
The nRF-Controller is a tool used to test a Thread Mesh Network. It uses the OpenThread CLI to make Benchmark tests
on a the Network. To start testing write your tests inside the Workflow.py file.

## Controller Command List

* [ping](#ping)
 
## Controller Command Details

### ping
Writes the results of your given ping execution into a file with a given name.
 
 
     def ping(self, ipaddr="ff03::1", size=8, count=1, interval=1, file_name="results/result.csv"):
