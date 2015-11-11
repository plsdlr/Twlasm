from Crypto.Hash import SHA256
import tweepy, time, sys
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

hashlist = []
wholemessage =[]

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

#____________________ Clases
#__________ message

class MyMessageListener(tweepy.StreamListener):

    def __init__(self, api=None):
        super(MyMessageListener, self).__init__()
        self.num_tweets = 0


    def on_error(self, status):
        print(status)

    def filtermessage(self,message):
            a = message.find("#")
            wholemessage.append(message[0:a-1])

    def hashcomparison(self,newhash,message):
        global hashlist
        if newhash == str(hashlist[0]):
            self.num_tweets += 1
            print ">>>>> found Message <<<<<"
            print ">>>>>>>>>>>>>>>>>>>"+str(message)+"<<<<<<<<<<<<<<<<<<<<<<<<"
            self.filtermessage(message)
        else:
            print ">> not the Message <<"


    def decrypt(self,message):
        hash = SHA256.new()
        hash.update(message.encode('ascii', 'ignore'))
        self.hashcomparison(hash.hexdigest(),message)


    def on_status(self, status):
        if self.num_tweets < 1:
            print (status.text)
            self.decrypt(status.text)
            return True
        else:
            return False


#__________ hash

class MyHashListener(tweepy.StreamListener):

    def __init__(self, api=None):
        super(MyHashListener, self).__init__()
        self.num_tweets = 0

    def on_status(self, status):
            del hashlist[:]           #cleans old hash
            print (status.text)
            hashlist.append(status.text)
            return False

    def on_error(self, status):
            print(status)


#____________________ mainfunctions

#_____________calling Messagelisterner

def startlistneruser():
    global CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET
    l = MyMessageListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, l)
    try:
        ">>>>> start listening to stream <<<<<"
        stream.filter(track=['yolo'])
        api.update_status(status = Message)
    except:
        print ">>>>> disconect this stream <<<<<"
        stream.disconnect()

#_____________calling hashlisterner

def starthashlistener():
    global CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET
    a = MyHashListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, a)
    try:
        print ">>>>> start catching hash <<<<<"
        stream.filter(follow=['4091042235'])
        api.update_status(status = Message)
    except:
        print ">>>>> disconect this stream <<<<<"
        stream.disconnect()

def printmessage():
    global wholemessage
    b=""
    d = b.join(wholemessage)
    print ">>>>>>>>>>>>>>>>>>> current message : "+d+"<<<<<<<<<<<<<<<<<<<<<<<<"

print ""
print ""
print "Chaffing and winnowing Twitter 0.01"
print "Listner Program"

while True:
    starthashlistener()
    print ">> change stream / 20 seconds <<"
    time.sleep(18)
    startlistneruser()
    print ">> change stream / 20 seconds <<"
    time.sleep(18)
    printmessage()
    pass
