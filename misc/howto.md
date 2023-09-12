Varun Saini

# How to do things

## Questions

- **What's your computer's IP address for its current Internet connection? (0-point bonus: how can you tell the difference between your Ethernet IP and your wireless IP if you have both connections active?)**
  - Public IP: `curl ifconfig.m`
  - Local IP: `ipconfig getifaddr en0`

- **How can you determine the IP address associated with a given host name?**
  - `nslookup <hostname>`

- **How can you determine the host name(s) associated with a given IP address?**
  - `nslookup <ipaddress>`

- **How can you copy a file from one computer to another? Or more to the point, if you create a file on Kali virtual machine and you want to put it someplace where you can save it, like your your account on mantis.mathcs.carleton.edu, how do you go about it from the Kali command-line interface?**
  - [Source](https://kb.iu.edu/d/agye)
  - `scp [options] username1@source_host:directory1/filename1 username2@destination_host:directory2/filename2`

- **How can you tell whether there's a process listening on a given port (e.g. port 80 or port 22) on a given host?**
  - `lsof -i -P -n | grep LISTEN | grep <PORT>`
  - [Source](https://www.cyberciti.biz/faq/unix-linux-check-if-port-is-in-use-command/)

- **How can you tell which ports have processes listening on them on a given host?**
  - `lsof -i -P -n | grep LISTEN`
  - [Source](https://www.cyberciti.biz/faq/unix-linux-check-if-port-is-in-use-command/)

- **How can you retrieve and save a given web page (say https://google.com/ or https://carleton.edu/) in a file on your system?**
  - `wget -O <filename> <url>`
  - `curl -o <filename> <url>`

- **How can you view the HTTP headers sent back from a specified web server when you request one of its pages?**
  - `curl -I <url>` (only response headers)
  - `curl -v <url>` (includes request and response headers)

- **How can you view the HTTP headers that your computer sends to the web server when you do the tasks in the previous two questions?**
  - `curl -v <url>` (includes request and response headers)

**Some commands that you might find interesting: nc (also known as netcat), nmap, curl, wget. There are other relevant commands, of course, so use your internet-searching powers.**