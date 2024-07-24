import md5, md2, sha1, sha256, sha224, sha384, sha512



print("0 : MD5\n1 : MD2&MD4\n2 : SHA-1\n3 : SHA-256\n4 : SHA-224\n5 : SHA-384\n6 : SHA-512")
choice1 = input("Choice An Option: ")
if(choice1 == "0"):
	md5.main()
elif(choice1 == "1"):
	md2.main()
elif(choice1 == "2"):
	sha1.main_sha1()
elif(choice1 == "3"):
	sha256.main()
elif(choice1 == "4"):
	sha224.main_sha224()
elif(choice1 == "5"):
	sha384.main_sha384()
elif(choice1 == "6"):
	sha512.main_sha512()
else:
	print("we not get there yet or you choose an invalid option")

