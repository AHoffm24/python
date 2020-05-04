# 
# Example file for retrieving data from the internet
#
import urllib.request #allows for http request

def main():
  URL = urllib.request.urlopen("http://www.google.com")
  print("result code: " + str(URL.getcode()))
  data = URL.read() #reading entire contents of the url to data and printing it. Returns html of the webpage. 
  print(data)

if __name__ == "__main__":
  main()
