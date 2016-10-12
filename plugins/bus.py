from slackbot.bot import respond_to
from slackbot.bot import listen_to
from datetime import datetime
import sqlite3


@respond_to('bus')
def cheer(message):
    message.reply('あっ, バス使う？')


@respond_to('(.*),(.*)')
def send_timetable(message, param1, param2):
    con = sqlite3.connect("db/timetable.db")
    con.row_factory = sqlite3.Row
    if param1 == "n3" or param1 == "N3":
        bus_name = "北3系統 北大路バスターミナル行き"
        line = "3"
    elif param1 == "40":
        bus_name = "40系統 国際会館行き"
        line = "40"

    about_bus = ":busstop:京都産業大発の{}バス:busstop:".format(bus_name)
    about_time = ":bus: {}時以降の出発時間です:bus:".format(param2)
    hour = param2

    sql = "select * from Timetable where lines == {} and hour == {}".format(line, hour)
    text = about_bus + about_time
    text += "\n" + "=== Time Table ==="
    for row in con.execute(sql):
        text += "\n" + "{}:{}".format(row["hour"], row["minute"])
    text += "\n" + "==============="
    message.send(text)
    con.close()


@respond_to('(.*)')
def send_timetable(message, param1):
    con = sqlite3.connect("db/timetable.db")
    con.row_factory = sqlite3.Row
    hour = datetime.now().hour
    minute = datetime.now().minute

    if param1 == "n3" or param1 == "N3":
        bus_name = "北3系統 北大路バスターミナル行き"
        line = "3"
    elif param1 == "40":
        bus_name = "40系統 国際会館行き"
        line = "40"

    about_bus = ":busstop:京都産業大発の{}バス:busstop:".format(bus_name)
    about_time = "\n:bus:{}時{}分以降の出発時間です:bus:".format(hour,minute)
    sql = "select * from Timetable where lines == {} and hour >= {} and minute >= {} limit 1".format(line, hour, minute)
    for row in con.execute(sql):
        result_id = row["id"]

    sql = "select * from Timetable where id >= {} limit 5".format(result_id)
    text = about_bus + about_time
    text += "\n" + "=== Time Table ==="
    for row in con.execute(sql):
        text += "\n" + "{}:{}".format(row["hour"],row["minute"])
    text += "\n" + "==============="
    message.send(text)
    con.close()
