# Automated Fedora Program Installation Script :robot:
This script is designed to automate the installation of essential programs on Fedora. It includes the installation of Git, Node.js, and the NvChad Neovim configuration.

Programs to be Installed:
Git

```bash
sudo dnf install git -y
``` 
Node.js

```bash
sudo dnf install -y https://rpm.nodesource.com/pub_18.x/nodistro/repo/nodesource-release-nodistro-1.noarch.rpm; 
sudo dnf install -y nodejs --setopt=nodesource-nodejs.module_hotfixes=1
```
NvChad (Neovim configuration)

```bash
 git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim
```
Usage:
Run the script in a terminal.

```bash
python script_name.py
```
The script will prompt you with the question: **"Ok, do you want to start with the installation of programs on Fedora? (y/n):"**

If you choose **'y'** (yes), the script will perform the following tasks:

Update the system: sudo dnf -y update
Upgrade the system: sudo dnf -y upgrade
Install the specified programs.
If you choose 'n' (no), the installation will be aborted.

Notes:
Ensure that you have the necessary permissions to run commands with sudo.
The script uses the subprocess module to execute system commands.
In case of any errors during the update, upgrade, or installation processes, the script will provide appropriate error messages.

:warning: Disclaimer:
This script assumes you are running it on a Fedora system. Use it at your own risk, and review the commands in the script to ensure compatibility with your system.