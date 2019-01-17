#Installer for anubis
# First things first

# Declare variables
#"""Colors
red=`tput setaf 1`
green=`tput setaf 2`
normal=`tput sgr0`
#"""OS
os=`uname`
distribution=`awk '{print $1}' /etc/issue`
user=`whoami`

# Cool Banner
# Loving fancy things
cat << EOF
 █████╗ ███╗   ██╗██╗   ██╗██████╗ ██╗███████╗
██╔══██╗████╗  ██║██║   ██║██╔══██╗██║██╔════╝
███████║██╔██╗ ██║██║   ██║██████╔╝██║███████╗
██╔══██║██║╚██╗██║██║   ██║██╔══██╗██║╚════██║
██║  ██║██║ ╚████║╚██████╔╝██████╔╝██║███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝
                   Installer

EOF
echo "OS:${green}$os${normal}  Distribution:${green}$distribution${normal}  Logged in as:${green}$user${normal}"

#Request root access/sudo
function check() {
  #$EUID = user id 0 is for root
  if [[ "$EUID" -ne 0 ]]; then
    echo "${red}[✘]Error!!! Not enough priviledged${normal}"
    sleep 3
    echo "${red}[✘]Requesting root${normal}"
    #Running the installer with sudo
    sudo ./installer.sh
    # Prevent script from continue running
    exit 1
  fi
}


#Check for dependencies
if command -v python3 &>/dev/null; then
    echo ""
    echo "${green}[✔]Python3 installed${normal}"
    echo ""
else
    echo "${red}[✘]Python3 is not installed${normal}"
    py3=False
fi

#Install Pip for python3
sudo apt-get install python3-pip -y
if [ $? -eq 0 ]; then
    echo "${green}[✔]Pip3 successfully installed${normal}"
else
    echo "${red}[✘]Pip3 has not installed${normal}"
fi

#Check internet connection
# Alt ping http://www.msftncsi.com/ncsi.txt
wget -q --spider http://google.com

if [ $? -eq 0 ]; then
    echo "[*]̾i̾n̾s̾t̾a̾l̾l̾i̾n̾g ̾d̾e̾p̾e̾n̾d̾e̾n̾c̾i̾e̾s"
    # Installing argcomplete quietly
    pip install argcomplete 2>&1 >/dev/null &
    PID=$!
    i=1
    sp="/-\|"
    echo -n ' '
    while [ -d /proc/$PID ]
    do
      printf "\b${sp:i++%${#sp}:1}"
    done
    activate-global-python-argcomplete

    #Install Python3
    if py3=False; then
      apt-get -q --assume-yes install python3 2>&1 >/dev/null
    fi


else
    echo "${red}[**]${normal}Error${red}[**]${normal}"
    echo "Cannot complete Installation :("
    echo "Please check your internet connection"
fi
