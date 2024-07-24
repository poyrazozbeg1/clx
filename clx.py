import md5


print("0 : MD5\n1 : MD2&MD4\n2 : SHA-1\n3 : SHA-256\n4 : SHA-224\n5 : SHA-384\n6 : SHA-512")
choice1 = input("Choice An Option: ")
if(choice1 == "0"):
	md5.main()
elif(choice1 == "0"):
	md2.main()
elif(choice1 == "0"):
	sha1.main()
elif(choice1 == "0"):
	sha256.main()
elif(choice1 == "0"):
	sha224.main()
elif(choice1 == "0"):
	sha384.main()
elif(choice1 == "0"):
	sha512.main()
else:
	print("we not get there yet or you choose an invalid option")

