import telegram
from configure_keys import load_keys


def tg_bot():
    bot = telegram.Bot(token=load_keys("TG_KEY"))
    print(bot.get_me())
    # bot.send_message(text='Hi!', chat_id="@tg_test_bots_ch")
    bot.send_photo(chat_id="@tg_test_bots_ch", photo=open('images/0.jpg', 'rb'))
    bot.get_updates()



def main():
    tg_bot()


if __name__ == "__main__":
    main()
