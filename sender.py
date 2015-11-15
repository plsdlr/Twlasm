from Crypto.Hash import SHA256
import tweepy, time, sys,random

random.seed()
rawuserinput = ""
string = ""
hashstring =""
hashtag="#yolo"

#_____________________

#First Key fill in correctly
CONSUMER_KEY1 = ''
CONSUMER_SECRET1 = ''
ACCESS_KEY1 = ''
ACCESS_SECRET1 = ''

#Second Key fill in correctly
CONSUMER_KEY2 = ''
CONSUMER_SECRET2 = ''
ACCESS_KEY2 = ''
ACCESS_SECRET2 = ''


def userinput():
    print ""
    print "***** enter your message *****"
    global rawuserinput
    rawuserinput = raw_input()
    pass


def checkstring():
    global rawuserinput
    global string
    try:
        if len(rawuserinput) < 140:
            string = str(rawuserinput)
            print "***** valid string *****"
            print ""
        else:
            string = str(rawuserinput)[0:139]
            print "string to long / cut it to 140 character"
    except:
        print "enter valid string"

    pass


def cutter():
    packetsize = 4
    global string
    for i in range(0,len(string),packetsize):
        testcut = string [i:i+packetsize]
        print ""
        print "Next String Part : " + testcut
        print ""
        createhash(testcut)

def createhash(testcut):
    global hashtag
    print "***** createhash *****"
    fullstring =testcut+" "+hashtag
    print "Tweet : " + fullstring
    hash = SHA256.new()
    hash.update(fullstring)
    hashstring =  hash.hexdigest()
    print hashstring
    time.sleep(70)
    postmessage(CONSUMER_KEY2,CONSUMER_SECRET2,ACCESS_KEY2,ACCESS_SECRET2,hashstring)
    print ">>>>> Hash send <<<<<"
    print ""
    time.sleep(70)
    postmessage(CONSUMER_KEY1,CONSUMER_SECRET1,ACCESS_KEY1,ACCESS_SECRET1,fullstring)
    print ">>>>> Message send <<<<<"
    print ""



def postmessage(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET,Message):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    #print api
    api.update_status(status = Message)

def funtext():
    print " _____       _                  ___   ___ ___   "
    print "|_   _|_ _ _| |___ ___ _____   |   | |   |_  |  "
    print "  | | | | | | | .'|_ -|     |  | | |_| | |_| |_ "
    print "  |_| |_____|_|__,|___|_|_|_|  |___|_|___|_____| "

print ""
print ""
print "Chaffing and winnowing Twitter 0.01"
print "Send Program"

def mainfunction():
    userinput()
    checkstring()
    cutter()
#    createhash()
#postmessage(CONSUMER_KEY1,CONSUMER_SECRET1,ACCESS_KEY1,ACCESS_SECRET1,hashstring)

funtext()
mainfunction()

