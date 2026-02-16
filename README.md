
In this project, I built a small DevOps-style application to understand how real applications are deployed using Docker. 

Initially, I ran a Flask application container directly and exposed it to the browser, but later I improved the architecture by introducing an Nginx reverse proxy and a user-defined Docker network to make the setup closer to a real production environment.

The Flask application works as the backend service, while Nginx handles incoming requests from the browser and forwards them internally to the application container. This helped me understand how external traffic is routed securely without exposing backend services directly.

I also used Docker Compose to manage multiple containers together instead of running many Docker commands manually. With Docker Compose, the entire application stack (network, containers, and configurations) can be started using a single command.

Through this project, I gained hands-on experience with Dockerfiles, container networking, reverse proxy configuration, environment variables, and multi-container orchestration.

