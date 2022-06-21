import pyautogui

print('Hello')
print(1+2+3)

#add start + start+1 + ... + end
def add(start,end):
	result=0
	
	for i in range(start,end+1):
		result+=i
	
	return result

print(add(1,10))

#https://pyautogui.readthedocs.io/en/latest/quickstart.html
pyautogui.moveTo(100,100,2)#move to 100,100 in 2 seconds
pyautogui.click(x=200,y=100)#click at 200,100
