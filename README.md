# Twlasm 0.01
A small fun project and a paraphrase of "Plasm: not a crime".
https://vimeo.com/11793767

A proof of concept implementation of Chaffing and winnowing technique in twitter. (with bots)
The Sender types the message. A hash of the message gets tweeted by public hash bot. The original message gets split and tweeted together with a twitter hashtag, which works as a kind of key, by a variable number of bots. The receiver scrapes the hash from the hashbot and opens a stream of the hashtag. It then calculate live hashes of every message in the stream and can filter the message out of the stream.

Needs at minimum 3 Twitter api keys to work basic.
Might get stem in next version.

See also : https://en.wikipedia.org/wiki/Chaffing_and_winnowing
