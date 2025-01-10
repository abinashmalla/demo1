import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    insert into student (st_id,st_name,st_class,st_email)
    Values ('1',"Abi","BCA","abinashm498@gmail.com"),
           ('2',"Bishal","Civil",'abinashmalla47@gmail.com'),
           ("3","Sandesh","Doctor","sandeshm486@gmail.com");

'''
conn.execute(ins)
conn.commit()
conn.close()