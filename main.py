###################################
####                           ####
####    Author : Im.Payz       ####
####    Name   : EZDownloader  ####
####    Version: 2.0           ####
####                           ####
###################################



from Module import ezdownloader as EZ
from Module.packages import *
from Module.banner import *

os.system("clear")

banner = Banners()
print(banner.EzWelcome())

def check(links):
   
   
   link = links  
   name = link.split("//")[1]
   
   if "instagram" in name:
      ig = EZ.Instagram(link)
      ig.Run()
   elif "facebook" in name:
      fb = EZ.Facebook(link)
      fb.Run()
   elif "youtube" in name:
      yt = EZ.Youtube(link)
      yt.Run()
   elif "tiktok" in name:
      tk = EZ.Tiktok(link)
      tk.Run()
   else:
      return "Sory this is will be update soon" 
  


links = input("[>>] Put Your Link: ") 
check(links)

   
