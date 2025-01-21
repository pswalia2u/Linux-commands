#wget -qO- https://raw.githubusercontent.com/pswalia2u/Pentest_Commands/refs/heads/master/env/ready.sh | bash
touch ~/.hushlogin
cd ~
sudo apt update -y && sudo apt install zsh tmux vim -y && sudo apt -y install kali-root-login
which zsh
chsh -s `which zsh`
wget -O .zshrc https://raw.githubusercontent.com/pswalia2u/Pentest_Commands/master/.zshrc
wget -O .tmux.conf https://raw.githubusercontent.com/pswalia2u/Pentest_Commands/master/env/.tmux.conf
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update -y
sudo apt-get install sublime-text git -y
sudo wget -qO- https://api.github.com/repos/VSCodium/vscodium/releases/latest | grep browser_download_url | grep amd64.deb | cut -d '"' -f 4 | wget -i - && sudo apt install -y ./codium*.deb && rm codium*.deb
sudo git clone https://github.com/zsh-users/zsh-autosuggestions.git /usr/share/zsh-autosuggestions
sudo apt install -y openssh-server && sudo systemctl start ssh && sudo systemctl enable
[ -d "/home/linuxbrew/.linuxbrew/bin" ] && echo 'export PATH=$PATH:/home/linuxbrew/.linuxbrew/bin' >> ~/.zshrc && source ~/.zshrc
