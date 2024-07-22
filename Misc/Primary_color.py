primarycolor_1=input("Enter primary color:")
primarycolor_2=input("Enter primary color:")
if (primarycolor_1=="red" and primarycolor_2=="blue") or (primarycolor_1=="blue" and primarycolor_2=="red"):
	print(f"When you mix {primarycolor_1} and {primarycolor_2}, you get purple.")
elif (primarycolor_1=="red" and primarycolor_2=="yellow") or (primarycolor_1=="yellow" and primarycolor_2=="red"):
	print(f"When you mix {primarycolor_1} and {primarycolor_2}, you get orange.")
elif (primarycolor_1=="blue" and primarycolor_2=="yellow") or (primarycolor_1=="yellow" and primarycolor_2=="blue"):
	print(f"When you mix {primarycolor_1} and {primarycolor_2}, you get green.")
else: 
	print("You didn't input two primary colors.")