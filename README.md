# Containerized Microservice Mesh Development & Depolyment using Python, Flask & Kubernetes

## Programming Task

1. Your task is to build four simple microservices and wire them up in a Kubernetes cluster, e.g. using [Link](https://minikube.sigs.k8s.io/docs/start/).

2. The first microservice provides a simple web interface and allows the entry of a password. (A simple HTML form is sufficient.) This password is sent to all the other microservices and the responses are displayed on this HTML page. (No styling needed.)

3. The second microservice receives a password, calculates its strength and sends the score back to the caller. Please implement this from scratch. (See [Link](https://www.uic.edu/apps/strong-password/) for an example how to calculate the password strength.)

4. The third microservice receives a password, checks if the last 10 calls contained the same password and sends this information back to the caller.

5. The fourth microservice receives a password, checks if the password matches a password on a common password list on the Internet and sends this information back to the caller. (Simple text file with one password per line. Use [Link](https://pwlist.cfapps.eu10.hana.ondemand.com/passwords.txt)

6. Please present your implementation and your setup during the interview.

## Discussion Task

1. Get familiar with the concept of Service Meshes and in particular Istio.

2. Select and explain 2 of the 4 mesh qualities with your setup (an implementation is not necessary):

    * Resilience
    * Observability
    * Routing
    * Security

## Requirements

1. Python 3
2. flask
3. minikube
4. kubectl
5. hashlib
6. requests
7. pyopenssl (optional - to generate self-signed SSL certificate)

## Hints

1. For the microservices, use a programming language of your choice.
2. Feel free to also use helpful libraries and frameworks, if necessary.
3. Please also consider the following code qualities: object-oriented programming principles (if applicable), clean code, design patterns, testing, documentation, etc.
4. Please put all your artifacts into a public or private Git repository at least 7 days before the interview. If you choose a private repository, please let us know how we can access it.

### Author

Poojitha Vijayanarasimha
