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

class Youtube(Downloader):
   
   def run(self):
   
      os.system("clear")
      print(self.banner.EzWelcome())
      yt = YouTube(self.url, on_progress_callback=on_progress)
      menu = "\n[1] Youtube MP4\n[2] Youtube MP3\n"
      print(menu)
      cek = input("[+] Masukan Pilihan(1/2): ")
      filenames = yt.title
      if cek == "1":   
         print("\n")
         yt.streams.first().download(output_path="result/Youtube/",filename=str(filenames))
         done = input("\n\n -> [ Download Finished ... ]")
      elif cek == "2":
         print("\n")
         outfile = yt.streams.get_audio_only().download(output_path="result/Youtube/",filename=yt.title)
         os.rename(outfile, "result/Youtube/"+filenames+".mp3")
         done = input("\n\n -> [ Download Finished ... ]")
      else:
         cek = input("[+] Masukan Pilihan(1/2): ")
   
   @Downloader.url.setter
   def url(self, input):
      self.__url = input
            
   @url.getter
   def url(self):
      return self.__url