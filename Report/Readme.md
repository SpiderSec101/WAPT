# General points to remember while writing reports 

- Application Name 
- Environment: UAT / PROD / QA
- Funcitonality: 
	-- Write about the business logic of the application 
	-- About the function of the application 
	-- EG: The applicaiton is used to monitor the trafiic rules like speed limiting in a particular campus. Also it helps to generate the challan and click an image of the veichle along with its veichle id.

- Overall Security Posture:
	-- According to the findings present in the application 
	-- Not depending on the number of findings.

- Adversary: How the application is affected if the findings are exploited in real life.

- Testing Tools:
	-- All the tools like
	1. Burpsuite 
	2. Sublime Text
	3. Different Linux Command Line Tools

- User Roles: 
	-- Example
	The following user accounts are provided for the assessment
  	- [ ] Super User 
	1. Admin1/admin1@company.com 
	2. Admin2/admin2@company.com
	- [ ] Normal User
	1. Test1/test1@company.com 
	2. Test2/test2@company.com

- Scope:
	-- Example
  - [ ] In-Scope:
	-- URLs:
	1. url1
	2. url2
	-- Functionalities
	1. Register / Login
	2. Admin Panel 
	3. File Upload
	- [ ] Out-of-Scope
	-- URLs:
	1. url1
	2. url2
 	-- Functionalities

- Strength: 
	-- About the strength of the applicaiton
	-- Write it based on failed testcases
	-- Helps the management guys to make an idea about the applicaiton strenghts.

- Weakness
	-- Includes all the findings [CRITICAL/HIGH/MEDIUM/LOW]

- Technical Impact: 
	-- What breaks technically 
	-- For managements Guys

- Business Impact: 
	-- Why the organisation should care
	-- For management Guys


#### Findings

- Description: 
	-- Two parahs
	-- 1st parah: The technical definition of the finding  
	-- 2nd parah: During the assessment
		- [ ] Where and How the vulnerability occurs
		- [ ] User role used to exploit it 

- Affected URLs:
	-- Full URL path
	-- All the endpoint URLs where the particular vulnerability is present 

- Affected Parameters:
	-- GET: ID
	-- POST: ID
	-- Request/Response Header: HOST / Access-Control-Allow-Origin
	-- JSON Body: uid

- Steps to Reproduce:
	-- A client can follow the steps and reproduce the vulneranbility without any blockers
	-- Do not summarize the steps 
	-- Mentioned steps should be exact and explicit
	-- Uses clear screenshots
	-- If Burp tools are involved, explicitly mention the tools used
		- [ ] Proxy
		- [ ] Repeater
		- [ ] Intruder
	-- For modified requests mention
		- [ ] You have send the request into the repeater
		- [ ] Modified any partcular header or any parameter value
		- [ ] The reason of modification
	-- The observations should be clearly metioned after sending a modified request to the application.

	-- When authentication is required the following format can be used
		- [ ] Log in toi the applicaiton using the credentials of the User-Role / Username account
		- [ ] Admin / Jeremy
		- [ ] Normal User / Spider
	-- When UI Based workflows are required
		- [ ] EG: Navigate to the 'Admin Panel -> Add User' functionality using the browser.
		- [ ] Clearly distuinguish between UI based and Direct URL based access 
	-- When the URL Based workflow is required
		- [ ] EG: Navigate to the following URL in the browser.




































