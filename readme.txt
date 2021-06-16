Flames is a relationship calculating algorithm popular between the youngsters in India (or atleast it was popular back in the 90s, 90s kids will know). At the time of schooling or even graduation everyone might heard about this and many of them tried out this secretly. Some took this as very serious. 🤭️️ 

Anyways, here's my giving back to the silly game of my childhood

FLAMES stand for:
F - Friendship
L - Love
A - Affection
M - Marriage
E - Enemy
S - Sibling

The whole logic consists mainly two steps:

     1.Get the flames count
        Take the two names ('asd' and 'abcd')
        Remove the common characters (two common characters 'a', 'd')
        Get the count of the characters that are left (Removed a,d and the rest are s,b,c. 
				So total 3.)
     2.Get the flames result
        We take FLAMES letters ('F', 'L', 'A', 'M', 'E', 'S')
        And start removing letters using the flames count we got.
        And the letter which last the process is the result.
	
In our example we got flames count = 3. So first we takes FLAMES.
FLAMES
Then we start count from left up to flames count 3. Then remove the letter which is in the position 3. In this case it is 'A'. So the letters become:
FLMES
Then we start count again from the letter which is removed ie, from 'M'. So the next character to remove is 'S'. So our letters become:
FLME
After next step:
FLE
Then:
FE
Last:
F

So the result is Friends.

P.S- I am complete beginner at python so the code I have written might not be efficient or clean. Apologies for that.


created with ❤️ by dims88