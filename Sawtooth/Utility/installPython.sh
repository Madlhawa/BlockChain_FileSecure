#Python3.5
sudo apt-get update && sudo apt-get install checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.5

#pip
sudo apt install python3-pip
pip search search_string

sudo apt-get update -y
sudo apt-get install -y pkg-config
sudo apt install build-essential automake pkg-config libtool libffi-dev libgmp-dev
sudo apt install libsecp256k1-dev



#Remove the repo:
sudo add-apt-repository --remove ppa:fkrull/deadsnakes
#Refresh apt cache:
sudo apt-get update
#Remove the package:
sudo apt-get remove --purge python3.6

pip3 install sawtooth-sdk
pip3 install sawtooth_signing
pip3 install cbor
pip3 install sawtooth_sdk
pip3 install hashlib 
pip3 install flask
pip3 install sqlite
pip3 install requests
pip3 install flask_wtf
pip3 install flask-sqlalchemy

from web import db
from web import Record, Part
db.create_all()
