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
- ### JS Scraping
- ### Waymore
- ### [Network Scan]()
- [ ] naabu
- [ ] nmap
- [ ] rustscan 
- ### [Automated Analysis]()
- nuclei
- Burpsuite Active Scan 
- ### [Manual Analysis]()

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





























 
