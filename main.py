def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select mode.")
print("0.pengiraan mudah")
print("1.pengiraan sains tenaga dan kuasa")
choice = input("masukan mode: ")
if choice == '0':
	print("1.tambah")
	print("2.tolak")
	print("3.darab")
	print("4.bahagi")
	choice1 = input("masukan operasi: ")
	num1 = float(input("nombor pertama: "))
	num2 = float(input("nombor kedua: "))
	
	if choice1 == '1':
	    print(num1, "+", num2, "=", add(num1, num2))
	
	elif choice1 == '2':
	    print(num1, "-", num2, "=", subtract(num1, num2))
	
	elif choice1 == '3':
	    print(num1, "*", num2, "=", multiply(num1, num2))
	
	elif choice1 == '4':
	    print(num1, "/", num2, "=", divide(num1, num2))
	else:
	    print("Invalid Input")
		
elif choice == '1':
	
	print('1.formula kerja')
	print('2.formula kuasa')
	choice2 = input("masukan mode: ")
	
	if choice2 == '1':
		num1 = float(input("berat (kg): "))
		num2 = float(input("jarak (meter): "))
		newton = ( multiply(num1, 10))
		newton = float(newton)
		jawapan = multiply (newton , num2)
		print(jawapan,'joule(j)')
		
	elif choice2 == '2':
		num1 = float(input("kerja (joule): "))
		num2 = float(input("masa (saat): "))
		jawapan2 = ( divide(num1, num2))
		print(jawapan2,'watt(w)')


