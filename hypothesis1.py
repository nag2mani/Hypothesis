'''
have a function for checking vowels in word

Author : Nagmani Kumar
Date :November 12,2022
'''
def number_vowels(word):
    a=word.count('a') + word.count('A')
    e=word.count('e') + word.count('E')
    i=word.count('i') + word.count('I')
    o=word.count('o') + word.count('O')
    u=word.count('u') + word.count('U')
    #print(a+e+i+o+u)
    return(a+e+i+o+u)

def sol_number_vowels(word):
	a=word.count('a') + word.count('A')
	e=word.count('e') + word.count('E')
	i=word.count('i') + word.count('I')
	o=word.count('o') + word.count('O')
	u=word.count('u') + word.count('U')
	# print(a+e+i+o+u)
	return(a+e+i+o+u)

from hypothesis import given, strategies as st,settings

@settings(max_examples=1000)
@given(st.text(min_size=3))
def test_number_vowels(word):
    assert number_vowels(word)==sol_number_vowels(word)

#go beyond the human goes.
#work for fruitful and proceser fun.
#pytest only work for fruitful fun.
#doctest both fruitful and processer function ke liye work karega.
#agar kuchh return nhi ho rha then none hoga.


	