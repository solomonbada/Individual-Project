Introduction The web app was maded using Flask which is a micro web framework using python language. The environment used to run the app is Ubuntu 16.04 and Google cloud platform

Pre-requistes sudo apt-get isntall python3 sudo apt-get install python3-pip sudo pip3 install virtualenv

Running the App with Google cloud platform with Jenkins #install git sudo apt-get install git #clone down the repo git clone https://github.com/sharonkele/gcp cd in Stylist #install Jenkins using the the script called Jenkins-install.sh #Create a new item with freestyle project #In the execute shell add the following commands

sudo apt-get update sudo apt-get install python3 -y sudo apt-get install python3-pip -y

cd Stylist

chmod 777 requirements.txt

pip3 install -r requirements.txt

python3 run.py

SystemD #The app can also be run with systemD #Enter the following command into the execute shell instead

sudo apt-get update sudo pip3 install virtualenv cd Stylist sudo cp flask-app.service /etc/systemd/system/ sudo systemctl daemon-reload sudo systemctl stop flask-app

install the application files
install_dir=/opt/flask-app sudo rm -rf ${install_dir} sudo mkdir ${install_dir} sudo cp -r ./* ${install_dir} sudo chown -R pythonadm:pythonadm ${install_dir}

# configure python virtual environment and install dependencies
sudo su - pythonadm << EOF cd ${install_dir} virtualenv -p python3 venv source venv/bin/activate sudo apt-get update sudo apt-get install python3 -y sudo apt-get install python3-pip -y chmod 777 requirements.txt pip3 install -r requirements.txt EOF

sudo systemctl start flask-app

To Run with Docker in Google cloud platform

#First install Docker curl https://get.docker.com|sudo bash #to use docker without sudo sudo usermod -aG docker $(whoami) #to confirm user has been added to docker group id -nG #check status of docker systemctl status docker #create an image docker run hello-world

#Create a Docker directory mkdir 'your choosen name'

#Pull down Dockerfile and use it to build an image docker build -t Stylist #run the app in docker run -d -p 5000:5000 --name flaskapp flaskapp

To run with Jenkins
