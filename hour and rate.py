def computepay(h,r):   
    if (h > 40):
        pay = (h-40)*1.5*r+(40*r)
  	else :
    	pay = (h*r)
     return pay
try:
    hrs = raw_input("Enter Hours:")
	rat = raw_input("Enter Rate:  ")
	hour = float(hrs)
	rate = float(rat)
except
	print "please enter a number"
    quit()
print computepay(h,r)
