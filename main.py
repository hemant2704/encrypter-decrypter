from tk_gui import *
from en_de_function import *



#function to display the output in GUI
def showMsg():
	out=", "
	disp_out.insert(0,out)
	try:
		inp=t1.get(1.0, "end-1c")
		#select the required function
		cmd=comboOneTwoPunch.get()
		if cmd=='String to Binary':
			out=str_to_bin(inp)

		elif cmd=='Binary to String':
			out=bin_to_str(inp)

		elif cmd=='Decimal to Binary':
			out=dec_to_bin(int(inp))

		elif cmd=='Binary to Decimal':
			out=bin_to_dec(inp)

		elif cmd=='Frequency analysis':
			out=freq_analysis(inp)

		elif cmd=='Reverse String':
			out=rev_str(inp)

		elif cmd=='ROT13 Encode':
			out=str_to_caesar(inp,13)

		elif cmd=='ROT13 Decode':
			out=caesar_to_str(inp,13)

		elif cmd=='base64 Encode':
			out=str_to_base64(inp)

		elif cmd=='base64 Decode':
			out=base64_to_str(inp)

		elif cmd=='md5 hashing':
			out=str_to_md5(inp)

		elif cmd=='salted md5 hashing':
			out=str_to_saltedmd5(inp)

		elif cmd=='sha1 hashing':
			out=str_to_sha1(inp)

		elif cmd=='sha256 hashing':
			out=str_to_sha256(inp)

		elif cmd=='sha512 hashing':
			out=str_to_sha512(inp)

		else: out="error!"
		#showing output in messagebox
		messagebox.showinfo('Output',out)
	except:
		out="some error occured"
	#showing output in output field
	disp_out.insert(0,out)

