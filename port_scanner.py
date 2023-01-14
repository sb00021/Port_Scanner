import socket, threading, pyfiglet, time

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print("/"*50)
print("\t....    By SAYAN    ....")
print("/"*50)

host=(input("\nEnter host or ip to scan: "))
start_port=int(input("Enter start port: "))
end_port=int(input("Enter end port: "))

if end_port<=65336:
    print("Scanning.....")
    print("\n")

    try:
        socket.gethostbyname(host)
    except:
        print("failed to get ip...")
        exit()

    def scan(port):
        s=socket.socket()
        s.settimeout(2)
        result=s.connect_ex((host,port))
        if result==0:
            if port<10:
                print(f"{port}     no. port is open")
            elif port<100:
                print(f"{port}    no. port is open")
            elif port<1000:
                print(f"{port}   no. port is open")
            elif port<10000:
                print(f"{port}  no. port is open")
            else:
                print(f"{port} no. port is open")
        s.close()
    for i in range(start_port,end_port+1):
        t=threading.Thread(target=scan, args= (i,)) 
        t.start()
else:
    print("Enter port between 0 - 65336")
print('\n')