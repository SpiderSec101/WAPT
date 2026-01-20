#!/bin/bash

#~~~~~~~~ Set a color output ~~~~~~~~~~~

color='\033[38;5;83m'
color()     { echo -e "${color}$*${RESET}"; }
color
#~~~~~~~~~~ Setup the target details ~~~~~~~~~~~~~~~~~

echo "[-]Example Usage: bash recon.sh tesla.com"
company=$(echo $1|cut -d '.' -f1)

#~~~~~~~~~~~~ Directory Structure ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>

mkdir $1
mkdir -p $1/{analysis,burp,assets/{domain,ip,ss,dns_records,others},tmp}
touch $1/tracker.md
#~~~~~~~~~~~~ config.ini set-up ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
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
echo "[-] Use the config file for different tools and place it as required, E.G. => ~/.config/amass/config.ini for amass"
echo "Update the API key values in config.ini" | lolcat
read -p "Press Enter if you have updated the config.ini file" asdasdasd

#~~~~~~~~~~~ Current Working Directory Set-up ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cd ./tmp
echo "Current Working Directory => ${pwd}" 
#~~~~~~~~~~~~~~~ Set up API keys ~~~~~~~~~~~~~~~~~~~~

shodan_api_key=$(cat ../config.ini | grep 'shodan' | grep -Po '"(.+)"' | tr -d '"')
github_api_key=$(cat ../config.ini | grep 'spyse' | grep -Po '"(.+)"' | tr -d '"')
read -p "Enter the wordlist location for subdomain bruteforcing : " sub_wordlist
#~~~~~~~~~~~ Listing all the tools ~~~~~~~~~~~~~~
echo "[*] Gdorklink.sh"
echo "[*] crunchbase.com"
echo "[*] bgp.he.net"
echo "[*] amass intel"
echo "[*] crt.sh"
echo "[*] Shosubgo"
echo "[*] kaeferjaeger.gay"
echo "[*] Karma_V2"
echo "[*] github-subdomains"
echo "[*] amass enum"
echo "[*] Subfinder"
echo "[*] BBOT"
echo "[*] puredns"
echo "[*] shuffledns"
echo "[*] httpx"
echo "[*] dnsgen"
echo "[*] dnsrecon"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Information Gathering (Passive) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~ Gdorklink.sh ~~~~~~~~~~~~~~~

echo "[*] Generating dorks for Github searching"
wget https://gist.githubusercontent.com/jhaddix/1fb7ab2409ab579178d2a79959909b33/raw/e9fea4c0f6982546d90d241bc3e19627a7083e5e/Gdorklinks.sh
bash Gdorklink.sh $1
echo "[*] Go through the dorks "
#~~~~~~~~~~~~ Acquitions ~~~~~~~~~~~~~~~
echo "[*]Find the Acquitions from crunchbase.com and chatGPT. The apex domains"
#~~~~~~~~~~~~ ASN ~~~~~~~~~~~~~~~
echo "[*]Finding the ASN from https://bgp.he.net" 
curl -sL https://bgp.he.net/search\?search%5Bsearch%5D=$company\&commit=Search -H 'User-Agent: Mozilla/Firefox' | grep -Po 'AS[0-9]*' | grep -vw 'AS' | sort -u > asn
curl -s https://api.bgpview.io/search\?query_term=$company | jq -r | grep 'asn'| cut -d ':' -f2 | tr -d ',[]' | sed -e 's/\ /AS/g'| grep -Po '(AS[0-9]+)' >> asn
cat asn | sort -u > ASN
rm asn 
echo "done" 

#~~~~~~~~~~~~ amass intel ~~~~~~~~~~~~~~~
echo "[*]Extracting domains, ips from ASN using amass intel" 
#for asn in $(cat ASN | tr -d 'AS');do amass intel -asn "$asn" >> asn.results;done
k=0;for asn in $(cat ASN | tr -d 'AS');do echo "$k/$(wc -l ASN) => AS$asn"; sudo docker run --rm -it caffix/amass intel -asn "$asn" >> asn.assets ;k=$((k+1));done
cat asn.assets | grep -vF ".$company." | sort -u > ../assets/domain/asn.apex-domains
cat asn.assets | grep -F ".$company." | sort -u > ../assets/domain/asn.sub-domains
echo "[-]Finally Done ;)" 
#~~~~~~~~~~~~ crt.sh ~~~~~~~~~~~~~~~
echo "[*]Enumerating domains from crt.sh (Certificate Transparency Logs) " 
curl -sL http://crt.sh\?q=$1\&output=json -H 'User-Agent: Mozilla/Firefox' | jq . | grep -F 'common_name' | cut -d ':' -f2 | tr -d ',"' | grep -F ".$company." | sort -u > ../assets/domain/crt.sub-domains
curl -sL http://crt.sh\?q=$1\&output=json -H 'User-Agent: Mozilla/Firefox' | jq . | grep -F 'common_name' | cut -d ':' -f2 | tr -d ',"' | grep -vF ".$company." | sort -u > ../assets/domain/crt.apex-domains
echo "[-]Completed"

#~~~~~~~~~~~~ Shosubgo ~~~~~~~~~~~~~~~
echo "[*]Running shosubgo to extract subdomains  using Shodan"
shosubgo -d $1 -s $shodan_api_key > ../assets/domain/shodan.sub-domains
#~~~~~~~~~~~~ Cloud ~~~~~~~~~~~~~~~
echo "[*]Extracting domains, ips from cloud"
platforms=(amazon google microsoft digitalocean oracle)
mkdir cloud
(for i in "${platforms[@]}"; do mkdir cloud/$i; cd cloud/$i; wget -q https://kaeferjaeger.gay/sni-ip-ranges/$i/ipv4_merged_sni.txt; cd ../../ ;done;cat cloud/amazon/ipv4_merged_sni.txt cloud/digitalocean/ipv4_merged_sni.txt cloud/google/ipv4_merged_sni.txt cloud/microsoft/ipv4_merged_sni.txt cloud/oracle/ipv4_merged_sni.txt | grep -Po "(.+\.$1)" | cut -d '-' -f1 | tr -d ':[],' | sed 's/443/\ /g' > ../assets/ip/cloud.ips ;cat cloud/amazon/ipv4_merged_sni.txt cloud/digitalocean/ipv4_merged_sni.txt cloud/google/ipv4_merged_sni.txt cloud/microsoft/ipv4_merged_sni.txt cloud/oracle/ipv4_merged_sni.txt | cut -d '-' -f3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 | sed 's/\ /\n/g' |  grep -Po "(.+\.$1)" | tr -d ',[]' | sort -u > ../assets/domain/cloud.sub-domains; echo "[-] Completed Cloud Enumeration") &
echo "Running process in background"
echo "PID ==> $!" | lolcat
#~~~~~~~~~~~~ Karma ~~~~~~~~~~~~~~~
echo "[*] Runing Karma_v2  ........"
read -p "Do you want to download karma_v2 ? (y/n) => " karma_q
if [ "$karma_q" == "y" ]; then
	git clone https://github.com/Dheerajmadhukar/karma_v2.git
echo "$shodan_api_key" > ./karma_v2/.token
bash ./karma_v2/karma_v2 -d $1 -l -1 -deep
mv ./karma_v2/output .
cat ./output/favicons_$1.txt | cut -d '/' -f3 | cut -d ':' -f1 > ../assets/ip/karma.ip
cat ./output/main_$1.data | cut -d ':' -f5 | tr ';' '\n' | sort -u| grep -F ".$company." > ../assets/domain/karma.sub-domains
cat ./output/main_$1.data | cut -d ':' -f5 | tr ';' '\n' | sort -u| grep -vF ".$company." > ../assets/domain/karma.apex-domains
# Inside output/company.com/Collect
gzip  -d ./output/$1/Collect/*
cat ./output/$1/Collect/*json | jq -r .domains | tr -d '",[] ' | sort -u | grep -vF ".$company." >> ../assets/domain/karma.apex-domains
cat ./output/$1/Collect/*json | jq -r .domains | tr -d '",[] ' | sort -u | grep -F ".$company." >> ../assets/domain/karma.sub-domains
cat ./output/$1/Collect/*json | jq -r .hostnames | tr -d '",[] ' | sort -u | grep -F ".$company." >> ../assets/domain/karma.sub-domains
cat ./output/$1/Collect/*json | jq -r .hostnames | tr -d '",[] ' | sort -u | grep -vF ".$company." >> ../assets/domain/karma.apex-domains
cat ./output/$1/Collect/*json | jq -r .ip_str | sort -u >> ../assets/ip/karma.ip 

#~~~~~~~~~~~~ github-subdomains ~~~~~~~~~~~~~~~
echo "[*]Gathering domains from github"
echo "[-]Check out other github enumerating tools here => https://glc.st/posts/github-tools-collection/"
github-subdomains -d $1 -t $github_sub_domains -o ../assets/domain/github.sub-domains
#~~~~~~~~~~~~ amass scanning ~~~~~~~~~~~~~~~	
echo "[*]Running amass scan with amass scanning "
echo "[-]Setup config file (https://www.hahwul.com/blog/2020/amass-go-deep-in-the-sea-with-free-apis/)"
echo Running scan on $1
read -p "[-]Enter to continue: "
#amass enum -d $1 > amass.info
(sudo docker run -v /home/spider/.config/amass/:/root/.config/amass/ caffix/amass enum -d $1 > amass.info; cat amass.info | awk '{print $6}' | grep -Po '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sort -u > ../assets/ip/amass.ip; cat amass.info | grep -F 'aaaa_record' | awk '{print $6}' | sort -u > ../assets/ip/amass.ipv6; cat amass.info | cut -d ' ' -f1,6 | sed 's/\ /\n/g' | grep -Po "(.+\.$1)"| sort -u > ../assets/domain/amass.sub-domains; cat amass.info | grep -F 'cname_record' > ../assets/dns_records/cname_records; echo "Done amass scanning") &
echo  "PID of the process => $!"
# a_record aaaa_record contains cname_record
#~~~~~~~~~~~~ subfinder ~~~~~~~~~~~~~~~
echo "[*]Subfinder (https://github.com/projectdiscovery/subfinder)"
read "[?]Have you set-up the config file ? (Enter to continue): "
subfinder -d $1 -all -o ../assets/domain/subfinder.sub-domains
#~~~~~~~~~~~~ bbot ~~~~~~~~~~~~~~~
echo "[*]Running BBOT (https://github.com/blacklanternsecurity/bbot)"
echo "[?]Have you set the config file for bbot ? (Enter to continue) "
bbot -m otx -t $1 -p subdomain-enum > bbot.info
cat bbot.info | grep -Po "[a-zA-Z0-9]+\.$1" | sort -u > ../assets/domain/bbot.sub-domains
cat bbot.info | grep 'CNAME' | awk '{print $3 " ==> " $2}' > ../assets/dns_records/cname
#~~~~~~~~~~~~ puredns ~~~~~~~~~~~~~~~
echo "[*] Downloading resolvers.txt"
wget https://raw.githubusercontent.com/blechschmidt/massdns/refs/heads/master/lists/resolvers.txt
echo "[*] Completed "
# raft-all.txt
#~~~~~~~~~~~~ shuffledns ~~~~~~~~~~~~~~~
echo "[*] Now running shuffledns"
shuffledns -up
shuffledns -d $1 -w $sub_wordlist -r resolvers.txt -mode bruteforce -o ../assets/domain/shuffledns.sub-domains
echo "[*] Completed"
#~~~~~~~~~~~~ gathering all domains ~~~~~~~~~~~~~~~
cat ../assets/domain/*sub-domains | sort -u  > ../assets/domain/all.subdomains
cat all.subdomains | grep -Po '^[0-9]+.*' > ../assets/domain/all1.subdomains
cat all.subdomains | grep -vP '^[0-9]+.*' > ../assets/domain/all2.subdomains

cat ../assets/domain/*apex-domains | sort -u  > ../assets/domain/all.apexdomains

#~~~~~~~~~~~~ live subdomains ~~~~~~~~~~~~~~~
httpx -l all2.subdomains -silent > ../assets/domain/live.subdomains
#httpx -l all1.subdomains -silent >> ../assets/domain/live.subdomains

#~~~~~~~~~~~~ permuted scanning ~~~~~~~~~~~~~~~
cat ../assets/domain/live.subdomains | dnsgen - | puredns resolve -r resolvers.txt > ../assets/domain/dnsgen.sub-domains

#~~~~~~~~~~~~~~~ final list of subdomains ~~~~~~~~~~~~~~~
cat ../assets/domain/live.subdomains ../assets/domain/dnsgen.sub-domains | tr -d '/' | cut -d ':' -f2 | sort -u > final.subdomains

#~~~~~~~~~~~~~~~ DNS Info ~~~~~~~~~~~~~~~
#Only running one tool as it is an active recon
dnsrecon -d $1 > ../assets/dns_records/out.dnsrecon

#~~~~~~~~~~~~~~~ Taking ss ~~~~~~~~~~~~~~~
cat ../assets/domain/final.subdomains | cut -d ':' -f2 | tr -d '/ ' | sort -u | awk '{print "http://"$0 "\n" "https://"$0}' > ./ss.subdomains
echo "[*] Started taking scresnshots"
if [ -f resume.cfg ]; then 
	httpx -l ss.sub-domains -ss -system-chrome -srd ../assets/ss -threads 1 -timeout 20 -retries 1 -no-screenshot-full-page -resume
else
	httpx -l ss.sub-domains -ss -system-chrome -srd ../assets/ss -threads 1 -timeout 20 -retries 1 -no-screenshot-full-page

