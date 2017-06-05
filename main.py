#!/usr/bin/env python

# how pub priv key encryption works 
# generate two big primes and take max
# 13(prime1) * 7(prime2) = 91 (max)
# choose public key = 5 
# from https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm  + pub key + prime1 + prime2
# calcuate
# private key = 29 

#NOTE: the original text value cannot be greated than 91

# see magic happen
max = 91
orig = 31

################ NOTE: only public key shared ##############################
publicKey = 5
encoded = 1
for  x in range (publicKey):
	encoded = encoded*orig
	encoded = encoded%max
print ("encoded value = %s", encoded )
############################################################################


################ NOTE: only private key shared ##############################
decoded = 1
privateKey = 29
for  x in range (privateKey):
	decoded = decoded*encoded
	decoded = decoded%max
print ("decoded value = %s", encoded )
############################################################################
# BUT STILL SHARING  "max" ???
