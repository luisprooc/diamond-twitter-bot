from Bot import Bot


diamond_bot = Bot()

while True:
    if diamond_bot.show_options() in diamond_bot.actions:
        if diamond_bot.show_options() == "a":
            diamond_bot.see_public_tweets()
        

    else:
        print("\nBOT OFF")
        break
