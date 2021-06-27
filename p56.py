# Multiple inheritamce
class m1:
 def display(self):
  print "Display method of class m1"
class m2(m1):
 def rohit(self):
  print "Display method of class m2"
class m3(m2):
 def Ankit(self):
  print "Display method of class m3"
m=m3()
m.Ankit()
m.rohit()
m.display()