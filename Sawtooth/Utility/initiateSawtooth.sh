#runsawtooth on docker
cd /usr/local/bin/
docker-compose -f sawtooth-default.yaml up
docker-compose -f sawtooth-default.yaml down

#running commands on local shell
curl http://localhost:8008/blocks
curl --request POST --header "Content-Type: application/octet-stream" --data-binary @intkey.batches "http://localhost:8008/batches"

#running commands on docker shell
docker exec -it sawtooth-shell-default bash
sawtooth block list --url hyyp://rest-api:8008

#installing docker
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo systemctl status docker
sudo curl -L https://github.com/docker/compose/releases/download/1.25.5/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
cd /usr/local/bin/docker-compose
cd /usr/local/bin/
ls
docker-compose -f sawtooth-default.yaml up
curl –O https://sawtooth.hyperledger.org/docs/core/nightly/master/app_developers_guide/sawtooth-default.yaml
ls
cp ~/FileSecure_BC/Sawtooth/sawtooth-default.yaml ./
sudo cp ~/FileSecure_BC/Sawtooth/sawtooth-default.yaml ./
ls
docker-compose -f sawtooth-default.yaml up
sudo systemctl status docker
docker info
sudo docker info
psu
sudo ls -la /var/run/docker.sock
sudo systemctl status docker
cd /usr/local/bin/
docker-compose -f sawtooth-default.yaml up