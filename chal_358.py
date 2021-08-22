"""

https://www.reddit.com/r/dailyprogrammer/comments/8eger3/20180423_challenge_358_easy_decipher_the_seven/

[2018-04-23] Challenge #358 [Easy] Decipher The Seven Segments
Description

Today's challenge will be to create a program to decipher a seven segment display, commonly seen on many older electronic devices.
Input Description

For this challenge, you will receive 3 lines of input, with each line being 27 characters long (representing 9 total numbers), with the digits spread across the 3 lines. Your job is to return the represented digits. You don't need to account for odd spacing or missing segments.
Output Description

Your program should print the numbers contained in the display.
Challenge Inputs

    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

    _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_ 
  | _| _||_||_| _||_||_  _|

 _  _  _  _  _  _  _  _  _ 
|_  _||_ |_| _|  ||_ | ||_|
 _||_ |_||_| _|  ||_||_||_|

 _  _        _  _  _  _  _ 
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ 

Challenge Outputs

123456789
433805825
526837608
954105592

"""

def decode(txt):

	digit_map = { 	' _ | ||_|' : '0',
					'     |  |' : '1',
					' _  _||_ ' : '2',
					' _  _| _|' : '3',
					'   |_|  |' : '4',
					' _ |_  _|' : '5',
					' _ |_ |_|' : '6',
					' _   |  |' : '7',
					' _ |_||_|' : '8',
					' _ |_| _|' : '9'}

	out = ''
	span   = len(txt)//3
	for i in range(span//3):
		c = ''.join([txt[i*3+j*span:i*3+j*span+3] for j in range(3)])
		out += '?' if c not in digit_map else digit_map[c]
	return out

def encode(digits):

	digit_map = { 	'0' : ' _ | ||_|',
					'1' : '     |  |',
					'2' : ' _  _||_ ',
					'3' : ' _  _| _|',
					'4' : '   |_|  |',
					'5' : ' _ |_  _|',
					'6' : ' _ |_ |_|',
					'7' : ' _   |  |',
					'8' : ' _ |_||_|',
					'9' : ' _ |_| _|'}

	if not set(digits).issubset(set("0123456789")):
		raise Exception("Invalid chars to encode!")
		exit()
	
	for span in range(3):
		row = ''
		for digit in digits:
			row += digit_map[digit][span*3:span*3+3]
		print(row)

l1 = "    _  _     _  _  _  _  _ "
l2 = "  | _| _||_||_ |_   ||_||_|"
l3 = "  ||_  _|  | _||_|  ||_| _|"

print(decode(l1+l2+l3))

l1 = "    _  _  _  _  _  _  _  _ "
l2 = "|_| _| _||_|| ||_ |_| _||_ "
l3 = "  | _| _||_||_| _||_||_  _|"

print(decode(l1+l2+l3))

l1 = " _  _  _  _  _  _  _  _  _ "
l2 = "|_  _||_ |_| _|  ||_ | ||_|"
l3 = " _||_ |_||_| _|  ||_||_||_|"

print(decode(l1+l2+l3))

l1 = " _  _        _  _  _  _  _ "
l2 = "|_||_ |_|  || ||_ |_ |_| _|"
l3 = " _| _|  |  ||_| _| _| _||_ "

print(decode(l1+l2+l3))

encode("123456789")
encode("433805825")
encode("526837608")
encode("954105592")

