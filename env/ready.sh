cd ~
apt update -y && apt install zsh tmux -y
which zsh
chsh -s `which zsh`
wget https://raw.githubusercontent.com/pswalia2u/Pentest_Commands/master/.zshrc
wget https://raw.githubusercontent.com/pswalia2u/Pentest_Commands/master/env/.tmux.conf