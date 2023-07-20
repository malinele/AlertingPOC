# AlertingPOC

My goal was to demonstrate how different parts of an application can communicate and handle errors effectively in a Dockerized environment. I used Docker to encapsulate the application components in a closed environment, which made it easier to manage dependencies and create a uniform deployment process.

# What I Did
Application Component Communication: I established communication channels between different parts of my application. I achieved this by using HTTP-based APIs, which allowed the components to interact and exchange data.

Docker Networking: To ensure the components could interact seamlessly, I used Docker Compose to define and run the Docker applications. I set up a custom network, allowing each component to reach the others using their service names. This way, I created an isolated environment where each component could function independently while still being able to communicate with others.

Configuration Management: To make the system flexible and easy to adjust, I managed all the configurations using a JSON file. This approach allowed me to easily switch between different settings, like moving from a development environment to a production one.

Centralized Logging with Elasticsearch: I introduced Elasticsearch into the mix to provide a centralized logging system. With this setup, every component could log its activities to Elasticsearch, making it easy for me to monitor what's happening in the system from a single place.

Error Handling: A major part of my work involved creating robust error handling mechanisms for the application components. I ensured that my system was resilient and could recover effectively from any failures. Additionally, any exceptions that occurred were logged, aiding in debugging and system maintenance.

Environment-Specific Data Logging: Besides logging general information, I also configured each component to log data specific to its environment. This data was obtained from the configuration file, making it possible for me to track how the application behaved in different environments.
