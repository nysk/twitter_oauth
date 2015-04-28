twitter_oauth
====

このコードは python と [django](https://github.com/django/django), [tweepy](https://github.com/tweepy/tweepy) を使った twitter 認証のサンプルコードです. 2011 年 5 月 29 日に初 commit し, 有難いことにたま〜に fork したり star 付けてくれる方がおられるようなので, 気が向いたときにたま〜にメンテしたりしています. また, 練習がてらに README 書いてみたり, Licence 付けてみたり, いろいろ試しています.

## Screenshot
![](https://github.com/ketulive/twitter_oauth/blob/images/twitter_oauth/images/screenshot01.png)

![](https://github.com/ketulive/twitter_oauth/blob/images/twitter_oauth/images/screenshot02.png)

![](https://github.com/ketulive/twitter_oauth/blob/images/twitter_oauth/images/screenshot03.png)

## Requirement
    Django==1.3
    flake8==2.2.4
    mccabe==0.3
    oauthlib==0.7.2
    pep8==1.5.7
    pyflakes==0.8.1
    requests==2.6.2
    requests-oauthlib==0.4.2
    six==1.9.0
    tweepy==3.3.0

## Usage
virtualenv などで, 任意の環境名で環境を作ってください. 良くわからない場合はググってください.

    $ git clone git@github.com:ketulive/twitter_oauth.git
    $ cd twitter_oauth/twitter_oauth
    $ pip install -r ../requirements.txt

[twitter application management](https://apps.twitter.com/) で アプリを作って CONSUMER_KEY と CONSUMER_SECRET を発行し,

    $ vim oauth/views.py

などとしてあなたのものに差し替えてください.

そして最後に

    $ python manage.py runserver --settings=settings

これで動くと思います.

## Licence

[MIT](https://github.com/ketulive/twitter_oauth/blob/master/LICENSE)

## Author

[ketulive](https://github.com/ketulive)
