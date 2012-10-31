""" Copyright (C) 2012 Arpit Chauhan """

""" This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
     

from random import randint
from prime import *


def dec2bin(n):
    return (bin(n)[2:])

def string2ascii_int_list(string):
    ascii_int_list=[]
    for char in string:
        ascii_int_list.append(ord(char))
    return ascii_int_list

def ascii_int_list2string(ascii_int_list):
    string=[]
    for integer in ascii_int_list:
        string.append(chr(integer))
    return ''.join(string)
    
    
def getprime(lower,upper):
    while True:
        num = randint(lower, upper)
        if isprime(num, 2):
            break
    return num 

#Public Key = {e, n} and Private Key = {d, n}
 
def generate_keys(lower=1000, upper=50000):    
    while True:
        p = getprime(lower, upper)
        print 'p = ', p
        q = getprime(lower, upper)
        print 'q = ', q
        n = p * q 
        print 'n = ', n
        phi_n = (p-1) * (q-1)
        print 'phi_n = ', phi_n
        
        e = getrelprime(phi_n)
        print 'e = ', e
        d = modinv(e, phi_n)
        print 'd = ', d
        if d>=2:
            break
    PU = (n, e)
    PR = (n, d)
    print 'd*e mod phi_n = ', pow(d*e, 1, phi_n)
    return (PU, PR)

def rsa_encrypt(plaintext, key):
    n, e = key
    print 'rsa_encrypt'
    plaintext_list = string2ascii_int_list(plaintext)
    ciphertext_list = []
    
    for M in plaintext_list:     
        print 'M = ', M
        C = pow(M, e, n) # pow (a,b[,c]) returns (a**b) mod c
        print 'C = ', C
        ciphertext_list.append(C)
        
    return ciphertext_list
   
    
def rsa_decrypt(ciphertext_list, key):
    print 'rsa_decrypt'
    n, d = key
    plaintext_list = []
    
    for C in ciphertext_list:
        print 'C = ', C, 'd = ', d 
        M = pow(C, d, n)
        print 'M = ', M
        plaintext_list.append(M)
    plaintext = ascii_int_list2string(plaintext_list)
    return plaintext
 
def main():
    plaintext = raw_input('Enter the plaintext: ')
    
    
    PU, PR = generate_keys()
    
    print 'PU = ', PU
    print 'PR = ', PR
    
    ciphertext = rsa_encrypt(plaintext, PU)
    
    print 'ciphertext = ', ciphertext
    
    plaintext_2 = rsa_decrypt(ciphertext, PR)

    print 'plaintext_2 =', plaintext_2
    
main()
  