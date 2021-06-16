import time
print(r""""


                               )
                               (
                 (            ( )
                 )             "
                ( )
                 "    |          |
             |       ((          ))
       |     ))      ))   )     //
       ))   ( )     / /   (    ( (     |
       .(    \ \   ( (   ( )   )  )    ))
      ( (     ) '.'   '.  "  .'   /   ( \
       ) \  .'          '._.'     '._  ) )
       :  '' _.oooooo._   _.oooooo._ ''  /
        )  .odOOOOOOOObo.odOOOOOOOObo.   |
       /  dOOOY dOOOOOOOOOOOOOOOOOOOOOb  (
         OOOY dOOOOOOOOOOOOOOOOOOOOOOOOO  \
        dOOY dOOOOOOOOOOOOOOOOOOOOOOOOOOb
        OOO dOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOO YOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        YOOb OOOOOOOOOOOOOOOOOOOOOOOOOOOY
         YOObdOOOOOOOOOOOOOOOOOOOOOOOOOY
          YOOOOOOOOOOOOOOOOOOOOOOOOOxXY
           "YOOOOOOOOOOOOOOOOOOOOOxXY"
             "YOOOOOOOOOOOOOOOOOAoS"
               YOOOOOOOOOOOOOxXXXY
                "YOOOOOOOOOxXXXY"
                   "YOOOXXXXY"
                      ""Y""

""")

print ("Welcome to Flames love calculator💘️")

name1 = input("Enter your name\n")
name2 = input("Enter their name\n")

# combining the names and removing any spaces
combinedname = (name1 + name2).replace(" ","")

# removing repeating characters
aa = [ ch  for i, ch in enumerate(combinedname) if ch not in combinedname[:i]]
revisedname = ''.join(aa)

# counting the number of letters left
count = len(revisedname)
flames_list = ['F', 'L', 'A', 'M', 'E', 'S']
print(f"\n{flames_list} \n\n")
time.sleep(1)
i = 1
x = 5 
while i < 6:
	num = count % (x+1)
	popped =  flames_list.pop(num-1)
	
	#creating a new revised list that has FLAMES rearragned according to the last removed letter
	if num != 1:

	 flames_list= flames_list[(0-(x-num+1)):] + flames_list[:(0-(x-num+1))]


	print(f"{flames_list} ------> {popped} popped")
	i += 1
	x -= 1
	time.sleep(1)
	print("\n")

#printing relevant messages according to the last element
if flames_list[0] == 'F':
	print('\033[1m' + '\nFriendship 😏️ \n')
	print("Friends (with benfits) is another way of saying good enough to hang with, good enough to be lay with, but never good enough to be with.")
if flames_list[0] == 'L':
	print('\033[1m' + '\nLove ❤️ \n')
	print("It was always her.")
if flames_list[0] == 'A':
	print('\033[1m' + '\nAffection 😍️ \n')
	print("Affection is responsible for nine-tenths of everything that is solid and durable in all the relationships there are.")
if flames_list[0] == 'M':
	print('\033[1m' + '\nMarriage 💌️ \n')
	print("A marriage requires falling in love many times, always with the same person.")
if flames_list[0] == 'E':
	print('\033[1m' + '\nEnemy 😨️ \n')
	print("People can be lovers and enemies at the same time, you know.")
if flames_list[0] == 'S':
	print('\033[1m' + '\nSibling 😱️ \n')
	print("You could be a Lannister, but this is not a tv show.")	

