## original code from : http://dann.com.br/alexctf2k17-crypto100-many_time_secrets/

import string
import collections
import sets
import sys




#cipher text:  O_\ULY]T@SP_FDYBTTGJS
c1 = "7f4f105f5c55194c595d5411405350185f4612445919425454474a5313151810"


#cipher text1:  _W^I\]SUXEPALAZ^E^_RQE_]WT
c2 =  "5f575e49125c5d53551058451050414c16415a5e45195e5f521251455f5d5754"


#cipher text:  TSU\A@PUCTCBQ[BE__ZY^ARGQM^
c3 =  "5453555c41104050551043544342515b4215455f5f5a59115e41185247514d5e"


#cipher text:  \Y\[]]LD^GZULTZWWRV\R]VC
c4 =  "5c59105c5b5d5d4c10445e11475a554c1654125a57571152565c18525d145643"


#cipher text:  kYE_EGLRTDZQU]SYQ\HXGA[GQ
c5 =  "6b5945105f45474c10525411445a5118555d5359515c1148584718415b475111"


#cipher text:  f^YCYGQETCFWPF_St\R@_S\W@
c6 =  "665e59431259471851104554434614575015465f5319745c52405f535c574011"


#cipher text:  f^_EAQZ\C^WQUVRYWDZP_P]Z[SQE
c7 =  "665e5f4541515a5c43105e571051555652595744165a505f17505d5a5b535145"


#cipher text:  {PI_GXWFUEX]G]BZXU^GRWBZQKB
c8 =  "7b50495f4710585746551145585d475d16425a5816555e47521257425a514b42"

ciphers = [c1, c2, c3, c4, c5, c6, c7,c8]


def strxor(a, b):     # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

# To store the final key
final_key = [None]*150
# To store the positions we know are broken
known_key_positions = set()



for current_index, ciphertext in enumerate(ciphers):
	counter = collections.Counter()
	# for each other ciphertext
	for index, ciphertext2 in enumerate(ciphers):
		if current_index != index: # don't xor a ciphertext with itself
			for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): # Xor the two ciphertexts
				# If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)
				if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 # Increment the counter at this index
	knownSpaceIndexes = []

	# Loop through all positions where a space character was possible in the current_index cipher
	for ind, val in counter.items():
		# If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!
		if val >= 7: knownSpaceIndexes.append(ind)
	#print knownSpaceIndexes # Shows all the positions where we now know the key!

	# Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!
	xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)
	for index in knownSpaceIndexes:
		# Store the key's value at the correct position
		final_key[index] = xor_with_spaces[index].encode('hex')
		# Record that we known the key at this position
		known_key_positions.add(index)

# Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)
final_key_hex = ''.join([val if val is not None else '00' for val in final_key])

output = strxor(c6.decode('hex'),final_key_hex.decode('hex'))

print ("Fix this sentence: 6")
#print ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])+"\n"
print (''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])+"\n")

target_plaintext = "This is a test of the Emergency "
print ("Fixed:")
print (target_plaintext+"\n")

key = strxor(c6.decode('hex'),target_plaintext)

print ("Decrypted msg:")
for cipher in ciphers:
	print strxor(cipher.decode('hex'),key)

print "\nPrivate key recovered: "+key+"\n"
