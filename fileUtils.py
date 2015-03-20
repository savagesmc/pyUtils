import os
import hashlib

# returns an md5 has of the given file
def md5(fname, block_size=2**20):
   with open(fname, "r") as f:
      md5 = hashlib.md5()
      while True:
         data = f.read(block_size)
         if not data:
            break
         md5.update(data)
   return md5.hexdigest()

# returns a list of all the files (recursive) within the provided path
def recurse(rootPath):
   result = set()
   for root, subFolder, files in os.walk(rootPath):
      r = root
      for s in subFolder:
         p = os.path.join(r, s)
         result = result.union(recurse(p))
      for i in files:
        p = os.path.join(r, i)
        result.add(p)
   return result

if __name__ == "__main__":
   filenames = recurse(os.getcwd())
   for f in filenames:
      print "{:s}".format(f)
