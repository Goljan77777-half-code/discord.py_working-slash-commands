#!/bin/bash

read -p "Do you want to continue? (y/n): " response

if [[ $response =~ ^[Yy]$ ]]; then
    echo "You selected 'yes'. Continuing..."
    sudo apt update
    sudo apt install python3.9
    sudo apt install pip
    sudo python3 -m pip install -U discord.py;
else
    echo "You selected 'no'. Exiting..."
fi
