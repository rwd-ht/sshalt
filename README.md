# sshalt
Simple Netmiko wrapper for misconfigured devices

Meant to deal with devices that give this error.  This error is easily fixed by regenerating a host key on the offending device, but you don't always have the permissions, technical or otherwise, to do that.

    Bad server host key: Invalid key length

# Requirements

    python3.10 or greater
    netmiko

# Usage

    python sshalt.py

Enter credentials when prompted

    CONNECT <ip or hostname>

The prompt will reflect that you're connected.  Any commands after that will be sent to the connected device.  Use the CONNECT command again to connect to a different device.

# Disconnect

Send EOF or type EXIT
