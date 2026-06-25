#coding:utf-8
import os
import time
import argparse

def biaoti():
    splash1 = """
        +----------------------------------+
        | LulZ_41m4r11                     |
        +----------------------------------+
        | by kr0k3tⒶuN    #̸̥̬̯́̆̾͘Lú̸̺̱̮̖͊̂lzs̶̡͔̉̀eC        |
        +----------------------------------+
    """
    print(splash1)

def args():
    parser = argparse.ArgumentParser(description='LulZ_41m4r11')
    parser.add_argument('-i', '--input', help='masscan -iL', required=True)
    parser.add_argument('-p', '--port',help='masscan -p', required=True)
    parser.add_argument('-rate','--rate', help='masscan rate', required=True)
    args = parser.parse_args()
    return args

def update():
    splash00 = """
        +----------------------------------+
        | Fuck The System Forever         
        +----------------------------------+
    """
    print(splash00)
    os.system('nuclei -update')
    os.system('./xray_linux_amd64 upgrade')
    splash03 = """
        +----------------------------------+
        | lulz for aimar11 created for kroketon 
        +----------------------------------+
    """
    print(splash03)


def check_args(args):
    if not os.path.exists(args.input):
        print('ip')
        exit()
    if not args.port:
        print('Number of ports to scan')
        exit()
    if not args.rate:
        print('Enter the scan rate (example).：-rate 2000)')
        exit()
    return args

def masscan2httpx2nuclei(args):
    args = check_args(args)
    input_file = args.input
    port = args.port
    rate = args.rate
    os.system('masscan -iL ' + input_file + ' -p' + port + ' -oL masscan.txt --rate ' + rate)

def masscan2httpx2nuclei_main():
    while True:
        if os.path.exists("masscan.txt"):
            break
        else:
            time.sleep(1)
    if os.path.getsize("masscan.txt") == 0:
        splash3 = """
            +----------------------------------+
            |No port open, program exited!         
            +----------------------------------+
        """
        print(splash3)
        exit()
    else :
        splash4 = """
            +------------------------------------------+
            | Masscan scan results parse and call httpx   
            +------------------------------------------+
        """
        print(splash4)
        masscanfile = open("masscan.txt", "r")
        masscanfile.seek(0)
        for line in masscanfile:
            if line.startswith("#"):
                continue
            if line.startswith("open"):
                line = line.split(" ")
                with open("masscanconvert.txt", "a") as f:
                    f.write(line[3]+":"+line[2]+"\n")
                    f.close()
        masscanfile.close()
    if os.path.exists("masscan.txt"):
        os.system('httpx -l masscanconvert.txt -nc -o httpxresult.txt')
        os.remove("masscan.txt")
        splash2 = """
            +----------------------------------+
            | Httpx is done !                  
            +----------------------------------+
        """
        print(splash2)
    else:
        splash5 = """
            +--------------------------------------------------+
            | No results were found for the parsed masscan port    
            +--------------------------------------------------+
        """
        print(splash5)
        exit()
    if os.path.exists("httpxresult.txt"):
        os.system('nuclei -l httpxresult.txt -s medium,high,critical -o nucleiresult.txt')
        os.system('./xray_linux_amd64 webscan -url-file httpxresult.txt --html-output xray.html')
        os.remove("httpxresult.txt")
        os.remove("masscanconvert.txt")
    else:
        print("The scan results did not find the http protocol")
        exit()
    if os.path.exists("nucleiresult.txt"):
        splash6 = """
            +----------------------------------------+
            |The scan is complete. Please check it out 
            +----------------------------------------+
        """
        print(splash6)
    else:
        splash7 = """
            +----------------------------------------------------------+
            | nuclei No medium and high-risk vulnerabilities were found               
            +----------------------------------------------------------+
        """
        print(splash7)
    if os.path.exists("xray.html"):
        splash8 = """
            +----------------------------------------------+
            | The scan is complete. Please check 看xray.html        
            +----------------------------------------------+
        """
        print(splash8)
    else:
        splash9 = """
            +----------------------------------+
            | xray No vulnerabilities found                    
            +----------------------------------+
        """
        print(splash9)
    exit()


def main():
    biaoti()
    update()
    LulZ_41m4r11(args())
    LulZ_41m4r11_main()

if __name__ == '__main__':
    main()
    exit()
