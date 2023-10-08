cd ~/Downloads/

# Download and extract Renpy
wget https://www.renpy.org/dl/8.1.3/renpy-8.1.3-sdk.tar.bz2
sudo tar -xf renpy-8.1.3-sdk.tar.bz2

# Download the game source code
git clone git@github.com:jestemc/eclipse_adventure.git

# Use Renpy to run the game
renpy-8.1.3-sdk/renpy.sh eclipse_adventure
