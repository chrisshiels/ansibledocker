# ansible-docker


## Pre-requisites, e.g. on macOS

- Install VirtualBox.
  (See:  https://www.virtualbox.org/)

- Install Vagrant.
  (See:  https://www.vagrantup.com/downloads.html)

- Install Docker.
  (See:  https://docs.docker.com/docker-for-mac/)

- Install Brew with python and virtualenv.
  (See:  https://docs.brew.sh/Installation)

```
    host$ brew install python
    host$ pip3 install virtualenv
```

## Steps

    host$ # Clone repository.
    host$ git clone https://github.com/chrisshiels/ansibledocker.git
    host$ cd ansibledocker


    host$ # Configure virtualenv.
    host$ virtualenv virtualenv
    host$ . virtualenv/bin/activate
    (virtualenv) host$ pip install -r requirements.txt 


    (virtualenv) host$ # Build Docker image locally.
    (virtualenv) host$ cd docker
    (virtualenv) host$ docker build -t helloworld:0.0.1 .


    (virtualenv) host$ # Test Docker image locally with conu.
    (virtualenv) host$ cd test
    (virtualenv) host$ pytest -v
    (virtualenv) host$ cd ../..


    (virtualenv) host$ # Run Vagrant with Ansible provider.
    (virtualenv) host$ vagrant up


    (virtualenv) host$ # Test Vagrant virtual machine with testinfra.
    (virtualenv) host$ testinfra \
        --hosts=default --ssh-config=<(vagrant ssh-config) test_vagrant.py


    (virtualenv) host$ # Check output from virtual machine.
    (virtualenv) host$ curl \
        http://$(vagrant ssh-config | awk '/HostName/ {print $2}')/


## What's missing

- Ideally would include molecule testing of individual Ansible roles.
