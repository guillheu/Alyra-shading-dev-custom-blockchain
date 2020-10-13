from Block import *

#for a better difficulty granularity, we can retreive the hash as a binary value instead of a hex value
target = "00000"

#this function will keep incrementing the salt/nonce of the block until we get the right hash
def mine(block):

    #run until the hash of the block starts with the target string ("00000")
    #the longer the target string, the longer it will take to find an hash conform to the target, and the higher the difficulty
    while(not block.hash.startswith(target)):

        #incrementing the salt/nonce of the block
        block.salt+=1

        #displaying the current hash of the block (only for convenience sake, should not be implemented in production for performance concerns)
        print(block.hash)






#testing a new empty block
mine(Block(1, "", "", ""))
