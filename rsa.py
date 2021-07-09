import math

def isPrime(n):
	if n % 2 == 0 and n > 2: 
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

print("RSA")
print("Nhập 2 số nguyên tố a và b")

p = int(input("Nhập p: "))
q = int(input("Nhập q: "))


def rsa():
	if(not isPrime(p) or not isPrime(q)):
		print("p hoặc q không là SNT")
		return 

	n = p*q
	phi_n = (p-1)*(q-1)

	gcdList = []

	for i in range(phi_n):
		if(math.gcd(i,phi_n) == 1):
			gcdList.append(i)

	print("Chọn số e là một trong các số sau: ")
	print(gcdList)

	e = int(input("Chọn e: "))

	if(e not in gcdList):
		print('Số e bạn chọn không nằm trong dãy')
		return
	
	print(e)

	print("d = (x*phi_n + 1)/e")

	print("d = x*{0} + 1/{1}".format( phi_n, e))

	print('{0}d = {1}x + 1'.format(e, phi_n))

	x = 1
	d = 0

	while d == 0 or x > phi_n:
		toan = (phi_n*x + 1)/e
		if(toan == int(toan)):
			d = toan
		else:
			x+=1

	if(d==0):
		print('Không tìm được')
	else:
		print("Khoá công khai: n={0}, e={1}".format(n,e))
		print("Khoá bí mật d={0}".format(int(d)))

rsa()
