# Web_infrastructure_design
Often referred to as web architecture design is the process of planning and creating the foundational structure and components that support web applications, websites, and online services. It encompasses the architecture, hardware, software, networks, and configurations necessary to ensure the reliability, scalability, security, and performance of web-based systems.

## Key components and considerations in web infrastructure design include:

 ### Servers and Hosting: 
A server is a piece of computer hardware or software that provides functionality for other programs or devices. Servers can be physical or virtual as in the case of cloud hosting. since servers are computers, they run an OS. some of the more popular ones are Linux and Windows. Servers are located in data centers. Servers can serve various functions, but for this project, we would be looking at servers as web servers and application servers.
    
    * Web server: web servers just act as HTTP servers, receiving HTTP requests and sending HTTP responses allowing users to access hosted files. popular examples include NGINX and Apache.
   
    * Application servers: this is a server-side software platform designed to host and run web-based applications and provides a runtime environment for applications and business logic. They are usually used in conjunction with a database and a web server to deliver dynamic content on dynamic websites. Popular examples include Apache TomEE and Oracle.

### Databases:
 This is a collection of data for our website. We select a database management system (DBMS), database schema design, and replication strategies to manage data for our web application. Popular DBMSs include MySQL.

### Codebase:
 this is a collection of the source code and related files that make up our software application or project. it includes all the programming codes, scripts, configuration files, and documentation necessary for developing, maintaining, and running the software. 

 ### Load balancing:
 A load balancer is a networking device or software component that distributes incoming traffic across multiple servers to ensure utilization, high availability, and scalability. 

 ### Monitoring:
 this refers to the practice of continuously observing and measuring the performance, availability, and health of various components and services within a web application. It involves collecting data, analyzing it, and taking appropriate actions to ensure the system operates as expected. Popular monitoring software includes DataDog, Uptime Robot, and NewRelic.

 ### Firewall
This is a network security device or software that serves as a barrier between an organization's internal network and the external internet.

### DNS:
This is the technology that translates human-adapted, text-based domain names to machine-adapted, numeric-based IP addresses.

### Scaling stratagies: 
Planning for scalability and the ability to handle increased traffic and growing user bases. This may involve horizontal scaling (adding more servers) or vertical scaling (upgrading server resources).

### High Availability:
Ensuring high availability and minimizing downtime through failover mechanisms, load balancing, and resilient system architecture.


## Task details
### [0-simple_web_stack ](https://github.com/2oothpick/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack "github"):
Issues with the infrastructure:
* DNS has only one name server and this is a single point of failure.
* Since there is only one server, the website would be temporarily down when new code is deployed and the web server needs to be restarted.
* This infrastructure cannot scale and will not be able to handle traffic exceeding the server's capacity.

### [1-distributed_web_infrastructure](https://github.com/2oothpick/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure)

For this task, I added a second passive HAProxy load balancer to prevent it from becoming a single point of failure and use a virtual IP address across both load balancers.

The load balancers have an active-active balancer setup. ie: both server instances are actively serving traffic simultaneously to evenly distribute incoming requests, this provides high availability. 
I assume the website has high traffic.

The MySQL uses a Master-Replica configuration used to replicate data and keep it synchronized. This allows only the Master database node to accept read/write while the Replica accepts only reads.

Issues with the infrastructure:
* There is no failover mechanism in place in the off chance that both servers crash or become unavailable.

* There is no firewall on servers

* Traffic is unencrypted.

* There is no Monitoring

### [2-secured_and_monitored](https://github.com/2oothpick/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure)
For this task, I added three firewalls, one for each server and the last one to the load balancer to filter network traffic.

Added SSL to encrypt traffic so it can't be read if intercepted.

A monitoring system (DataDog) to check for any anomalies. It comprises a client collecting data and sending it to the monitoring system and triggers an alert if QPS is getting out of control.

Issues with the infrastructure:
* Terminating SSL at the load balancer level is an issue  because the traffic between the load balancer and the web servers is unencrypted.

* Having only one MySQL server accepting writes is an issue because if the master inexplicably becomes unavailable, the application would not be able to write to the database anymore.

* Having servers with all the same components (database, web server, and application server) might be a problem because when there is maintenance performed on a server for a specific component, it will affect other components that are on it.

## [3-scale_up](https://github.com/2oothpick/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up)
For this project, I added another server cluster(passive cluster) as a failover mechanism, should the active cluster become unavailable.

The databases in the active cluster are both masters(ie: they can both write data) should the other server in the active cluster become unavailable, the application would still be able to write to the database.
The databases in the passive cluster are both replicas, ie: they only read data. This is for synchronization

SSL is terminated at both the load balancer and server level, encrypting internal traffic
