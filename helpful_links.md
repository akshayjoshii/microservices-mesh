# Web Articles & Commands Used During Development

## References

1. [Flask Application over HTTPS](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https)
2. [Common Internet Passwords](https://pwlist.cfapps.eu10.hana.ondemand.com/passwords.txt)
3. [Flask API & MySQL on Kubernetes](https://github.com/RikKraanVantage/kubernetes-flask-mysql)
4. [Multiple Dockerfiles](https://stackoverflow.com/questions/27409761/docker-multiple-dockerfiles-in-project)

## Commands

1. Generate Self-Signed SSL Certificate for HTTPS:  
   > openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

2. Build multiple Dockerfiles in the same project
   > docker build -f service_1.Dockerfile -t poojiyengar5/service-1 . \
   > docker build -f service_1.Dockerfile -t poojiyengar5/service-2 . & so on...

3. Setup minikube for the first time (only after wsl2, docker, minicube & kubectl are installed)
   > minikube start --driver=docker
