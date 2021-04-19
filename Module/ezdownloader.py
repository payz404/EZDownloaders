###################################
####                           ####
####    Author : Im.Payz       ####
####    Name   : EZDownloader  ####
####    Version: 2.0           ####
####                           ####
###################################



from Module.packages import *
from Module.banner import *

class Downloader(ABC):
           
   def __init__(self, url):      
      
      os.system("clear")
      
      global banner
      self.banner = Banners()
      print(self.banner.EzWelcome())     
      self.url = url
      
   
   def browser(self):
      
      
      software_names = [SoftwareName.CHROME.value]
      operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
      
      user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
      user_agents = user_agent_rotator.get_user_agents()
      user_agent = user_agent_rotator.get_random_user_agent()
      
      return user_agent
   
   
      
   @abstractmethod
   def Run(self):
      pass  
                        
   @property
   @abstractmethod
   def url(self):
      pass
   
   
      
                      
            
                                             

class Instagram(Downloader):
 
 
      
   def Run(self):
      os.system("clear")
      #self.Menu
      print(self.banner.EzWelcome())     
      header = {'User-Agent':self.browser()}
      r = requests.get(self.url, headers=header)
      
      getLink_video = re.findall('"video_url":"([^"]+)"', r.content.decode('utf-8'))

      getLink_img = re.findall('"display_url":"([^"]+)"', r.content.decode('utf-8'))

      video = {'url':match.replace("\\u0026", "&") for match in getLink_video}
      img = {'url':match.replace("\\u0026", "&") for match in getLink_img}

      if video:
         #print(video['url'])
         output = input("[>>] Save Dengan Nama: ")
         wget.download(video['url'], 'Result/Instagram/{}.mp4'.format(output))
         print("\n")
         print("[ Download Complete ! ]\n")
               
         
      elif img:
         print("Img")
         output = input("[>>] Save Dengan Nama: ")
         wget.download(video['url'], 'Result/Instagram/{}.jpg'.format(output))
         print("\n")
         print("[ Download Complete ! ]\n")
      else:
         print("Invalid URL")     
      
          
   @Downloader.url.setter
   def url(self, input):
      self.__url = input
            
   @url.getter
   def url(self):
      return self.__url     
      


class Facebook(Downloader):
 
   
   def Run(self):
   
      os.system("clear")
      print(self.banner.EzWelcome())
      print("[1] Download Dengan Resolusi Tinggi.\n[2] Download Dengan Resolusi Normal.")
      step1 = input("\n[>>] Masukan Pilihan Resolusi (1/2): ")
      
      if step1 == "1":
         
         try:
           
           html = requests.get(self.url, headers={"User-Agent": self.browser()})          
           sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
           
           
         except requests.ConnectionError as e:
           print("Cek koneksi anda")
         except requests.RequestException as e:
           print("Invalid URL")
         except (KeyboardInterrupt, SystemExit):
           print("Dibatalkan")
           sys.exit(1)
         except TypeError as e:
           print("[ Something Error: Try Again Later ]")
         else:
           sd_url = sdvideo_url.replace('hd_src:"', '')
           print("\n")
           print("[!] Kualitas HD: " + sd_url)
           print('\n[!] Example: namafile')
           filemu = input('[>>] Save dengan nama: ')
           myRes = "/Result/Facebook/"
           print("[+] Download start")
           wget.download(sd_url, "Result/Facebook/{}.mp4".format(filemu))
           
           print("\n")
           print("[+] Finish Download")
           print("\n")
           
      elif step1 == "2":
         
         try:
           
           html = requests.get(self.url,headers={"User-Agent": self.browser()})          
           sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
         except requests.ConnectionError as e:
           print("Cek koneksi anda")
         except requests.RequestException as e:
           print("Invalid link")
         except (KeyboardInterrupt, SystemExit):
           print("Dibatalkan")
           sys.exit(1)
         except TypeError:
           print("[ Something Error: Try Again Later ]")
         else:
           sd_url = sdvideo_url.replace('sd_src:"', '')
           print("\n")
           print("[!] Kualitas Normal: " + sd_url)
           print('\n[!] Example: namafile')
           filemu = input('[>>] Save dengan nama: ')
           print("[+] Download start")
           wget.download(sd_url, "Result/Facebook/{}.mp4".format(filemu))
           
           print("\n")
           print("[+] Finish Download")
           print("\n")
           
           
           
   
   @Downloader.url.setter
   def url(self, input):
      self.__url = input
            
   @url.getter
   def url(self):
      return self.__url
      

class Youtube(Downloader):
   
   def Run(self):
   
      os.system("clear")
      print(self.banner.EzWelcome())
      yt = YouTube(self.url, on_progress_callback=on_progress)
      menu = "[1] Youtube MP4\n[2] Youtube MP3\n"
      print(menu)
      cek = input("[+] Masukan Pilihan (1/2): ")
      filenames = yt.title
      if cek == "1":   
         print("\n")
         yt.streams.first().download(output_path="result/Youtube/MP4/",filename=str(filenames))
         done = input("\n\n -> [ Download Finished ! | Press Enter To Exit ... ]")
         print("\n")
      elif cek == "2":
         print("\n")
         outfile = yt.streams.get_audio_only().download(output_path="result/Youtube/MP3/",filename=yt.title)
         os.rename(outfile, "result/Youtube/mp3/"+filenames+"(Music).mp3")
         done = input("\n\n -> [ Download Finished ! | Press Enter To Exit ... ]")
         print("\n")
      else:
         cek = input("[+] Masukan Pilihan(1/2): ")
   
   @Downloader.url.setter
   def url(self, input):
      self.__url = input
            
   @url.getter
   def url(self):
      return self.__url
    
    
class Tiktok(Downloader):


   def Run(self):
     
      os.system("clear")
      print(self.banner.EzWelcome())
      urls = "https://tiktokd.herokuapp.com/tiktok"
      
      ezdata = {"url":self.url}
      ezheader = {"User-Agent":self.browser()}
      r = requests.post(urls, data=ezdata, headers=ezheader)
      ez = json.loads(r.content)

      if ez["status"] == 200 or ez["status"] == "200":
         try:
            outfile = input("[ > ] Save Dengan Nama: ")
            wget.download(ez['data']['link'], 'result/Tiktok/{}.mp4'.format(outfile))
            print("\n")
            done = input("-> [ Download Complete ! | Press Enter To Exit ... ]")
            print("\n")
         except:
            print("Invalid URL")
      else:
         print("Bad Connection")
   
   
   @Downloader.url.setter
   def url(self, input):
      self.__url = input
            
   @url.getter
   def url(self):
      return self.__url
    
    
    
    
    
    

    
    
    
