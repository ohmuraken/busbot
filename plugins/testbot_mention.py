from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('疲れた')
@respond_to('つかれた')
def cheer(message):
    message.reply('ファイト!')

@listen_to('あきらめたら')
@listen_to('諦めたら')
def anzai(message):
    message.send('そこで試合終了ですよ。')

print("CALL!")

@listen_to('いいですか')
def reaction(message):
    message.react('+1')