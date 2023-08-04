cd ~
apt update -y && apt install zsh tmux -y
which zsh
chsh -s `which zsh`
wget -O .zshrc https://raw.githubusercontent.com/pswalia2u/Pentest_Commands/master/.zshrc
wget -O .tmux.conf https://raw.githubusercontent.com/pswalia2u/Pentest_Commands/master/env/.tmux.conf
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update -y
sudo apt-get install sublime-text -y
sudo git clone https://github.com/zsh-users/zsh-autosuggestions.git /usr/share/zsh-autosuggestions