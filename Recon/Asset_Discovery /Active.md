## Active Reconnaissance

* Active reconnaissance refers to techniques used to gather information about a target system, network, or environment by directly interacting with it.  
* Here I have made a list of tools that helps to recon actively.  
* The list shows what type of informations I am trying to extract and to acheive that what kind of tools I am using. I also guide on how to use a tool.
---  

### Domain Registration Information
- [ ] [<ins>whois</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#whois)
### DNS Enumeration
- [ ] [<ins>dnsrecon</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#dnsrecon)
- [ ] [<ins>fierce</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#fierce)
- [ ] [<ins>dsnenum</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#dnsenum)
- [ ] [<ins>dig</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#dig)
- [ ] [<ins>host</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#host)


### Web Application Firewall
- [ ] [<ins>wafw00f</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#wafw00f)

### Web Clone
- [ ] [<ins>httrack</ins>](https://github.com/SpiderSec101/WAPT/blob/main/Recon/Asset_Discovery%20/Active.md#httrack)
---  


#### whois
    whois example.com
#### dnsrecon
    
    
    dnsrecon -d target.com
    
    
#### fierce
    
    
    fierce --domain target.com
    
    
#### dnsenum
    
    
    dnsenum target.com
    
    
#### dig
    
    
    dig axfr @<name-server-here> example.com
    
    
   - Here we are using the **`axfr`** protocol to zone transfer the DNS records of the target domain

#### host
   - It helps to look for the A and AAAA records of the domain.
    
    
    host target.com
    
#### wafw00f
    wafw00f -a example.com  

#### httrack
    httrack
   Then it will ask for different options, follow the instructions. 

         
