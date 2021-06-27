# Multiple In heritance
class A:
 def akhilesh(self):
  print "akhilesh student of class A"
class B:
 def abhijeet(self):
  print "abhijeet student of class B"
class C(A,B):
 def satwik(self):
  print "satwik student of class C"
D=C()
D.satwik()
D.abhijeet()
D.akhilesh()