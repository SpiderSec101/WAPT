#!/usr/bin/env python3 

import argparse
import os 
import requests
import re 
import subprocess 
import threading
import json
from datetime import datetime
import glob
import shutil
import importlib.util
from bbot.scanner import Scanner
from pathlib import Path

#--------------------------------------------------------------------------------------------------------------
# Setting up the parser
parser = argparse.ArgumentParser(
    prog="recon_tool.py",
    description="Passive Recon Tool",
    epilog="""
Example:
    python3 recon_tool.py target.com -o ./passive_recon_output

""",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument(
    "target",
    help="Target domain (e.g. example.com)"
)

parser.add_argument(
    "-o",
    "--output-dir",
    default="./output",
    help="Directory where recon results will be saved (default: ./output)"
)

args = parser.parse_args()


# Setting the target domain 
target_domain = (args.target).strip()
# Setting the company name 
target_company = target_domain.split('.')[0]
# Directory path to create the directory structure 
base_dir = args.output_dir
# working directory setup 
working_dir = f"{base_dir}/{target_domain}/tmp"
#--------------------------------------------------------------------------------------------------------------




def tools_installation():
    print("[+] Installing different required tools")
    
    if shutil.which("docker") is None:
        subprocess.run(["apt", "install", "-y", "docker.io"], check=True)

    # Go
    if shutil.which("go") is None:
        subprocess.run(["apt", "install", "-y", "golang-go"], check=True)

    bashrc = f".zshrc"
    go_path = f"/go/bin"
    with open(bashrc, "r") as f:
        content = f.read()
    line = f'export PATH="$PATH:{go_path}"'
    if line not in content:
        with open(bashrc, "a") as f:
            f.write(f"\n{line}\n")


    # Clone repository only if it doesn't already exist
    repo_dir = f"{working_dir}/karma_v2"
    if not os.path.isdir(repo_dir):
        subprocess.run(
            ["git", "clone",
            "https://github.com/Dheerajmadhukar/karma_v2.git",
            repo_dir],
            check=True
        )

    # shosubgo
    if shutil.which("shosubgo") is None:
        subprocess.run(
            ["go", "install", "github.com/incogbyte/shosubgo@latest"],
            check=True
        )


    # httprobe
    if shutil.which("httprobe") is None:
        subprocess.run(
            ["go", "install", "github.com/tomnomnom/httprobe@latest"],
            check=True
        )


    # anew
    if shutil.which("anew") is None:
        subprocess.run(
            ["go", "install", "github.com/tomnomnom/anew@latest"],
            check=True
        )

    # Install mmh3 if not present
    if importlib.util.find_spec("mmh3") is None:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "mmh3"],
            check=True
        )

    # github-endpoints.py
    githubendpoint_url = "https://raw.githubusercontent.com/gwen001/github-search/refs/heads/master/github-endpoints.py"
    try:
        tool_download = requests.get(githubendpoint_url)
        tool_download.raise_for_status()

        with open(f"{working_dir}/github-endpoints.py", "wb") as githubEndpoints_tool:
            githubEndpoints_tool.write(tool_download.content)
    except Exception as e: print(f"[-] Got an error => {e}") 



    # github-subdomains
    if shutil.which("github-subdomains") is None:
        subprocess.run(
            ["go", "install", "github.com/gwen001/github-subdomains@latest"],
            check=True
        )

    # bbot 
    if shutil.which("bbot") is None:
        subprocess.run(
            ["pipx", "install", "bbot"],
            check=True
        )


    # subfinder
    if shutil.which("subfinder") is None:
        subprocess.run(
            ["go", "install", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"],
            check=True
        )

    # resolvers.txt 
    resolver_download = requests.get("https://raw.githubusercontent.com/blechschmidt/massdns/refs/heads/master/lists/resolvers.txt")
    with open(f"{working_dir}/resolvers.txt", "wb") as resolver_file: resolver_file.write(resolver_download.content)


    # subdomains-top1million-110000.txt 
    subtopmillion_download = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/DNS/subdomains-top1million-110000.txt")
    with open(f"{working_dir}/subdomains-top1million-110000.txt", "wb") as subtop_file: subtop_file.write(subtopmillion_download.content)


    # puredns
    if shutil.which("puredns") is None:
        subprocess.run(
            ["go", "install", "github.com/d3mondev/puredns/v2@latest"],
            check=True
        )


    # shuffledns
    if shutil.which("shuffledns") is None:
        subprocess.run(
            ["go", "install", "github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest"],
            check=True
        )

    # dnsgen
    if shutil.which("dnsgen") is None:
        subprocess.run(
            ["pip", "install", "dnsgen"],
            check=True
        )

    if shutil.which("theHarvester") is None:
        subprocess.run(["apt", "install", "-y", "theharvester"], check=True)


    subprocess.run(f"apt install lolcat -y", shell=True)
    subprocess.run("export PATH=$PATH:/go/bin", shell=True)




#creating-directory-structure
def create_dir_structure():
    structure_dirs = ['burp', 'exploit', 'findings', 'assets', 'tmp']
    structure_subdirs = ['IP', 'Domains', 'endpoints', 'secrets']
    os.makedirs(f"{base_dir}/{target_domain}", exist_ok=True)

    for dirs in structure_dirs:
        path = f"{base_dir}/{target_domain}/{dirs}"
        os.makedirs(path, exist_ok=True)

    for subdirs in structure_subdirs:
        path = f"{base_dir}/{target_domain}/assets/{subdirs}"
        os.makedirs(path, exist_ok=True)



#creating-directory-structure
def create_dir_structure():
    print("[+] Creating the directory structure")
    structure_dirs = ['burp', 'exploit', 'findings', 'assets', 'tmp']
    structure_subdirs = ['IP', 'Domains', 'endpoints', 'secrets']
    os.makedirs(f"{base_dir}/{target_domain}", exist_ok=True)

    for dirs in structure_dirs:
        path = f"{base_dir}/{target_domain}/{dirs}"
        os.makedirs(path, exist_ok=True)

    for subdirs in structure_subdirs:
        path = f"{base_dir}/{target_domain}/assets/{subdirs}"
        os.makedirs(path, exist_ok=True)


# Gdorklink.sh 
def github_dorks():
    print("[+] Generating github dorks")
    try:
        gitdork_download = requests.get("https://raw.githubusercontent.com/RobinRana/githubRecon/refs/heads/main/Gdorklinks.sh")
        gitdork_download.raise_for_status()
        with open(f"{working_dir}/Gdorklink.sh", "wb") as gitdork_tool:
            gitdork_tool.write(gitdork_download.content)
    except Exception as e: print(f"[-] Got an error => {e}") 
    gitdork_cmd = f"bash {working_dir}/Gdorklink.sh {target_domain} > {working_dir}/github_dorks.txt"
    subprocess.run(gitdork_cmd, shell=True, text=True)
    print("[+] Go through the Github dorks and other google dorks while I am gathering Subdomains and IPs")


# Gathering ASN from bgp.he.net
def asn_gather():
    print("[+] Gathering ASN")

    url = "https://bgp.he.net/search"
    params = {
        "search[search]": f"{target_company}",
        "commit": "Search"
    }
    headers = {
        "User-Agent": "Mozilla/Firefox"
    }
    response = requests.get(url, params=params, headers=headers)
    asn = re.findall(r'<a href="/AS(\d+)">', response.text)
    try:
        for i in asn:
            with open(f'{working_dir}/asn', 'a') as asn_file: asn_file.write(f'AS{i}\n')
        asn_file.close()
        open(f'{working_dir}/ASN', 'w').write(''.join(sorted(set(open(f"{working_dir}/asn").readlines()))))
        os.remove(f'{working_dir}/asn')
    except Exception as e: print(f"[>] At the time of collecting ASN getting an error as: {e}")
    asn.clear()
    # https://api.bgpview.io/search\?query_term=$company => this link is not working 
    print("[+] Completed gathering ASN from bgp.he.net")



# amass intel 
def enumerate_asn():

    print("[+] Extracting subdomains from ASN")

    def amass_intel(asn):
            asn_results = subprocess.run(f"docker run --rm caffix/amass intel -asn {asn}", shell=True, capture_output=True, text=True)
            asn_output = asn_results.stdout
            with open(f"{base_dir}/{target_domain}/assets/Domains/asn_domains.txt", 'a') as asn_domains: asn_domains.write(asn_output)
            asn_domains.close()

    asn_threads = []
    try:
        for i,j in enumerate(sorted(set(open(f"{working_dir}/ASN")))):
                t = threading.Thread(target=amass_intel, args=(f"{j}",))
                print(f"[+] {i+1}/{len(sorted(set(open(f'{working_dir}/ASN'))))} => {j}")
                asn_threads.append(t)
                t.start()
    except Exception as e: print(f"[+] Getting an error while enumerating domains from ASN as: {e}")

    print(f"[+] Rnning ASN enumeration parallely ;)")

    for t in asn_threads:
        t.join()
    print(f"[+] Done ASN Enumeration")


# crt.sh
def crtsh():   
    print("[+] Attempting for transparency check using crt.sh")
    def crt_requester():
        url = "https://crt.sh/"
        params = {
            "q": target_domain,
            "output": "json"
        }
        headers = {
            "User-Agent": "Mozilla / Firefox"
        }
        res = requests.get(url, params=params, headers=headers)
        try: 
            data = res.json() 
            with open(f'{working_dir}/crt_res.json', 'w') as asd: json.dump(data, asd)
            asd.close()
        except Exception as e:
            print(f"[-] Timeout Error. wait...\n[-] {e}")
            crt_requester()

    crt_requester()

    crt_file_data = open(f'{working_dir}/crt_res.json', 'r').read()
    crt_common = re.findall('"common_name": "(.*?)",', crt_file_data)
    crt_name = re.findall('"name_value": "(.*?)",', crt_file_data)
    crt_together = crt_common + crt_name 
    crt_total = set()

    for i in crt_together:
        j = i.replace('\\n','\n').replace('www.', '').replace('*.', '').strip()
        crt_total.add(j)
    
    crt_domains = open(f'{working_dir}/pre_crt_domains.txt', 'a')
    #crt_apex_file = open(f'{working_dir}/pre_crt_apexdomains.txt', 'a')

    for i in set(crt_total):
        i = i.strip()
        crt_domains.write(i + '\n')
    crt_domains.close()

    with open(f'{working_dir}/pre_crt_domains.txt', 'r') as f:
        lines = f.readlines()
    unique_sorted = sorted(set(line.strip() for line in lines))
    with open(f'{base_dir}/{target_domain}/assets/Domains/crt_domains.txt', 'w') as f:
        for line in unique_sorted:
            f.write(line + '\n')
    print("[+] Done extracting domains from crt.sh")


# shodan enumeration using shosubgo
def shosubgo():
    print("[+] Starting shosubgo tool")
    shosubgo_run = subprocess.run(f"shosubgo -d {target_domain} -s {shodan_api_key}", shell=True, capture_output=True, text=True)
    shosubgo_domains = shosubgo_run.stdout
    with open(f"{base_dir}/{target_domain}/assets/Domains/shosubgo_domains.txt", 'w') as shosubgo_file: shosubgo_file.write(shosubgo_domains)
    print("[+] Successfully extracted subdomains from shodan using shosubgo tool")


# Karma V2 tool based on Shodan
def karma():
    print("[+] Running the shodan based tool Karma_v2")

    with open(f"{working_dir}/karma_v2/.token", "w") as karma_token:
        karma_token.write(shodan_api_key)

    # Run tool if needed
    subprocess.run(f"bash {working_dir}/karma_v2/karma_v2 -d {target_domain} -l -1 -deep --silent 2>/dev/null", shell=True)
    
    today_date = datetime.today().strftime("%Y-%m-%d")
    karma_output_path = f"{working_dir}/karma_v2/output/{target_domain}-{today_date}"

    # 1. Extract IPs from favicons file
    karma_favicons_file = f"{karma_output_path}/favicons_{target_domain}.txt"
    karma_ip_output = f"{base_dir}/{target_domain}/assets/IP/karma.ip"

    with open(karma_favicons_file, "r", errors="ignore") as infile, \
         open(karma_ip_output, "w") as outfile:

        for line in infile:
            try:
                value = line.strip().split("/")[2].split(":")[0]
                outfile.write(value + "\n")
            except Exception as e: print(e)
                
    # 2. Read JSON files
    subprocess.run(f"gzip -d {working_dir}/karma_v2/output/{target_domain}-{today_date}/Collect/*", shell=True)
    karma_json_files = glob.glob(f"{karma_output_path}/Collect/*json")

    karma_ips = set()
    karma_results = set()

    for file in karma_json_files:
        try:
            with open(file, "r", errors="ignore") as f:
                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    try:
                        data = json.loads(line)
                    except Exception as e: print(e)

                    # IPs
                    ip = data.get("ip_str")
                    if ip:
                        karma_ips.add(str(ip).strip())

                    # Domains
                    for field in ["domains", "hostnames"]:
                        values = data.get(field, [])

                        for domain in values:
                            domain = str(domain).strip()
                            if domain:
                                karma_results.add(domain)

        except Exception as e:
            print(e)

    # Append sorted unique IPs
    with open(karma_ip_output, "a") as outfile:
        for ip in sorted(karma_ips):
            outfile.write(ip + "\n")

    # 3. Read main_domain.data
    karma_main_file = f"{karma_output_path}/main_{target_domain}.data"

    with open(karma_main_file, "r", errors="ignore") as infile:
        for line in infile:
            parts = line.strip().split(":")

            if len(parts) >= 5:
                field_5 = parts[4]

                for domain in field_5.split(";"):
                    domain = domain.strip()
                    if domain:
                        karma_results.add(domain)

    # 4. Save all domains
    karma_domain_output = f"{base_dir}/{target_domain}/assets/Domains/karma_domains.txt"

    with open(karma_domain_output, "w") as outfile:
        for domain in sorted(karma_results):
            outfile.write(domain + "\n")

    print("[+] Karma completed successfully")



def cloud():

    cloud_platforms = ['amazon', 'google', 'microsoft', 'oracle', 'digitalocean']
    os.makedirs(f"{working_dir}/cloud", exist_ok=True)
    print("[+] Downloading the cloud resources")
    print("[+] Starting Cloud Enumeration")
    for i in cloud_platforms:

        os.makedirs(f"{working_dir}/cloud/{i}", exist_ok=True)

        cloud_url = f"https://kaeferjaeger.gay/sni-ip-ranges/{i}/ipv4_merged_sni.txt"
        cloud_response = requests.get(cloud_url)

        if cloud_response.status_code == 200:
            with open(f"{working_dir}/cloud/{i}/ipv4_merged_sni.txt", "w") as cloud_file:
                cloud_file.write(cloud_response.text)
            #print("File downloaded successfully.")
        else:
            print(f"Failed to download file. Status code: {cloud_response.status_code}")

    cmd_cloud_ip = rf"""
    cat {working_dir}/cloud/amazon/ipv4_merged_sni.txt {working_dir}/cloud/digitalocean/ipv4_merged_sni.txt {working_dir}/cloud/google/ipv4_merged_sni.txt {working_dir}/cloud/microsoft/ipv4_merged_sni.txt {working_dir}/cloud/oracle/ipv4_merged_sni.txt \
    | grep -Po "(.+\.{target_domain})" \
    | cut -d '-' -f1 \
    | tr -d ':[],' \
    | sed 's/443/\ /g'
    """

    result_cloud_ip = subprocess.run(cmd_cloud_ip, shell=True, capture_output=True, text=True)
    #print(result_cloud_ip.stdout)
    with open(f'{base_dir}/{target_domain}/assets/IP/cloud.ip', 'w') as cloud_ip_file: cloud_ip_file.write(result_cloud_ip.stdout)

    cmd_cloud_subdomains = rf"""
    cat {working_dir}/cloud/amazon/ipv4_merged_sni.txt {working_dir}/cloud/digitalocean/ipv4_merged_sni.txt {working_dir}/cloud/google/ipv4_merged_sni.txt {working_dir}/cloud/microsoft/ipv4_merged_sni.txt {working_dir}/cloud/oracle/ipv4_merged_sni.txt \
    | cut -d '-' -f3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 \
    | sed 's/\ /\n/g' \
    |  grep -Po "(.+\.{target_domain})" \
    | tr -d ',[]' 
    """
    result_cloud_subdomains = subprocess.run(cmd_cloud_subdomains, shell=True, capture_output=True, text=True)
    #print(result_cloud_subdomains.stdout)
    with open(f'{base_dir}/{target_domain}/assets/Domains/cloud_domains.txt', 'w') as cloud_subdomain_file: cloud_subdomain_file.write(result_cloud_subdomains.stdout)

    print("[+] Cloud Enumeration completed successfully")



def github_enumeration(): 
    print("[+] Starting gathering subdomains from Github")

    # github-endpoints.py 
    github_endpoints_tool_run = f"python3 {working_dir}/github-endpoints.py -d {target_domain} -s -r -t {github_api_key}"
    result_github_endpoints = subprocess.run(github_endpoints_tool_run, shell=True, capture_output=True, text=True)
    with open(f"{base_dir}/{target_domain}/assets/endpoints/github_endpoints", "w") as output_github_endpoints: output_github_endpoints.write(result_github_endpoints.stdout)

    # github-subdomains

    github_subdomains_tool_run = f"github-subdomains -d {target_domain} -t {github_api_key} -o {base_dir}/{target_domain}/assets/Domains/github_subdomains.txt"
    subprocess.run(github_subdomains_tool_run, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)

    print("[+] github enumeration done")



def amass_enum():
    print("[+] Starting amass enum ")
    cmd = (
        f"docker run --rm caffix/amass enum -d {target_domain} -timeout 10 > {working_dir}/amass_enum_res; "
        f"cat {working_dir}/amass_enum_res | "
        f"awk '{{print $6}}' | "
        f"grep -Po '[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+' | "
        f"sort -u > {base_dir}/{target_domain}/assets/IP/amass.ip; "
        f"cat {working_dir}/amass_enum_res | "
        f"cut -d ' ' -f1,6 | "
        f"sed 's/ /\\\n/g' | "
        f"grep -Po '(.+\\.{target_domain})' | "
        f"sort -u > {base_dir}/{target_domain}/assets/Domains/amass_subdomains.txt"
    )
    result = subprocess.run(cmd, shell=True, text=True)
    print("[+] amass enum done")



def my_bbot():
    print("[+] starting bbot")
    scan_bbot = Scanner(
        target_domain,
        modules=["otx"],
        config={
        "silent": True,
        "log_level": "CRITICAL"
    }
    )
    seen = set()
    with open(f"{base_dir}/{target_domain}/assets/Domains/bbot_subdomains.txt", "w") as f:
        for event in scan_bbot.start():
            if event.type == "DNS_NAME" and event.data not in seen:
                seen.add(event.data)
                f.write(event.data + "\n")
                f.flush()  # Ensure it's written to disk
    print("[+] BBOT done")


def subfinder():
    print("[+] Running subfinder tool")
    subfinder_cmd = f"subfinder -d {target_domain} -all -o {base_dir}/{target_domain}/assets/Domains/subfinder_subdomains.txt"
    subprocess.run(subfinder_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    print("[+] Done subfinder tool")

def puredns():
    print("[+] Running puredns")
    puredns_cmd = f"puredns bruteforce {working_dir}/subdomains-top1million-110000.txt {target_domain} -r {working_dir}/resolvers.txt -w {base_dir}/{target_domain}/assets/Domains/puredns.txt"
    subprocess.run(puredns_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    print("[+] Done puredns")

def harvester():
    print("[+] Running theHarvester tool")
    harvester_cmd = f"theHarvester -d {target_domain} -q -b all > {base_dir}/{target_domain}/assets/harvester_output.txt"
    subprocess.run(harvester_cmd, shell=True, text=True,  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("[+] Done theHarvester tool")


def dnsgen():
    dnsgen_decision = input("[+] Do you want to run DNSGen? (y/n) => ")
    if dnsgen_decision == 'y':
        print("[+] Running Dnsgen, it will take some times, grab a coffee for yourself :-)")
        dnsgen_cmd = f"cat {base_dir}/{target_domain}/assets/Domains/live_subdomains.txt | dnsgen - | puredns resolve -r {working_dir}/resolvers.txt | sort -u > {base_dir}/{target_domain}/assets/Domains/dnsgen.txt"
        subprocess.run(dnsgen_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    elif dnsgen_decision == 'n': print("[+] Skipped the tool Dnsgen")
    else: 
        print("[+] Not a valid option X")
        dnsgen()


# Threads

def asnEn_crtsh_shosubgo_t():
    print("[+] Running threads:\n [1] amass asn enumeration \n [2] crt.sh enumeration \n [3] running shosubgo")
    asnEn_crt_shosubgo_threads = [
        threading.Thread(target=crtsh),
        threading.Thread(target=shosubgo),
        threading.Thread(target=enumerate_asn)
    ]
    for t in asnEn_crt_shosubgo_threads:
        t.start()
    
    for t in asnEn_crt_shosubgo_threads:
        t.join()
    print("[+] ASN Enumeration, crt.sh, shosubgo thread task is done")



def gitEn_amassEn_subfinder_harvester_t():
    print("[+] Running threads:\n [1] github enumeration \n [2] amass enumeration \n [4] subfinder \n [5] theHarvester")
    five_tools_threads = [
        threading.Thread(target=github_enumeration),
        threading.Thread(target=amass_enum),
        threading.Thread(target=subfinder),
        threading.Thread(target=harvester)
    ]
    for t in five_tools_threads:
        t.start()
    
    for t in five_tools_threads:
        t.join()



def karma_cloud_t():
    print("[+] Running threads:\n [1] Karma_v2 Enumeration \n [2] Cloud Enumeration")
    karma_cloud_threads = [
        threading.Thread(target=karma),
        threading.Thread(target=cloud)
    ]
    for t in karma_cloud_threads:
        t.start()
    
    for t in karma_cloud_threads:
        t.join()
    print("[+] Karma_v2 and Cloud Enumeration thread task is done ")


def domain_type_separator():

    os.system(f"cat {base_dir}/{target_domain}/assets/Domains/* | sort -u > {base_dir}/{target_domain}/assets/Domains/all.txt")
    all_apex_file = open(f"{base_dir}/{target_domain}/assets/Domains/apexdomains.txt", 'a')
    all_sub_file = open(f"{base_dir}/{target_domain}/assets/Domains/subdomains.txt", 'a')
    with open(f"{base_dir}/{target_domain}/assets/Domains/all.txt", "r") as f:
        for i in f:
            i = i.strip()
            if i == target_domain or i.endswith("." + target_domain):
                all_sub_file.write(i + '\n')
        else:
            all_apex_file.write(i + '\n')
    all_apex_file.close()
    all_sub_file.close()
    total_sub = subprocess.run(f"wc -l {base_dir}/{target_domain}/assets/Domains/subdomains.txt", shell=True, capture_output=True, text=True)
    print("[+] Total numbers of live subdomains found => ", total_sub.stdout)


def live_domains_finder(domain_type):
        if domain_type == 'sub':
            print("[+] Extracting live subdomains")
            httpx_run_1 = subprocess.run(f"/go/bin/httpx -l {base_dir}/{target_domain}/assets/Domains/subdomains.txt -silent", shell=True, capture_output=True, text=True)
            live_subdomains = httpx_run_1.stdout
            with open(f"{base_dir}/{target_domain}/assets/Domains/live_subdomains.txt", 'w') as live_sub: live_sub.write(live_subdomains)
            live_sub.close()
            print("[+] Done")
            total_live_sub = subprocess.run(f"wc -l {base_dir}/{target_domain}/assets/Domains/live_subdomains.txt", shell=True, capture_output=True, text=True)
            print("[+] Total numbers of live subdomains found => ", total_live_sub.stdout)

        if domain_type == 'apex':
            print("[+] Extracting live apexdomains")
            httpx_run_2 = subprocess.run(f"/go/bin/httpx -l {base_dir}/{target_domain}/assets/Domains/apexdomains.txt -silent", shell=True, capture_output=True, text=True)
            live_apexdomains = httpx_run_2.stdout
            with open(f"{base_dir}/{target_domain}/assets/Domains/live_apexdomains.txt", 'w') as live_apex: live_apex.write(live_apexdomains)
            live_apex.close()
            print("[+] Done")



def take_ss():
    ss_question = input("Do you want to take screenshots of the live subdomains? (y/n) => ")
    if ss_question.lower() == 'y':
        if Path(f"{working_dir}/resume.cfg").is_file():
            #print("File exists")
            ss_cmd = f"/go/bin/httpx -l {base_dir}/{target_domain}/assets/Domains/live_subdomains.txt -ss -system-chrome -srd {base_dir}/{target_domain}/assets/ss -silent -threads 1 -timeout 20 -retries 1 -no-screenshot-full-page -resume"
        else:
            ss_cmd = f"/go/bin/httpx -l {base_dir}/{target_domain}/assets/Domains/live_subdomains.txt -ss -system-chrome -srd {base_dir}/{target_domain}/assets/ss -silent -threads 1 -timeout 20 -retries 1 -no-screenshot-full-page"

        print("[+] Started taking screenshots")    
        subprocess.run(ss_cmd, shell=True, text=True)
    elif ss_question.lower() == 'n':
        print("[+] Not taking scrrenshots...skipped")
    else : 
        print("[+] Invalid option (-_-) ")
        take_ss()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tool_file_download()
create_dir_structure()
#~~~~~~~~~~~~~~~~~ Secrets Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
try :
    config_file_read = open(f'config.yaml', 'r')
    content = config_file_read.read()
    github_api_key = re.findall(r'spyse.*"(.+)"', content)[0]
    shodan_api_key = re.findall(r'shodan.*"(.+)"', content)[0]
    print("shodan_api_key = ", shodan_api_key)
except Exception as e:
    print("[-] config file not found => ", e)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

github_dorks()
asn_gather()

asnEn_crtsh_shosubgo_t()

karma_cloud_t()

gitEn_amassEn_subfinder_harvester_t() 

puredns()

domain_type_separator()
live_domains_finder('sub')


print("[+] Dnsgen: https://github.com/AlephNullSK/dnsgen \n[+] DNSGen is a powerful and flexible DNS name permutation tool designed for security researchers and penetration testers. It generates intelligent domain name variations to assist in subdomain discovery and security assessments.")
dnsgen()


take_ss()



