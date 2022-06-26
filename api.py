"""
    Moduł, w którym znajdują się wszystkie funkcje, które
    obsługują komunikację z api twittera
"""
import configparser
import tweepy

config = configparser.ConfigParser()
config.read('cfg.ini')
consumer_key = config['api']['consumer_key']
consumer_secret = config['api']['consumer_secret']
access_token = config['api']['access_token']
access_token_secret = config['api']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
try:
    api.verify_credentials()
except tweepy.TweepError as err_api:
    print("Błąd podczas autoryzacji")
    print(err_api.api_code)
    print(err_api.reason)


def moja_nazwa():
    """
    Funkcja printująca moją nazwę użytkownika
    """
    try:
        user = api.me()
        print("Twoja nazwa użytkownika to:", user.name, "\n")
    except tweepy.TweepError as err:
        print("Coś poszło nie tak")
        print(err.api_code)
        print(err.reason)


def daj_followy():
    """
    Funkcja z pętlą, która przechodzi po moich followersach
    i daje im followy
    """
    try:
        user = api.me()
        for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
        print(f'Wszyscy, którzy followują {user.name} dostali zwrotnego followa', "\n")
    except tweepy.TweepError as err:
        print("Coś poszło nie tak")
        print(err.api_code)
        print(err.reason)


def tweety_os_czasu(liczba):
    """
        Wyświtla, która wyświetla zadeklarowaną liczbę
        ostatnich tweetów z mojej osi czasu
        :param liczba: liczba ostatnich tweetów do wyświetlenia
    """
    numer = 0
    try:
        timeline = api.home_timeline(tweet_mode="extended", count=liczba)
        for tweet in timeline:
            if timeline[numer].full_text.startswith("RT @"):
                print(f'Tweet nr {numer + 1}:')
                print(tweet.user.name, "podał:", timeline[numer].retweeted_status.full_text, "\n")

            else:
                print(f'Tweet nr {numer + 1}:')
                print(tweet.user.name, "napisał:", timeline[numer].full_text, "\n")
            numer += 1
    except tweepy.TweepError as err:
        print("Coś poszło nie tak")
        print(err.api_code)
        print(err.reason)


def tweety_kogos(nazwa, liczba):
    """
        Funkcja, która wyszukuje danego użytkownika i
        printuje jego zadeklarowaną liczbę ostatnich tweetów
        :param nazwa: nazwa użytkownika
        :param liczba: liczba ostatnich tweetów do wyświetlenia
    """
    numer = 0
    if nazwa != "":
        try:
            timeline = api.user_timeline(screen_name=nazwa, count=liczba, tweet_mode="extended")
            for tweet in timeline:
                if timeline[numer].full_text.startswith("RT @"):
                    print(f'Tweet nr {numer + 1}:')
                    print(tweet.user.name, "podał:", timeline[numer].retweeted_status.full_text,
                          "\n")
                else:
                    print(f'Tweet nr {numer + 1}:')
                    print(tweet.user.name, "napisał:", timeline[numer].full_text, "\n")
                numer += 1
        except tweepy.TweepError as err:
            print("Coś poszło nie tak")
            print(err.api_code)
            print(err.reason)
    else:
        print("Musisz podać nazwę użytkownika!")


def wyslij_tweeta(tekst):
    """
        Funkcja, która wysyła tweeta o zadeklarowanej treści
        :param tekst: treść tweeta
    """
    if tekst != "":
        try:
            api.update_status(tekst)
            print("Wysłano tweeta \n")
        except tweepy.TweepError as err:
            print("Coś poszło nie tak")
            print(err.api_code)
            print(err.reason)
    else:
        print("Musisz podać treść!")


def dane_uzytkownika(nazwa_uz):
    """
        Funkcja, która wyszukuje zadeklarowanego użytkownika i
        printuje jego nazwę, opis, zadeklarowaną lokalizację i
        20 ostatnich followów
        :param nazwa_uz: nazwa użytkownika
    """
    if nazwa_uz != "":
        try:
            user = api.get_user(nazwa_uz)
            print(f"Nazwa:{user.name}")
            print(f"Opis: {user.description}")
            print(f"Zadeklarowala lokalizacja: {user.location}")

            print("Ostatnich 20 followersów:")
            for follower in user.followers():
                print(follower.name)
        except tweepy.TweepError as err:
            print("Coś poszło nie tak")
            print(err.api_code)
            print(err.reason)
    else:
        print("Musisz podać nazwę użytkownika!")


def wysz_tweetow(liczba, fraza):
    """
        Funkcja, która wyszukuje tweety po danej frazie
        i printuje autora i treść tweeta
        :param liczba: liczba tweetów
        :param fraza: wyszukiwana fraza
    """
    numer = 0
    if fraza != "":
        try:
            api_search = api.search(fraza, count=liczba)
            for tweet in api_search:
                if tweet.text.startswith("RT @"):
                    print(f'Tweet nr {numer + 1}:')
                    print(tweet.user.name, "podał:", tweet.text, "\n")
                else:
                    print(f'Tweet nr {numer + 1}:')
                    print(tweet.user.name, "napisał:", tweet.text, "\n")
                numer += 1
        except tweepy.TweepError as err:
            print("Coś poszło nie tak")
            print(err.api_code)
            print(err.reason)
    else:
        print("Musisz podać frazę!")


def wysz_retweet(liczba, fraza):
    """
        Funkcja, która daje retweeta tweetom wyszukanym po danej frazie
        i printuje autora i treść tweeta
        :param liczba: liczba tweetów
        :param fraza: wyszukiwana fraza
    """
    numer = 0
    if fraza != "":
        try:
            api_search = api.search(fraza, count=liczba)
            for tweet in api_search:
                tweet.retweet()
                if tweet.text.startswith("RT @"):
                    print(f'Podano dalej: Tweet nr {numer + 1}:')
                    print(tweet.user.name, "podał:", tweet.text, "\n")
                else:
                    print(f'Podano dalej: Tweet nr {numer + 1}:')
                    print(tweet.user.name, "napisał:", tweet.text, "\n")
                numer += 1
        except tweepy.TweepError as err:
            print("Coś poszło nie tak")
            print(err.api_code)
            print(err.reason)
    else:
        print("Musisz podać frazę!")


def wysz_lajk(liczba, fraza):
    """
        Funkcj, która lajkuje wyszukane tweety po danej frazie
        i printuje autora i treść tweeta
        :param liczba: liczba tweetów
        :param fraza: wyszukiwana fraza
    """
    numer = 0
    if fraza != "":
        try:
            api_search = api.search(fraza, count=liczba)
            for tweet in api_search:
                tweet.favorite()
                if tweet.text.startswith("RT @"):
                    print(f'Polajkowano: Tweet nr {numer + 1}:')
                    print(tweet.user.name, "podał:", tweet.text, "\n")
                else:
                    print(f'Polajkowano: Tweet nr {numer + 1}:')
                    print(tweet.user.name, "napisał:", tweet.text, "\n")
                numer += 1
        except tweepy.TweepError as err:
            print("Coś poszło nie tak")
            print(err.api_code)
            print(err.reason)
    else:
        print("Musisz podać frazę!")


def wysz_follow(liczba, fraza):
    """
        Funkcja, która daje followa autora wyszukanego tweeta po danej frazie
        a także printuje autora i treść tweeta
        :param liczba: liczba tweetów
        :param fraza: wyszukiwana fraza
    """
    numer = 0
    if fraza != "":
        try:
            api_search = api.search(fraza, count=liczba)
            for tweet in api_search:
                tweet.user.follow()
                if tweet.text.startswith("RT @"):
                    print(f'{tweet.user.name} dostał followa za Tweet nr {numer + 1}:')
                    print(tweet.user.name, "podał:", tweet.text, "\n")
                else:
                    print(f'{tweet.user.name} dostał followa za Tweet nr{numer + 1}:')
                    print(tweet.user.name, "napisał:", tweet.text, "\n")
                numer += 1
        except tweepy.TweepError as err:
            print("Coś poszło nie tak")
            print(err.api_code)
            print(err.reason)
    else:
        print("Musisz podać frazę!")
