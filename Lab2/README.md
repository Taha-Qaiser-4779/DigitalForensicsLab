#### Note: For some unknown reason, Github isn't letting me paste pictures into this readme file so I will upload them in this folder (not in the README file)

## Q1) 
1) Double-click speed is 500
#####		(attached "registry mouse double click speed.png")
2) C:\Windows\System32\calc.exe
#####		(attached "registry typed paths.png")
3) A key called "Malware" has been added to the startup programs to establish persistence over the system. The value for that key is "C:\Users\w\Desktop\malware.exe"
#####		(attached "registry malwarestartup.png")
---
## Q2)
1) hackerman:sup3rs3cur3p4ssw0rd
#####		(attached "firefox credentials.png")
2) https://www.tryhackme.com OR https://www.amazon.com 
  tryhackme is the most frequently visited website according to the "moz_places" table and amazon is the most frequently visited website according to the
	"moz_origins" table.
#####		(attached "firefox moz_origins.png" and "firefox moz_places.png")
3) python-3.11.1-amd64(1).exe
#####		(attached "firefox Downloads.png")

---
## Q3)
1) We can see that the invoke web request command was used to download a file called "file.ps1" onto the system. 

		Invoke-WebRequest -UseBasicParsing -Uri https://raw.githubusercontent.com/vonderchild/digital-forensics-lab/main/Lab%202/files/file.ps1 -OutFile "file.ps1"
	
2) The script has two variables, one is a base64 encoded string called "data" and the second is the "flag" which is the decoded "data" variable. The script prints the flag variable.
		flag{ev3nt_l0gs_f0r_th3_w1n}
---
