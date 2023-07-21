# AlertingPOC

My goal was to demonstrate how different parts of an application can communicate and handle errors effectively in a Dockerized environment. I used Docker to encapsulate the application components in a closed environment, which made it easier to manage dependencies and create a uniform deployment process.

## What I Did

Application Component Communication: I established communication channels between different parts of my application. I achieved this by using HTTP-based APIs, which allowed the components to interact and exchange data.

Docker Networking: To ensure the components could interact seamlessly, I used Docker Compose to define and run the Docker applications. I set up a custom network, allowing each component to reach the others using their service names. This way, I created an isolated environment where each component could function independently while still being able to communicate with others.

Configuration Management: To make the system flexible and easy to adjust, I managed all the configurations using a JSON file. This approach allowed me to easily switch between different settings, like moving from a development environment to a production one.

Centralized Logging with Elasticsearch: I introduced Elasticsearch into the mix to provide a centralized logging system. With this setup, every component could log its activities to Elasticsearch, making it easy for me to monitor what's happening in the system from a single place.

Error Handling: A major part of my work involved creating error handling mechanisms for the application components. I ensured that my system was resilient and could recover effectively from any failures. Additionally, any exceptions that occurred were logged, aiding in debugging and system maintenance.

Environment-Specific Data Logging: Besides logging general information, I also configured each component to log data specific to its environment. This data was obtained from the configuration file, making it possible for me to track how the application behaved in different environments.

## README

### Quick Start
1. Clone this repository.
1. Ensure Docker and Docker Compose are installed on your machine.
1. Navigate to the root directory of the project in your terminal.
1. Run docker-compose up to start the services and the Elasticsearch instance.
1. Run the execution script using python3 script.py to simulate traffic to Service1.

### Services
The services are implemented as Flask applications. Each service exposes a single endpoint that, when invoked, calls a method that executes some logic, logs the execution to Elasticsearch using the shared logging module, and returns a response.

### Shared Logging Module
The shared logging module is a Python module that encapsulates the logic for logging data to Elasticsearch. It is imported and used by each service to log the execution of its methods. The module is located in a shared directory that is accessible to all services.

### Elasticsearch
The Elasticsearch instance is run as a Docker container and is exposed on port 9200. It is configured to run as a single-node cluster.

### Docker Compose
Docker Compose is used to define and manage all the Docker containers. The docker-compose.yml file specifies the services, the Elasticsearch instance, and their configurations.

### Execution Script
A Python script is provided to send HTTP requests to Service1 at random intervals of up to 5 seconds. This script simulates traffic to the service and triggers the logging of data to Elasticsearch.
