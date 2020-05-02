#
# Example file for working with conditional statements
# 

def main():
  x, y = 1000, 100
  
  # conditional flow uses if, elif, else; switch cases do not exist in python
  if(x < y):
      string = "x is less than y"
  elif(y < x):
      string = "x is greater than y"
  else:
      string = "x is equal to y"
  print(string)  
  # conditional statements let you use "a if C else b"
  string = "x is less than y" if (x < y) else "x is greater than or equal to y"   
  print(string)
if __name__ == "__main__":
  main()
