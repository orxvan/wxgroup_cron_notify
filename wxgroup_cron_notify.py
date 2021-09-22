from chinese_calendar import is_workday
import datetime
import requests
import os
import typer

# use the service https://github.com/tans/push-bot

TOKEN = os.environ['TOKEN']

app = typer.Typer()


@app.command()
def send_wx_group_msg(msg: str, token=TOKEN):
    if (is_workday(datetime.date.today())):
        url = "https://push.bot.qw360.cn/room/"+token+"?msg="+msg
        r = requests.get(url)
    return r


if __name__ == '__main__':
    # send_wx_group_msg("hello world", TOKEN)
    app()
