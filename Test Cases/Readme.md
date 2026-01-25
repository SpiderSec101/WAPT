# Test Cases

- [Asset Discovery](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#asset-discovery-subdomains-apexdomains-ipv4-ipv6)
- [DNS Records](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#dns-records)
- [Github Enumeration](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#github-enumeration)
- [Tech Profiling](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#tect-profiling)
- [Meta Files](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#meta-files)
- [Directory Bruteforcing](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#bruteforcing-directories--parameters)
- [Wordlists](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#wordlists)
- [URls and Endpoints](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#urls--endpoints)
- [Open Ports](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#open-ports)
- [Automated Analysis](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#automated-analysis)
- [Manual Analysis](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#manual-analysis)
- [Questions](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#questions)
- [Testing](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#testing)
- [Authentication](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#authentication)
- [SQL Injection](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#sql-injection)
- [XSS](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#xss)
- [Low Hanging Fruits](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#low-hanging-fruits)
- [File Uploads](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#file-uploads)
- [XXE](https://github.com/SpiderSec101/Web_Application_Security_Testing/tree/main/Test%20Cases#xxe)



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

## Testing 
- [ ] Source Code and JS Files Analysis
- [ ] Listing Modules and Sub-Modules  
- [ ] Authentication
  - Token Basis
  - Session Basis
- [ ] Authorization (IDOR, Privilege Escalation)
- [ ] Testing Parameters
- [ ] User Input Fields
- [ ] File Uploads
- [ ] Chat-Bots
- [ ] Forms
- [ ] Debugging Page / Console
- [ ] APIs
- [ ] HTTP Headers
- [ ] HTTP Methods
- [ ] Backup Files
- [ ] Directories and Sub-Directories
- [ ] Cache Security
- [ ] HTTP Request Smuggling
- [ ] Business Logic Flaws
- [ ] SSO / OAuth
- [ ] Race Condition
- [ ] Low Hanging Fruits
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
- [ ] Blind SQL Injection
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
- [ ] Context
  - HTML
  - URL
  - Attribute
  - Script
- [ ] Check Fragments `location.hash`
- [ ] Filter Bypasses
  - Whether the payload is HTML encoded
  - Look for allowed tags and evenlisteners
  - Without event handlers
    ```
    <script src=”javascript:alert(1)”></script>
    <iframe src=…></iframe>
    <a href=...>
    ```
  - Custom Tags
  - Filter's Rules : Which characters are blocked
  - Case Sensitive
  - Using Regex for filters ? : Try double occurance
  - Is it stripping ? : `<scr<script>ipt>`
- [ ] CSP Bypasses
  - CSP Evaluator [`https://csp-evaluator.withgoogle.com/`](https://csp-evaluator.withgoogle.com/)
  - unsafe inline
  - unsafe eval
      - CSP ⇒ Angular.js
      - CSP ⇒ DOM XSS
  - data:
  - JSONP
      - Callback end points
      - www.youtube.com
      - Any application using OAuth or SSO
  - Third Party Domain
      - *.google.com ⇒ google drive
      - *.yandex.net
      - www.google-analytics.com
  - File Uploads
      - file.js
  - `default-src ‘self’`
      - Redirecting the victim using `window.location`
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
  - CORS Bypasses
  - Dangling Markup Injection
- [ ] HttpOnly Bypasses
  - localstorage
  - phpinfo
  - cookie with long path

## Low Hanging Fruits
- [ ] Authentication 
  - Weak credentials
  - By-default credentials
  - Lac of Ratelimiting
  - Ratelimiting Bypasses
  - No Account Locking
  - Hardcoded Credentials in Source Code
  - Username Enumeration
  - Weak Cryptogaphy Implemented in Authentication
  - Weak Password Hash Algorithm
  - Weak Password Policy
  - Whether MFA enabled
  - Forgot password features
  - Change password to the existing password
- [ ] HTTP Headers
  - Missing Security Headers
  - Weakly configured security headers
- [ ] HTTPs
  - SSL / TLS issues (https://github.com/testssl/testssl.sh)
  - HTTPs not enabed
  - HTTPs not enforced
- [ ] Sesion
  - Session valid after logging out
  - No logout functionality
  - Session token present in URL
  - Session ID can be predicted
  - Session Fixation
- [ ] Vulnerable Libraries
- [ ] Transmitting specific data in plain text
- [ ] Server Banner Information Disclosed
- [ ] Unnecessarily exposed features
- [ ] Misconfiguration in mailing systems
- [ ] Application sends information to 3rd party domains
- [ ] Bypassing client side user input validation
- [ ] Sensitive metadata in downloadable files
- [ ] Exposing API keys in client side code
- [ ] Overflows
- [ ] No user input limit
- [ ] Client side DoS attacks
- [ ] APK application exposes API keys and endpoints
- [ ] Business or Company Specific Flaws


## File Uploads
- [ ] Allowed Extensions
- [ ] Extension Whitelist Bypasses
- [ ] Content-Type
- [ ] File Signatures
- [ ] Payload in between data chunks
- [ ] Polygot files
- [ ] Shell upload via path traversal
- [ ] Editing configuration files
- [ ] Uploading zip files
  - Symlink
  - Decompressed in different files
- [ ] File upload to XSS
- [ ] File upload to XXE
- [ ] DoS
  - XXE Million Laugh Attack
  - Decompression Bomb
  - Pixel Flood Attack
- [ ] No file size limit
- [ ] No rate limiting
- [ ] No limit of the number of uploaded files


## XXE 
- [ ] JSON to XML convertion
- [ ] LFI
- [ ] Error Based Attacks
- [ ] Blind XXE
- [ ] Using Local DTD and Remote DTD
- [ ] Parameter Entities
- [ ] XXE via SVG file upload
- [ ] SSRF using XXE
- [ ] Dos
  - Billion Laugh Attack
  - YAML Bomb
  - Parameter Laugh Attack
- [ ] XInclude







