# hallo bro :v

from wibu.YNTKTS import *
import urllib.request

areYOUgay=random.choice(["Kang.Pacman","Lo.Ngentod.Ajg"])

class report:
	def __init__(self,url,cookie):
		
		self.url=url
		self.cookies=cookie
		self.laporkan()
		
	def find_id(self,username):
		try: respon=req.get(f"{self.url}/{username}/about",cookies=self.cookies).text
		except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
		uid=re.search('\<a\ href\=\"/.*?\?v=timeline&amp;lst=(.*?)"',respon).group(1)
		return urllib.request.unquote(uid).split(":")[1]
	
	def chat(self,uid,ngebug,**data):
		try: respoN=req.get(f"{self.url}/messages/?fbid={uid}",cookies=self.cookies)
		except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
		respon=parser(respoN.text,"html.parser")
		nv=respon.find_all("input",{"type":"hidden","name":True,"value":True})
		act=respon.find("form",{"method":"post","action":True})
		if len(nv)!=0 and act!=None:
			data.update({x["name"]:x["value"] for x in nv})
			data.update({f"ids[{uid}]":uid,"body":ngebug,"Send":"Kirim"})
			respon=req.post(self.url+act["action"],headers=head(self.url,respoN),cookies=self.cookies,data=data)
			exit("\033[0;34m╚══\033[0;32mSUKSES" if "send_success" in respon.url else "\033[0;34m╚══\033[0;31mGAGAL")
		else: exit("\033[0;34m╚══\033[0;31mEROOR")
			
	def laporkan(self):
		#asuu=self.find_id(areYOUgay)
		teks_bug=input("\033[0;34m╠═\033[0;33mYANG SOPAN NGAB \033[0;34m⋙ ")
		while teks_bug in (""," "):
			print("\033[0;34m╠═\033[0;31mTEKS KOSONG")
			teks_bug=input("\033[0;34m╠═\033[0;33mYANG SOPAN NGAB \033[0;34m⋙ ")
		self.chat("100006230836266",teks_bug)
		
