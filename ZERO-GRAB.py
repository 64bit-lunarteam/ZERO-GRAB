# code obfuscated for safety purposes!

import os #line:1
import sys #line:2
import datetime #line:3
from datetime import datetime #line:4
import socket #line:5
import pyfiglet #line:6
import colorama #line:7
import time #line:8
import subprocess #line:9
from colorama import Fore ,Back ,Style #line:11
colorama .init ()#line:12
valid_hex ='0123456789ABCDEF'.__contains__ #line:15
def cleanhex (OOOO0OOO0O00OOO00 ):#line:16
    return ''.join (filter (valid_hex ,OOOO0OOO0O00OOO00 .upper ()))#line:17
def fore_fromhex (O0O00O00000OOO0O0 ,OO00OO0OO0O0O0OOO ):#line:19
    ""#line:20
    O000O0O0OOOOOOO00 =int (cleanhex (OO00OO0OO0O0O0OOO ),16 )#line:21
    print ("\x1B[38;2;{};{};{}m{}\x1B[0m".format (O000O0O0OOOOOOO00 >>16 ,O000O0O0OOOOOOO00 >>8 &0xFF ,O000O0O0OOOOOOO00 &0xFF ,O0O00O00000OOO0O0 ))#line:22
print ()#line:24
print ()#line:25
print ()#line:26
fore_fromhex ('          ███████╗███████╗██████╗  ██████╗        ██████╗ ██████╗  █████╗ ██████╗ ','#a903fc')#line:27
fore_fromhex ('          ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗      ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗','#a903fc')#line:28
fore_fromhex ('            ███╔╝ █████╗  ██████╔╝██║   ██║█████╗██║  ███╗██████╔╝███████║██████╔╝','#a903fc')#line:29
fore_fromhex ('           ███╔╝  ██╔══╝  ██╔══██╗██║   ██║╚════╝██║   ██║██╔══██╗██╔══██║██╔══██╗','#a903fc')#line:30
fore_fromhex ('          ███████╗███████╗██║  ██║╚██████╔╝      ╚██████╔╝██║  ██║██║  ██║██████╔╝','#a903fc')#line:31
fore_fromhex ('          ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝','#a903fc')#line:32
fore_fromhex ('          ========================================================================','#75488c')#line:33
fore_fromhex ('                              ZERO-GRAB v1.0 CREATED BY VENOM','#808080')#line:34
print ()#line:35
fore_fromhex ('                > Enter IP address to portscan >','#808080')#line:36
target =input (str ("Target IP: "))#line:39
fore_fromhex ("_"*50 ,'#a903fc')#line:40
fore_fromhex ("Scanning Target: "+target ,'#a903fc')#line:41
fore_fromhex ("Scanning started at: "+str (datetime .now ()),'#a903fc')#line:42
fore_fromhex ("_"*50 ,'#a903fc')#line:43
try :#line:45
    for port in range (1 ,65535 ):#line:47
        s =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:48
        socket .setdefaulttimeout (0.5 )#line:49
        result =s .connect_ex ((target ,port ))#line:51
        if result ==0 :#line:52
            fore_fromhex ("[*] Port {} is open.".format (port ),'#a903fc')#line:53
        s .close ()#line:54
except KeyboardInterrupt :#line:56
    fore_fromhex ("\n Exiting",'#75488c')#line:57
    sys .exit ()#line:58
except socket .error :#line:59
    fore_fromhex ("\n Host not responding",'#75488c')#line:60
    sys .exit ()#line:61
input ()