#!/bin/bash

#~~~~~~~~~~ Setup the target details ~~~~~~~~~~~~~~~~~

echo "[-] Example Usage: bash setup.sh tesla.com"
company=$(echo $1|cut -d '.' -f1)

#~~~~~~~~~~~~ Directory Structure ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

mkdir $1
mkdir -p $1/{analysis,burp,assets/{domain,ip,ss,dns_records,others},tmp}
touch $1/tracker.md

#~~~~~~~~~~~~ config ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
cd $1
cat > "config.ini" <<'EOF'
[datasources]
; Add your API keys under the relevant sections
; Example: 

; OpenAI
openai = 

; Chaos
virustotal =

; Shodan
shodan = 

; Github
spyse = 

; Facebook
securitytrails = 

; PassiveTotal
;censys = your_PassiveTotal_api_secret

; Twitter
apikey = 
secret = 
EOF

echo "[-] Created a config.ini file"
echo "[-] Use the config file for different tools and place it as required, e.g. => ~/.config/amass/config.ini for amass" | lolcat
echo "[-] Directory structure created successfully, as "; tree
echo "[*] Place the recon.sh inside the $1/tmp and run " | lolcat

