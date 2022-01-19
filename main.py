# ASCII artwork provided by https://ascii.co.uk/art

print('''
                  _________________
             ____/#################\____
         ___/################,##########\___
       _/################/##/ \##\##########\_
      /#################/\##| |##/\###########\
     /##################\ \#| |#/ /############\
    |##DWB###############\ \| |/ /#########JRB##|
    |####################{{{\ /}}}##############|
    |###################{{<.> <.>}}#############|
    |#####################{ | | }###############|
    |#####################{ | | }####_#######__#|
    |#####################/_| |_\##_( )###__(  )_
    |####################{(_)_(_)}(  ` )_( '__ ` )
    |#####################{VV_VV}##(__( `)_(  )-` )
    |#####################\^^))^/######(   )_')  )
    |######################--((-########( ' _)__)
    |########################))##########(__)###|
    |########################(##################|
    |###########################################|
    |###########################################|
    |###########################################|
    |###########################################|
\ | /########| |################################| \ | /
_\|/|#######/   \####################\|/########|__\|/___
            \   /
             \ /
              V
''')

print("Welcome to Treasure Haven")
print(
    "You have been tasked with finding the dragon's treasure and making it back alive. Let's go!"
)

first_path = input("You have just stepped off your ship. Do you want to go 'right' or 'left'?\n").lower()

if first_path == "left":
        second_path = input("You come to a massive lake. Do you 'wait' for a boat to take you across or 'swim' to the shore?\n").lower()
        if second_path == "wait":
                third_path = input("After hopping off the boat, you enter a castle with three large, wooden doors. Each painted a different color. Do you walk through 'red', 'blue', 'yellow'?\n").lower()
                if third_path == "red":
                    print("Ouch! You walked right into a dragon yawn. Let's just say the only way you'll be attending a hero's banquet is as the dinner.")
                elif third_path == "yellow":
                    print("Holy Moly! You've done it!! The dragon was so scared it flew away and left you its treasure. You are the champion!!")
                elif third_path == "blue":
                    print("Oh dear! The dragon must have been hungry because it ate you before you even knew what hit you. That's a plus, I suppose.")
                else:
                    print("Not sure where you thought you were going. I'd imagine you weren't looking for a death trap. Alas, here we are. Game Over.")
        else:print("You were closer than if you would have stayed on the ship. But you're still dead!")
else:
    print("The dragon would have eaten you, but you fell into a bottomless pit instead. You died, but at least you weren't eaten.")
