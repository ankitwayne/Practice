#Over-ridingclass m1:
 def display(self):
  print "Display is of class m1"
 def disp(self):
  print "Disp is of class m1"
class m2(m1):
 def display(self):
  print "Display is of class m2"
 def dis(self):
  print "Dis is of class m2"
m=m2()
m.dis()
m.disp()
m.display()
