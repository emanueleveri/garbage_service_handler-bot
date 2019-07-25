import sys
import time
import telepot
from telepot.loop import MessageLoop
import psycopg2
def handle(msg):
    username = msg['from']['username']
    conn = psycopg2.connect('String used to connect to postgresql dbms')
    cur = conn.cursor()
    content_type, chat_type, chat_id = telepot.glance(msg)
    giorno = msg['text']
    if msg['text']=='/start':
        bot.sendMessage(chat_id,"Benvenuto @"+str(username) + " per usare questo bot scrivi una data nel formato gg/mm/AAAA")
        bot.sendMessage(chat_id,"per esempio 1/08/19")
    else:
        if len(giorno.split('/')) == 3:
            query = "select garbagetype from garbage where data = '"+str(giorno)+"'"
            cur.execute(query)
            typegarb = cur.fetchone()
            typegarb = typegarb[0]
            if typegarb == None:
                bot.sendMessage(chat_id,'Per questo giorno non sono previsti servizi di ritiro dei rifiuti')
            else:
                bot.sendMessage(chat_id," Il giorno " +str(giorno)+ " passa <strong>" +str(typegarb[0])+"</strong>",parse_mode='HTML')
bot = telepot.Bot('Bot token')
MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)
