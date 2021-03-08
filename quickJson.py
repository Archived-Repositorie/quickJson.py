import json
import os

class File:

     def __init__(self, path):

         if not os.path.exists(path):
             fil = open(path, "a")
             fil.close()

         self.path = path
         self.fileR = open(self.path, "r")
         self.content = self.fileR.read()

         if not self.content.startswith("{"):
             self.content = "{}"

         self.data = json.loads(self.content)


     def set(self,name,value):

         try:
             self.data[name]
         except KeyError as err:
             self.data[name] = ""

         self.fileW = open(self.path, "w")
         self.data[name] = value
         self.fileW.write(json.dumps(self.data))

         return self.data[name]


     def get(self, name):

         try:
             self.data[name]
         except KeyError as err:
             self.data[name] = ""

         return self.data[name]


     def delete(self, name):

         try:
             self.data[name]
         except KeyError as err:
             self.data[name] = ""

         self.fileW = open(self.path, "w")
         self.data[name] = ""
         self.fileW.write(json.dumps(self.data))

         return None


     def add(self, name, value):

         try:
             self.data[name]
         except KeyError as err:
             self.data[name] = ""

         self.fileW = open(self.path, "w")
         self.data[name] += value
         self.fileW.write(json.dumps(self.data))

         return self.data[name]