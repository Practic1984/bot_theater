import telebot
import sql_fnc
import sql_query
from config import TOKEN, ADMIN_ID

import logging
from datetime import datetime, timedelta
import pandas as pd
import msg
import keyboards
    
bot = telebot.TeleBot(token=TOKEN, parse_mode='HTML', skip_pending=True)    
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("/start", "Start"),
    ],)

def save_user(message):
    userId = int(message.from_user.id)
    username = message.from_user.username
    first_name = message.from_user.first_name
    reg_time = datetime.fromtimestamp(message.date)
    str_query_time = reg_time.strftime('%Y-%m-%d %H:%M:%S')
    con = sql_fnc.create_connection('users.db')
    sql_fnc.execute_query(con, sql_query.create_users_table, params=[])
    sql_fnc.execute_query(con, sql_query.save_user, params=[userId, username, first_name, str_query_time, 'false','false','false'])
    con.close()

def main():

    @bot.message_handler(commands=['start'])
    def start_fnc(message):
        bot.send_message(chat_id=message.from_user.id, text=msg.welcome_msg, reply_markup=keyboards.main_menu_user())
        save_user(message=message)

    @bot.message_handler(content_types=['text'])
    def text_fnc(message):
        if message.text == '/admin':
            if message.from_user.id == ADMIN_ID: 
                con = sql_fnc.create_connection('users.db')
                df = pd.read_sql("SELECT * FROM users", con)
                df.to_excel("result_users.xlsx", index=False)
                with open("result_users.xlsx", mode='rb') as file:
                    bot.send_document(chat_id=message.from_user.id, document=file, caption=msg.report_admin_text, reply_markup=keyboards.main_menu_user())
                con.close()
       
               
    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == 'schedule':
            reg_time =  datetime.now()
            reg_time = reg_time + timedelta(hours=3)
            timedelta(hours=3)
            str_query_time = reg_time.strftime('%Y-%m-%d %H:%M:%S')
            con = sql_fnc.create_connection('users.db')
            sql_fnc.execute_query_select(con, sql_query.upd_par_user.format(upd_par='check_schedule'), params=[str_query_time, call.from_user.id])
            with open(file='schedule.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.main_menu_user())
            con.close()    

        elif call.data == 'price':
            reg_time =  datetime.now()
            reg_time = reg_time + timedelta(hours=3)            
            str_query_time = reg_time.strftime('%Y-%m-%d %H:%M:%S')
            con = sql_fnc.create_connection('users.db')
            sql_fnc.execute_query_select(con, sql_query.upd_par_user.format(upd_par='check_price'), params=[str_query_time, call.from_user.id])
            with open(file='price.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.main_menu_user())
            con.close()

        elif call.data == 'record':
            reg_time =  datetime.now()
            reg_time = reg_time + timedelta(hours=3)
            str_query_time = reg_time.strftime('%Y-%m-%d %H:%M:%S')
            con = sql_fnc.create_connection('users.db')
            sql_fnc.execute_query_select(con, sql_query.upd_par_user.format(upd_par='check_record'), params=[str_query_time, call.from_user.id])
            bot.send_message(chat_id=call.from_user.id, text=msg.record_text, reply_markup=keyboards.main_menu_user())
            con.close()
        
        
        elif call.data == 'adress':
            with open(file='adress.png', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, caption=msg.adress_text, reply_markup=keyboards.main_menu_user())

        elif call.data == 'workout':
            bot.send_message(chat_id=call.from_user.id, text=msg.workout_text, reply_markup=keyboards.menu_workout())
  
        elif call.data == '1':
            with open(file='1.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.menu_workout())
        elif call.data == '2':
            with open(file='2.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.menu_workout())
        elif call.data == '3':
            with open(file='3.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.menu_workout())
        elif call.data == '4':
            with open(file='4.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.menu_workout())
        elif call.data == '5':
            with open(file='5.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.menu_workout())
        elif call.data == '6':
            with open(file='6.jpg', mode='rb') as f:
                bot.send_photo(chat_id=call.from_user.id, photo=f, reply_markup=keyboards.menu_workout())
        elif call.data == 'back':
            bot.send_message(chat_id=call.from_user.id, text="Вы находитесь в главном меню...", reply_markup=keyboards.main_menu_user())



    bot.infinity_polling(skip_pending=True)
if __name__ == "__main__":
    main()