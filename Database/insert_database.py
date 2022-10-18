import mysql.connector


mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="MidNightSun2022",
      database = "db")


cursor = mydb.cursor()

cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("tlr6hc", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("thi7hc", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("sadh3n", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("ajd7ds", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("chn6as", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("hsays9", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("akd8w2", "write"))


# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0001', 'the_lords_of_the_rings', 'BMW');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0002', 'house_of_dragons', 'Aston');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0003', 'avengers_infinity_war', 'General');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0004', 'beauty_and_the_beast', 'Ford');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0005', 'she_hulk', 'Mercedes');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0006', 'spider_man_far_from_home', 'Volvo');")


cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('lashdlewnsadsad', 533, 'dabong', 'low', 'tlr6hc', 'A0001');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('sauefn dvysdfnw', 551, 'bongchay', 'low', 'sadh3n', 'A0001');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('sdfnkqwfosadosd', 533, 'dabong', 'high', 'tlr6hc', 'A0002');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('cyew fovasbdsus', 674, 'dabong', 'low', 'tlr6hc', 'A0003');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asuiefr cfpsdna', 975, 'dabong', 'high', 'chn6as', 'A0001');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asd7efbwdtyqdbq', 533, 'dabong', 'low', 'tlr6hc', 'A0004');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asdojweofbdhsvj', 216, 'bongro', 'low', 'hsays9', 'A0001');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('ascoadsalskfnw7', 533, 'dabong', 'high', 'tlr6hc', 'A0005');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('wq0943ihfsfknaf', 587, 'bongbauduc', 'low', 'tlr6hc', 'A0001');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asdiq39sdfq,ljd', 533, 'dabong', 'high', 'akd8w2', 'A0006');")
cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asdhbjewgfbjw7d', 034, 'dabong', 'low', 'tlr6hc', 'A0001');")

mydb.commit()