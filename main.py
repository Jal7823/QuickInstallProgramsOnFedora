import subprocess

programs = {
    'git': 'sudo dnf install git -y',
    'nodejs': (
        'sudo dnf install -y '
        'https://rpm.nodesource.com/pub_18.x/nodistro/repo/nodesource-release-nodistro-1.noarch.rpm; '
        'sudo dnf install -y nodejs --setopt=nodesource-nodejs.module_hotfixes=1'
    ),
    'nvichad': 'git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim',

}


def update_and_upgrade():
    try:
        subprocess.run(['sudo', 'dnf', '-y', 'update'], check=True)
        subprocess.run(['sudo', 'dnf', '-y', 'upgrade'], check=True)
        print('Upgrade successfully')
    except subprocess.CalledProcessError as e:
        raise Exception(f'Error during update/upgrade: {e}')


def install_programs():
    for program, command in programs.items():
        try:
            subprocess.run(command, shell=True, check=True)
            print(f'{program} installed successfully')
        except subprocess.CalledProcessError as e:
            print(f'Error installing {program}: {e}')


if __name__ == '__main__':
    start = input('Ok, do you want to start with the installation of programs on Fedora? (y/n): ')
    if start.lower() == 'y':
        update_and_upgrade()
        install_programs()
    else:
        print('Installation aborted.')
