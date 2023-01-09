import argparse

parser = argparse.ArgumentParser(
                    prog = 'encrypt.py',
                    description = 'This tool encrypts all files',
                    epilog = 'Thanks for using this piece of code')



parser.add_argument('-f', '--file',required=True,help="Any path to filename") 
parser.add_argument('-m', '--mode',required=True,help="Tool mode : 0 - Encrypt , 1 - Decrypt") 
parser.add_argument('-k', '--key',required=True,help="Offset number to change every char") 

args = parser.parse_args() #returns list of all args 

if not args.key.isdigit():
    print("Key isn't a number")
    exit()

if not (args.mode == '0' or args.mode == '1'):
    print("Mode is invalid")
    exit()
    
try:
    f = open(args.file,'rb')
    byte = f.read(10)
    arr = bytearray(byte)
    
    while(byte):
        byte = f.read(10)
        arr += byte
        #arr is full of bytes
        
        
    
   
    out = []
    for i in arr:
        if(args.mode=='0'): #encrypt
            out.append((i+int(args.key))%256)
            
        else: #decrypt
            if((i-int(args.key))<0): 
                out.append(256+(i-int(args.key)))
            else:
                out.append((i-int(args.key)))
                
                
    print(out)
    
    # encrypted/decrypted the file into out string
    # now we need to write it into the original file
    
    f.close() #optional
    f = open(args.file,'wb')
    f.write(bytearray(out))
    print("Done")
except FileNotFoundError as e:
    print(e)
    
    


