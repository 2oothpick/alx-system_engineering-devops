# Web_infrastructure_design
Often referred to as web architecture design is the process of planning and creating the foundational structure and components that support web applications, websites and online services. It encompasses the architecture, hardware, software, networks and configurations necessary to ensure the reliability, scalability, security and performance of web-based systems.

## Key components and considerations in web infrastructure design include:

 ### Servers and Hosting: 
A server is a piece of computer hardware or software that proides functionality for other programs or devices.Servers can be physical or virtual as in the case of cloud hosting. since servers are computers, they run an OS. some of the more popular ones are Linux and windows.Servers are located in datacenters. Servers can serve various functions, but for this project, we would be looking at servers as web servers and application servers.
    * Web server: web servers just act as HTTP servers, receiving HTTP requests and sending HTTP responses allowing users to access hosted files. popular examples include: NGINX and Apache.
    * Application servers: this is a server-side software platform designed to host and run web-based applications and provides a runtime environment for applications and business logic. They are usually used in conjuction withh a database and a web server to deliver dynamic content in dynamic websites. Popular examples include: Apache TomEE and Oracle.

### Databases:
 This is a collection of data for our website. We select a database management system (DBMS), database schema design, and replication strategies to manage data for our web application. Popular DBMSs include MySQL.

### Codebase:
 this is a collection of the source code and related files that make up our software application or project. it includes all the prorgramming codes, scripts, configuration files, and documentation necessary for developing, maintaining and running the software. 

 ### Load balancing:
 A load balancer is a networrking device or software component that distributes incoming trafic across multiple servers to ensure utilization, high availability and scalability. 

 ### Monitoring:
 this refers to the practice of continuously observing and measuring the performance, availability and health of various components and services within a web application. It involves collecting data, analyzing it and taking appropriate actions to ensure the system operates as expected.Popular monitoring softwares include DataDog, Uptime Robot and NewRelic.

 ### Firewall
This is a network security device or software that serves as a barrier between an organization's internal network and the external internet.

### DNS:
This is the technology that translates human-adapted, text-based domain names to machine-adapted, numeric-based IP addresses.

### Scaling stratagies: 
Planning for scalability and the ability to handle increase traffic and growing user bases. This may involve horizontal scaling (adding more server) or vertical scaling (upgrading server resources).

### High Availability:
Ensuring high availability and minimizing downtime through failover mechanisms, load balancing, and resilient system architecture.


## Tast details
### [0-simple_web_stack ](https://github.com/2oothpick/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack "github"):
![Imgur](https://imgur.com/VK39gaC)
Issues with the infrastructure:
* DNS has only one name server and this is a single point of failure.
* Since there is only one server, the website would be temporarily down when new code is deployed and the web server needs to be restarted.
* This infrastructure cannot scale and will not be able to handle traffic exceeding the server's capacity.

