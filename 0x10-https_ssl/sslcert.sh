#!/bin/bash

echo "Enter the domain name to connect to: "
read add

if [[ $add ]]
then
    # Update your server configuration
    sudo apt-get update -y
    # Install the certbot package
    sudo apt install certbot python3-certbot-nginx -y
    # Allow Nginx Full in firewall
    sudo ufw allow 'Nginx Full'
    # Check the status of the firewall
    sudo ufw status
    # Link certification to the domain name
    sudo certbot --nginx -d $add -d www.$add
    # certificate renewal
    sudo certbot renew --dry-run
else
    echo "Please enter a domain to connect to"
fi
