- ### [Wordlists]()
- ### [Subdomain Bruteforcing]()
- [ ] sublister
- [ ] dnsenum
- [ ] ffuf
- [ ] gobuster
- ### [Directory Bruteforcing]()
- [ ] Dirsearch
- [ ] ffuf
- [ ] gobuster
- [ ] feroxbuster
- ### [Parameter Fuzzing]()
- [ ] Arjun
- [ ] x8
- ### [Crawlers]()
- [ ] gospider
- [ ] hakrawler
- [ ] katana
- ### [JS Scraping]()
- [ ] Linkfinder
- [ ] SubDomainizer
- [ ] Burp GAP Extension
- [ ] JS Miner
- [ ] JS Finder
- [ ] Secret Finder
- ### [Paths]()
- [ ] Known Paths
- [ ] APK Leaks 
- ### [Wayback Archive]()
- [ ] waymore
- [ ] xnLinkFinder
- ### [Network Scan]()
- [ ] naabu
- [ ] nmap
- [ ] masscan
- [ ] dnsmasscan
- ### [Automated Analysis]()
- [ ] nuclei
- [ ] retirejs
- [ ] opengrep
- [ ] metasec.js
- [ ] Burpsuite Active Scan

- ### [Manual Analysis]()
- [ ] Manual Crawling 
- [ ] Questions
- [ ] Modules and Submodules
- [ ] Testcases

--- 

### Wordlists
- [ ] Subdomain Enumeration
  - [Jhaddix-all.tx](https://gist.githubusercontent.com/jhaddix/86a06c5dc309d08580a018c66354a056/raw/96f4e51d96b2203f19f6381c8c545b278eaa0837/all.txt)
- [ ] Directory and Subdomains
  - Assetnote Wordlists
  - SecLists
  - [fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts)
- [ ] Fuzzing
  - Paloadallthethings Intruder
  - SecLists
- [ ] API Resources
  - SecLists
  - [api_wordlist](https://github.com/chrislockard/api_wordlist)
  - [graphql_wordlist](https://github.com/Escape-Technologies/graphql-wordlist)
  - [A List of  Common Endpoints and Objects](https://gist.github.com/yassineaboukir/8e12adefbd505ef704674ad6ad48743d)
- [ ] Parameters
  - SecLists
  - [fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts)


### Subdomain Bruteforcing 

- [ ] sublist3r
    ```bash
    sudo apt install sublist3r 
    sublist3r -b -d tesla.com -o domains.txt
    ```
    
- [ ] dnsenum
    ```bash
    dnsenum --enum example.com -f /usr/share/wordlists/dirb/wordlists.txt -r
    ```
    - `dnsenum --enum example.com` ⇒ here we specify the domain name and use a tuning option `enum` that is used to gather as much information as the tool can.
    - `-f`  Used to specify the word list
    - `-r` is used for recursive option, if it discovers a subdomain like `auth.example.com` it will try to find the subdomain of the extracted subdomain

- [ ] ffuf
    ```bash
    ffuf -u https://example.com -H 'HOST: FUZZ.example.com' -w /usr/share/wordlists/.....
    ```
    
- [ ] gobuster
    ```bash
    gobuster vhost -w /usr/share/wordlists/SecLists/... -u https://example.com -t 10
    ```
### Directory Bruteforcing 

- [ ] ffuf
    
    ```bash
    ffuf -w /path/to/wordlists:FUZZ -u http://target.com/FUZZ -e .php,.js,.html -H "Cookie: session-cookie-here" -mc all
    ```
  
- [ ] gobuster
    
    ```bash
    gobuster dir -w /usr/share... -u http://evil.com -x .php,.txt -H "User-Agent: ..." -s 200-500 -hl 162
    ```
    
- [ ] dirsearch
    
    ```bash
    dirsearch -u http://target.com -i 200-500 -x 404 -e php,txt -r -H "Cookie: cookie-here" --exclude-sizes=162
    ```
    
- [ ] feroxbuster
    
    ```bash
    feroxbuster -u http://target.com -w <wordlist> -x pdf,php,txt -r -d 2 -H "Cookie: cookie-here"
    ```
    
### Parameter Fuzzing

- [ ] Arjun
    
    - Arjun can find query parameters for URL endpoints.
    
    - [https://github.com/s0md3v/Arjun](https://github.com/s0md3v/Arjun)
    
    ```bash
    arjun -u http://example.com/user/profile --headers "Cookie: cookie-here" -t 100 -d 1000
    ```
    
    - `-t` for threads
    - `-d` for delay between two requests
    - `-i` to scan all the endpoints from a list of targets
  
- [ ] x8
    
    - [https://github.com/Sh1Yo/x8](https://github.com/Sh1Yo/x8)
    
    ```bash
    x8 -u http://url1.com http://url2.com -w <wordlist> -X GET -H "Cookie: cookie-here" -d 1000
    ```

    - `-d` is used for delay between two requests


### Crawlers

- [ ] gospider
    
    ```bash
    gospider -s https://linked.com -w -d 0
    ```
    - `-d` is used for the depth control, set to 0 for infinite recurse and default set to 1
    - `-w` is for adding the subdomains inscope
      
- [ ] hakrawler

    ```bash
    echo https://target.com | hakrawler -subs -d 3
    ```

- [ ] katana

    - [https://github.com/projectdiscovery/katana](https://github.com/projectdiscovery/katana)
    
    ```bash
    go install github.com/projectdiscovery/katana/cmd/katana@latest
    ```

    ```bash
    katana -u https://tesla.com -H "header" -d 10 -jsl -jc 
    ```
    
    - `-jsl` is used for  Javascript link extaction
    - `-jc` is used to enable the Javasdcript crawling



### JS Scraping 

- [ ] LinkFinder

    - [https://github.com/GerbenJavado/LinkFinder](https://github.com/GerbenJavado/LinkFinder)
    
    ```bash
    python3 linkfidner.py -i https://linkedin.com -d -c "sessionid=oe79rcyno734t8y7"
    ```

- [ ] Subdomainizer

    - [https://github.com/nsonaniya2010/SubDomainizer](https://github.com/nsonaniya2010/SubDomainizer)
    
    ```bash
    python3 SubDomainizer.py -h
    python3 SubDomainizer.py -u https://linkedin.com 
    ```

    - To use it with the github token
    
    ```bash
    python3 SubDomainizer.py -u https://linkedin.com -o outputfile.txt -gt github_token_here -g
    ```

    - To use with cookie
    
    ```bash
    python3 SubDomainizer.py -u https://www.example.com -c "test=1; test=2"
    ```

- [ ] Burp Gap

    - This Burpsuite Extension is used to gather endpoints, URLs, parameters, names
    
    - [https://github.com/xnl-h4ck3r/GAP-Burp-Extension](https://github.com/xnl-h4ck3r/GAP-Burp-Extension)

- [ ] JSMiner

    - This Burp Extension is used to extract hard coded info from the JS it self

- [ ] JS Finder
    
    - [https://github.com/kacakb/jsfinder?tab=readme-ov-file](https://github.com/kacakb/jsfinder?tab=readme-ov-file)
        
    - Reading URLs from the JS files
        
    ```bash
    echo http://target.com | jsfinder -read -s -o out.txt 
    ```
    
    ```bash
    jsfinder -l list.txt -read -s -o out.txt
    ```
    
- [ ] Secret Finder
    
    - [https://github.com/m4ll0k/SecretFinder](https://github.com/m4ll0k/SecretFinder)
        
    ```bash
    python3 SecretFinder.py -i http://target.com -e -H "Cookie: cookie-here" -o cli
    ```
    
    - `-o` used to specify the output method
    - cli
    - results.html


### Paths 

- [ ] Known Paths
    - If the software is available then one can install it and extract the known paths using the Daniel Miller’s **`Source2URL`** bash script
    
    [https://github.com/danielmiessler/Source2URL/blob/master/Source2URL](https://github.com/danielmiessler/Source2URL/blob/master/Source2URL)
    
    - It is a bash script that helps to extract the URLs from a source code directory
    - It then makes HTTP requests to each path via a configured proxy (BurpSuite)
    
    ```bash
    ./Source2URL ~/downloads/wordpress wordpress 127.0.0.1:8080 example.com
    ```

- [ ] APK Leaks

    - [https://github.com/dwisiswant0/apkleaks](https://github.com/dwisiswant0/apkleaks)
    - The application we are testing might have some of the mobile application and the mobile application can have some API calls that the web application is not using.
    - This tool helps to find out the low hanging URLs from the APK itself
    
    ```bash
    apkleaks -f /source/app.apk -o out,txt
    ```


### Wayback Archive 

- [ ] waymore
    
    - [https://github.com/xnl-h4ck3r/waymore](https://github.com/xnl-h4ck3r/waymore)

    ```bash
    pip install waymore
    ```
    
    ```bash
    waymore -i target.com -mode B
    ```

- [ ] xnLInkFinder
    
    - [https://github.com/xnl-h4ck3r/xnLinkFinder](https://github.com/xnl-h4ck3r/xnLinkFinder)

    ```bash
    python3 xnLinkFinder.py -i ~/directory/to/xml/files -sp https://www.target.com -sf target.com -o output.txt
    ```


### Network Scan 
- [ ] naabu
    
    ```bash
      naabu -host 10.10.10.10 -p 1-65000    
    ```  
    
- [ ] nmap

    ```bash
      nmap -A -sV -sC -T3 -oA nmap/results -p 22,80,443 10.10.10.10
    ```  
      
- [ ] massscan

    - This is an Internet-scale **`port scanner`**. It can scan the entire Internet in under 5 minutes, transmitting 10 million packets per second, from a single machine.
    
    - [https://github.com/robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan)
    
    ```bash
    masscan --nmap
    ```
    
    ```bash
    masscan -p80,1000-2000 -Pn -iL <input_file> -oL outputfile.txt --max-rate <number>
    ```
    
    - Output File Formats
    
    - `-oG`  →  for saving the output in the gnmap format
    - `-oL`  →  In text format
    - `-oX`  →  In XML format

- [ ] dnmasscan

    - dnmasscan is a bash script to automate resolving a file of domain names and subsequentlly scanning them using masscan.
    
    - As masscan does not accept domain names, a file is created (specified in the second argument to the script) which will log which IP addresses resolve to which domain names for cross reference after the script has finished executing.
    
    - [https://github.com/rastating/dnmasscan](https://github.com/rastating/dnmasscan)
    
    ```bash
    dnmasscan domains.txt ips.txt -p80,443,1000-2000 -Pn -oG scan-results.gnmap --max-rate 1800
    ```
    - After the port analysis the output `gnmap` file format data is fed to the **`nmap`** service scan
    ```bash
    nmap -sV -Pn -iL scan-results.gnmap -oG nmap-results.gnmap
    ```    


### Automated Analysis 

- [ ] nuclei

    - [https://github.com/projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)
    
    ```bash
    nuclei -u target.com -fr -headless
    ```
    - **`-fr`** ⇒ Used for following redirects 
    - **`-headless`** ⇒ Used for headless mode which will enable templates that require headless browser support.
     
    - Scanning a directory of source code

    ```bash
    nuclei -u ./bank-application -file
    ```

- [ ] retirejs

    - [https://github.com/RetireJS/retire.js](https://github.com/RetireJS/retire.js)
    
    - This tool is used to scan the **`JS libraries`** for previously discovered **`CVEs`**
    - You can automatically scan for vulns in JavaScript libraries used by applications.
    - Burpsuite Extension
    - rowser Extension

- [ ] opengrep

    - This tool is used for static application scanning like source code review 
    - [https://github.com/opengrep/opengrep](https://github.com/opengrep/opengrep)
    
    - [https://github.com/opengrep/opengrep-rules](https://github.com/opengrep/opengrep-rules)
    
    ```bash
    opengrep scan -f /path/to/rules/language /path/to/target/directory
    ```

- [ ] metasec.js

    - [https://github.com/LewisArdern/metasecjs](https://github.com/LewisArdern/metasecjs)

- [ ] Burpsuite Active Scan
    - Scan a target
    - Scan a request
    - Scan a parameter
     


### Manual Analysis 

- #### Questions
  
- [ ] How the client and the server interacts
  - Reverse Proxies
  - CDN
  - Firewalls
  - Load Balancers
  - Virtual Host
- [ ] How does the app pass data
  - Body (x-www-urlencoded / multipart-formdata / json)
  - URL (Traditional / RESTful format)
- [ ] Where and how does the app talk about users
  - Authentication and Authorization
  - Where (Tokens / Cookies / API Calls)
  - How (UID / email / username)
- [ ] Multitenancy and User levels
  - Multitenancy (customer / normal user / employee)
  - User Levels (user / admin)
- [ ] A unique Threat Model (CIA)
- [ ] Past security researches, previously discovered vulns
- [ ] How the app stores data
  - Database
  - S3 Buckets
  - Image Uploads
  - Comments
  - Profile Data
- [ ] How the framework handles or protect itself from different vulns
      
- #### Testcasses


















































































 
