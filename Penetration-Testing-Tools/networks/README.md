## Networks Penetration Testing related scripts, tools and Cheatsheets

- **`CDPFlooder.py`** - CDP Flooding tool, intended to take out entire segment switched by some old Cisco switches, vulnerable to Denial of Service after receiving big amount of invalid CDP packets.

The effect will be similar to:
```
SW2960#show cdp traffic 
CDP counters :
	Total packets output: 361, Input: 11824
	Hdr syntax: 0, Chksum error: 0, Encaps failed: 0
	No memory: 0, Invalid packet: 461858, Fragmented: 0
	CDP version 1 advertisements output: 9, Input: 178
	CDP version 2 advertisements output: 352, Input: 76
```

- **`dtpscan.py`** - DTP Scanner - simple script trying to determine type of configured switchport and DTP negotation mode in order to assist in VLAN Hopping attacks. ([gist]())

- **`host-scanner-via-udp.py`** - Running Hosts scanner leveraging ICMP Destination Unreachable response upon UDP closed port packet. ([gist]())

- **`HSRPFlooder.py`** - Proof of concept _HSRP Coup State: Active_ flooder, trying to provoke Denial of Service within LAN segment due to tunnelling packets to the non-existent gateway that won active-router election. Not working stabily at the moment.

- **`iis_webdav_upload.py`** - Microsoft IIS WebDAV Write Code Execution exploit (based on Metasploit HDM's <iis_webdav_upload_asp> implementation). ([gist]())

- **`networkConfigurationCredentialsExtract.py`** - Network-configuration Credentials extraction script - intended to sweep input configuration file and extract keys, hashes, passwords. ([gist]())

- **`nmap-grep-to-table.sh`** - Script converting nmap's greppable output (-oG) into a printable per-host tables. ([gist]())

- **`nmap-scan-all.sh`** - Simple script to launch nmap scans against given target, using specific options and scripts set.

- **`pingsweep.py`** - Quick Python Scapy-based ping-sweeper. ([gist]())

- **`sshbrute.py`** - ripped out from Violent Python - by TJ O'Connor. ([gist]())

- **`smb-credential-leak.html`** - SMB Credentials leakage by MSEdge as presented in Browser Security White Paper, X41 D-Sec GmbH. ([gist]())

- **`smtpdowngrade.rb`** - Bettercap TCP Proxy SMTP Downgrade module - prevents the SMTP client from sending "STARTTLS" and returns "454 TLS Not available..." to the client. ([gist]())

- **`smtpvrfy.py`** - SMTP VRFY python tool intended to check whether SMTP server is leaking usernames. ([gist]())

- **`wpa2-enterprise-utils`** - Couple of scripts that became needed/useful during **WPA2-Enterprise** penetration-testing assignment.

- **`VLANHopperDTP.py`** - VLAN Hopping via DTP Trunk (Switch) Spoofing exploit - script automating full VLAN Hopping attack, from DTP detection to VLAN Hop with DHCP lease request ([gist]())

    Sample output:

```
$ ./VLANHopperDTP.py --help

        :: VLAN Hopping via DTP Trunk negotiation 
        Performs VLAN Hopping via negotiated DTP Trunk / Switch Spoofing technique
        Mariusz B. / mgeeky, '18
        v0.3

usage: ./VLANHopperDTP.py [options]

optional arguments:
  -h, --help            show this help message and exit
  -i DEV, --interface DEV
                        Select interface on which to operate.
  -e CMD, --execute CMD
                        Launch specified command after hopping to new VLAN.
                        One can use one of following placeholders in command:
                        %IFACE (choosen interface), %IP (acquired IP), %NET
                        (net address), %HWADDR (MAC), %GW (gateway), %MASK
                        (full mask), %CIDR (short mask). For instance: -e
                        "arp-scan -I %IFACE %NET%CIDR". May be repeated for
                        more commands. The command will be launched
                        SYNCHRONOUSLY, meaning - one have to append "&" at the
                        end to make the script go along.
  -E CMD, --exit-execute CMD
                        Launch specified command at the end of this script
                        (during cleanup phase).
  -m HWADDR, --mac-address HWADDR
                        Changes MAC address of the interface before and after
                        attack.
  -f, --force           Attempt VLAN Hopping even if DTP was not detected
                        (like in Nonegotiate situation).
  -a, --analyse         Analyse mode: do not create subinterfaces, don't ask
                        for DHCP leases.
  -v, --verbose         Display verbose output.
  -d, --debug           Display debug output.



$ sudo ./VLANHopperDTP.py -i enp5s0f1

        :: VLAN Hopping via DTP Trunk negotiation 
        Performs VLAN Hopping via negotiated DTP Trunk / Switch Spoofing technique
        Mariusz B. / mgeeky, '18
        v0.2

[+] VLAN Hopping IS possible.
[>] After Hopping to other VLANs - leave this program running to maintain connections.
[>] Discovering new VLANs...
==> VLAN discovered: 10
==> VLAN discovered: 20
==> VLAN discovered: 30
==> VLAN discovered: 99
[+] Hopped to VLAN 10.: 172.16.10.10
[+] Hopped to VLAN 20.: 172.16.20.10
[+] Hopped to VLAN 30.: 172.16.30.11
[+] Hopped to VLAN 99.: 172.16.99.10
```
