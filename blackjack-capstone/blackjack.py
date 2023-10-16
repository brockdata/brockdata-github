## DAY 11
# CAPSTONE: build a blackjack game
# normal rules, but dealer must draw again if lower than 17
def blackjack():
    import random
    cards = {
        'numcards':['2','3','4','5','6','7','8','9','10'],
        'royals':['J','Q','K','A'],
        'suits':['d','c','h','s'],
        'Aces':['Ad','Ah','Ac','As']
             }
    ## build the deck
    deck = []
    for card in cards['numcards']:
        for suit in cards['suits']:
            deck.append(card+suit)
    for card in cards['royals']:
        for suit in cards['suits']:
            deck.append(card+suit)

    ## functions
    def cardsum(hand):
        """input hand as list
        return sum"""
        indxHand = []
        for card in hand:
            suitx = card[-1]
            cardNum = card.replace(suitx,'')
            if cardNum == 'A':
                cardNum = '11'
            elif cardNum in cards['royals'] and cardNum != 'A':
                cardNum = '10'
            indxHand.append(cardNum)
        for n in range (0,len(indxHand)):
            indxHand[n] = int(indxHand[n])
        return sum(indxHand)

    def hitme(hand):
        '''select random card, remove from deck, append to hand
        return hand'''
        randCard = deck[random.randint(0, len(deck)-1)] #select random card
        deck.remove(randCard) #remove random card from deck
        hand.append(randCard) #append random card to hand
        return hand

    def aces(hand):
        '''input hand, check for aces, replace the first one found
        return hand'''
        for ace in cards['Aces']: #find ace
            if ace in hand:
                hand[hand.index(ace)] = '1x' #convert to one
                print('~aces converted to ones!~')
        return hand

    ## starting deal
    yourHand = []
    dealerHand = []
    dealerHand_view = []
    for n in range(0,2):
        randCard = deck[random.randint(0, len(deck) - 1)]
        yourHand.append(randCard)
        deck.remove(randCard)
        randCard = deck[random.randint(0, len(deck) - 1)]
        dealerHand.append(randCard)
        deck.remove(randCard)
    dealerHand_view.append(dealerHand[0])
    dealerHand_view.append('[ ]')
    yourSum = cardsum(yourHand)
    dealerSum = cardsum(dealerHand)
    print(f'your hand: {yourHand}')
    print(f'your total: {yourSum}')
    print(f'dealer\'s hand: {dealerHand_view}')
    ## let the game begin!
    youbust = False
    dealerbust = False
    playing = True
    while playing:
        youStay = False
        dealerStay = False
        hit = input('\nhit or stay? ') #your turn
        if hit != 'hit' and hit != 'stay':
            while hit != 'hit' and hit != 'stay':
                print('please enter a valid response')
                hit = input('\nhit or stay? ')
        if hit == 'hit':
            hitme(yourHand)
            yourSum = cardsum(yourHand)
        else:
            print('you will stay')
            yourSum = cardsum(yourHand)
            youStay = True
        if yourSum > 21:
            aces(yourHand)
            yourSum = cardsum(yourHand)
            if yourSum > 21:
                youbust = True
                print('you BUST!')
                break
        dealerSum = cardsum(dealerHand) #dealer turn
        if dealerSum <= 17:
            print('dealer hit')
            hitme(dealerHand)
            dealerHand_view.append('[ ]')
            dealerSum = cardsum(dealerHand)
        else:
            print('dealer will stay')
            dealerSum = cardsum(dealerHand)
            dealerStay = True
        if dealerSum > 21:
            aces(dealerHand)
            dealerSum = cardsum(dealerHand)
            if dealerSum > 21:
                dealerbust = True
                print('dealer BUST!')
                break
        if youStay and dealerStay:
            break
        print(f'\nyour hand: {yourHand}\nyour total: {yourSum}')
        print(f'dealer hand: {dealerHand_view}')
    # game over
    print('\nGAME OVER')
    print(f'your final hand: {yourHand}\nyour final total: {yourSum}')
    print(f'dealer\'s final hand: {dealerHand}\ndealer\'s final total: {dealerSum}')
    if youbust:
        for n in range(0, 5):
            print('...lose...')
    elif dealerbust:
        for n in range(0, 5):
            print('!!!WIN!!!')
    elif yourSum > dealerSum:
        if yourSum <= 21:
            for n in range (0,5):
                print('!!!WIN!!!')
        else:
            for n in range(0, 5):
                print('...lose...')
    elif yourSum == dealerSum:
        for n in range (0,5):
            print('---tie---')
    else:
        if dealerSum <= 21:
            for n in range(0, 5):
                print('...lose...')
gameon = True
while gameon:
    if input('do you  want to play blackjack? ') != 'y':
        gameon = False
    blackjack()