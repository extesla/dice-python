#!/bin/bash
# Copyright (c) 2016 Sean Quinn
#
# It is illegal to use, reproduce or distribute any part of this
# Intellectual Property without prior written authorization from
# the designated copyright holder.

IP_ADDRESS="$(ifconfig | grep '\<inet\>' | sed -n '1p' | tr -s ' ' | cut -d ' ' -f3 | cut -d ':' -f2)"

echo -e "[INFO ] Provisioning VM..."
sudo apt-get update
sudo apt-get install -y ack-grep nano

echo -e "[INFO ] Installing python tools and dependencies..."
sudo apt-get install -y build-essential make python2.7 python2.7-dev python-pip

echo -e "[INFO ] Installing Python dependencies via requirements.txt..."
pip install -r /vagrant/requirements.txt
