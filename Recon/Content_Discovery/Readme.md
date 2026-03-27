- ### [Wordlists]()
- ### [Subdomain Bruteforcing]()
- ### [Directory Bruteforcing]()
- ### [Parameter Fuzzing]()
- ### [URls and Endpoints]()
- ### [Network Scan]()
- ### [Automated Analysis]()
- ### [Manual Analysis]()

--- 

- #### Wordlists
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


- #### Subdomain Bruteforcing 

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













 
