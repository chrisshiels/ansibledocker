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


    (virtualenv) host$ # Build Docker image locally to test build.
    (virtualenv) host$ cd docker
    (virtualenv) host$ docker build -t helloworld:0.0.1 .
    (virtualenv) host$ cd ..


    (virtualenv) host$ # Run Vagrant with Ansible provider.
    (virtualenv) host$ vagrant up


    (virtualenv) host$ # Test Vagrant virtual machine with testinfra.
    (virtualenv) host$ testinfra \
        --hosts=default --ssh-config=<(vagrant ssh-config) test_vagrant.py


    (virtualenv) host$ # Check output from virtual machine.
    (virtualenv) host$ curl http://192.168.33.10/


## What's missing

- Molecule testing of individual Ansible roles.

- Got conu working on Fedora but couldn't get it working on macOS.

```
    (virtualenv) host$ # Test Docker image locally with conu.
    (virtualenv) host$ cd docker/test
    (virtualenv) host$ pytest -v
```
