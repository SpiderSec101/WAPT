# Test Cases

- [Asset Discovery](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#asset-discovery-subdomains-apexdomains-ipv4-ipv6)
- [DNS Records](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#dns-records)
- [Github Enumeration](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#github-enumeration)
- [Tech Profiling](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#tect-profiling)
- [Meta Files](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#meta-files)
- [Directory Bruteforcing](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#bruteforcing-directories--parameters)
- [URls and Endpoints](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#urls--endpoints)
- [Open Ports](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#open-ports)
- [Automated Analysis](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#automated-analysis)
- [Manual Analysis](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#manual-analysis)
- [Questions](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#questions)
- [Wordlists](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#wordlists)
---
- [Authentication](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#authentication)
- [SQL Injection](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#sql-injection)
- [XSS](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#xss)



## Asset Discovery (Subdomains, Apexdomains, IPv4, IPv6)
- [ ] Acquitisions
  - crunchbase.com
- [ ] ASN
  - bgp.he.net
  - nmap
- [ ] Extracting Domains from ASN
  - amass intel
- [ ] Certificate Transparency
  - crt.sh
- [ ] Shodan
  - Shodan CLI
  - Shosubgo
  - Karma_v2
- [ ] Cloud Based Recon
  - kaeferjaeger.gay
- [ ] github-subdomains
- [ ] Ad/Analytics Tracker Codes
  - builtwith
- [ ] Amass Scanning
- [ ] BBOT Scanning
- [ ] Subfinder
- [ ] Passive Subdomain Bruteforcing
  - Puredns
  - Amass
  - Shuffledns
- [ ] Active Subdomain Bruteforcing
  - Dnsenum
  - Sublist3r
  - OneForAll
- [ ] Live Hosts
  - httprobe
  - httpx
- [ ] Permutations
  - dnsgen
- [ ] Screenshots
  - Eyewitness
  - gowitness
  - httpx
  - Aquatone
  - html.sh (custom)
- [ ] Favicon Analysis
  - favfreak.py
## DNS Records
- [ ] Amass Scanning
- [ ] BBOT Scanning
- [ ] dig
- [ ] dnsrecon
- [ ] dnsenum
- [ ] fierce
- [ ] host
- [ ] whois
## Github Enumeration
  - git-history
  - github-dorks
  - github-endpoints
  - github-secrets
  - github-subdomains
  - github-contributors
  - github-employess
## Tech Profiling
- [ ] Wappalyzer
- [ ] Builtwith
- [ ] Whatruns
- [ ] Webanalyzer
- [ ] WAF
    - wafw00f
- [ ] Cloning
    - httrack
## Meta Files
- [ ] robots.txt
- [ ] sitemap.xml
- [ ] humans.txt
- [ ] security.txt
- [ ] .env
- [ ] .git
## Bruteforcing (Directories / parameters)
- [ ] dirsearch
- [ ] ffuf
- [ ] feroxbuster
- [ ] wfuzz
## Wordlists
- [ ] Assetnote Wordlists
- [ ] SecLists
- [ ] Payloadallthethings Intruder 
## URLs / Endpoints
- [ ] JS Analysis
  - Linkfinder
  - SubDomainizer
  - Burp-GAP
  - JSMiner
  - metasec.js
- [ ] Crawlers
  - katana
  - go-spider
  - hakrawler
- [ ] Waymore
- [ ] xnLinkFinder
- [ ] Known Paths
  - Demo
  - LocalInstall
  - Dockerhub
- [ ] APK Leaks
## Open Ports
- [ ] naabu
- [ ] nmap
- [ ] masscan
- [ ] dnmasscan
## Automated Analysis
- [ ] Nuclei
- [ ] Retire.js
- [ ] Jaeles
- [ ] Active Burpsuite Scan
  - Scan a Target
  - Scan a Request
  - Scan an Input Parameter
- [ ] Using AI
  - [ ] strix (https://github.com/usestrix/strix)
  - [ ] hexstrike
  - [ ] AI Auditor 
## Manual Analysis
- [ ] CVEs
- [ ] Passive Burp Scan
- [ ] Manual Crawling (Sitemap)
- [ ] Analyze Target
  - Dynamic URLs
  - Static URLs
  - Parameters
- [ ] Manual Fuzzing
  - Repeater
  - Intruder
  - Wordlists
## Questions
- [ ] How does the app pass data
     - Body (x-www-urlencoded / multipart-formdata / json)
     - URL (Parameters / RESTful format)
- [ ] Where does the app talk about users
     - Where (Tokens / Cookies / API Calls)
     - How (UID / email / username)
- [ ] Multitenancy and User levels
     - Multitenancy (customer / normal user / employee)
     - User Levels (user / admin)
- [ ] A unique Threat Model (CIA)
- [ ] Past security researches and discovered vulns, CVEs
- [ ] How the app stores data
     - Database
     - S3 Buckets
     - Image Uploads / Comments / Profile details
- [ ] How the framework handles or protect itself from different vulns
## Wordlists
- [ ] Seclists
- [ ] Payloadallthethings
- [ ] Assetnotes
- [ ] Custom (cewl)
## Modules and Sub-Modules
- [ ] Find Directories and Sub-Directories
- [ ] Authentication
  - Token Basis
  - Session Basis
- [ ] Authorization
- [ ] User Input Fields
- [ ] File Uploads
- [ ] Chat-Bots
- [ ] Debugging Page / Console
- [ ] APIs
- [ ] HTTP Headers
- [ ] HTTP Methods
- [ ] Backup Files / Source Code
---
## Authentication
- [ ] Weak Credentials
- [ ] By-default Credentials
- [ ] Ratelimiting
- [ ] Account Locking
- [ ] Captcha
  - Token Reuse
  - Bypass via different HTTP Methods
  - Captcha encoded into HTML
- [ ] Hardcoded Credentials
- [ ] Forgot Password or Reset Password
- [ ] User Name Enumeration
- [ ] Session ID Prediction
- [ ] Session Fixation
- [ ] JWT Manipulation
- [ ] SQL Injection
- [ ] No SQL Injection
- [ ] Stored Password Hash
- [ ] Strong Password Policy
- [ ] OAuth
- [ ] SSO
- [ ] MFA
  - OTP Bruteforcing
  - Guessing OTP
  - OTP Reuse
- [ ] Register Using Content Discovery
- [ ] Register Using API
## SQL Injection
- [ ] In-Band SQL Injection
  - Error Based
  - Union Based
  - Stacked Queries
  - Concatenation
- [ ] Blind SQL Inection
  - Boolean Based
  - Time Based
- [ ] Out of Band SQL Injection
- [ ] Second Order SQL Injection
- [ ] Double Queries
- [ ] Tools
  - SQLMap
  - Ghauri
## XSS 
- [ ] Types
  - Reflected
  - Stored
  - DOM Based
  - Self XSS
  - Blind XSS
- [ ] Try HTML Injection
- [ ] Blocked Characters
- [ ] Allowed Tags
- [ ] Allowed Eventhandlers
- [ ] Context
  - HTML
  - URL
  - Attribute
  - Script
- [ ] Check Fragments `location.hash`
- [ ] Filter Bypasses
- [ ] CSP Bypasses
- [ ] Iframe Sandbox
- [ ] XSS through File Uploads
  - SVG
  - JPG
  - Markdown
  - XML
  - JS
- [ ] Blind XSS
  - Out-Of-Band Payload
  - Environment Setup 
- [ ] Different Payloads
- [ ] Exploitation
  - Cookie Stealing
  - Autofillup Password
  - Stored XSS to CSRF
  - CORS Bypass
  - Dangling Markup Injection
- [ ] HttpOnly
  - localstorage
  - phpinfo
  - cookie with long path

















