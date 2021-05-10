# Documentation
AutoRaspiSSH is a windows LAN ssh server finder.

## Usage
The config file is the only file you will ever need to edit. So lets get to what is  it about.

When you first open the file you should see this:

```JSON
{	
  "autoSSH":false,
  "ssh":{
    "username":"pi",
    "password":"raspberry"
  },
  "log_file_name":"log.txt"
}
```

The autoSSH option automaticly launches PuTTY and logs with the predefined credentials when set to `true`.

The username and password in the object ssh are the login cretentials that wil be used to automaticly login in available ssh servers on your LAN network.

For example is i would run the programm with these credentials:
```JSON
"ssh":{
  "username":"pi",
  "password":"raspberry"
}
```
The programm would search the LAN network trying to login to every available ssh server with these credentials.

```
Note: if there is no password set ("password":"") then the programm will try to log in without a password only using the username.
There for if the autoSSH option is enabled PuTTY will ask u for password.
```

The "log_file_name" is the name of the log file.

## Log file

The log file consists all the errors that happend during the requesting and also all the connections.

So if the programm succeds to log in to some address the it writes this:
```
Successfuly connected to: {address}
```
With the `{address}` representing the address it connected to.

The most common errors that can be there are:
```
Error at host: {address_1} => Authentication failed.
Error at host: {address_2} => [Errno None] Unable to connect to port 22 on {address_2}
```
And also timeout errors ocure sometimes.

Errors are complietly normal and the programm writes them every time.
