import nltk
import pymysql
from textblob import TextBlob

db = pymysql.connect("localhost","root","MaruthiRaja","smart_shopping")
cursor = db.cursor()

sql = """SELECT * FROM `customer_review`"""

try:
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        print(row[0])
        print(row[1])
        print(row[2])
        if row[3] == -1:
            sen = TextBlob(row[2])
            print(sen.tags)
            for sen in sen.sentences:
                polarity_value = sen.sentiment.polarity
                print(polarity_value)
                if(polarity_value > 0 and polarity_value < 0.5 ):
                    up = "update customer_review set product_ranking = 3 where product_id = %s" % row[1]
                    cursor.execute(up)
                    db.commit()
                    print("3 star")
                elif(polarity_value > 0.5 and polarity_value < 0.8):
                    up = "update customer_review set product_ranking = 4 where product_id = %s" % row[1]
                    cursor.execute(up)
                    db.commit()
                    print("4 star")
                elif(polarity_value > 0.8 and polarity_value < 1):
                    up = "update customer_review set product_ranking = 5 where product_id = %s" % row[1]
                    cursor.execute(up)
                    db.commit()
                    print("5 star")
                elif(polarity_value < 0 and polarity_value > -0.9):
                    up = "update customer_review set product_ranking = 2 where product_id = %s" % row[1]
                    cursor.execute(up)
                    db.commit()
                    print("2 star")
                elif(polarity_value < -0.9 ):
                    up = "update customer_review set product_ranking = 1 where product_id = %s" % row[1]
                    cursor.execute(up)
                    db.commit()
                    print("1 star")

    db.commit()
except pymysql.InternalError as error:
    print(error)
db.close()