#Tinyutils

This is the initial Documentation about the project **tinyutils**, we appreciate more inputs from community users about the project.


###About

We wish to build a simple utility that gives some basic information about the system. Executing a command with a specific switch should give basic, intuitive information about the system.

The below is the switch table and its expected output

 Switch|Output
:-----:|:------------------------:
   -n  |  Network information
   -m  |  Memory information
   -s  |  Disk-Space information
   -p  |  Processor information

Executing the command 'tinyutils' with any of above Switch should give appropriate output. Executing command without any switch should print all the information in a intuitive way for naive users.

>###Example


```

$ tinyutils -n

Connected Networks : [eth0, ip : x.x.x.x]

```

>###Note

* Currently the project is for **Linux Systems** only
