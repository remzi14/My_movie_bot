import psycopg2
from psycopg2.extras import DictCursor


conn=psycopg2.connect(
    user='postgres',
    dbname='kinokod',
    password='ramiz',
    port=5432,
    cursor_factory=DictCursor
)


cur=conn.cursor()


def startup_table():
    query= '''
        CREATE TABLE IF NOT EXISTS users(
            id  BIGSERIAL PRIMARY KEY,
            telegram_id VARCHAR(60) UNIQUE,
            create_at TIMESTAMP  DEFAULT now()
        )
    
    '''

    channel_query="""
    CREATE TABLE IF NOT EXISTS channel(
        id BIGSERIAL PRIMARY KEY,
        username VARCHAR(200) NOT NULL,
        chanel_id VARCHAR(200) UNIQUE,
        create_at TIMESTAMP DEFAULT now()
    
    )
    
    """


    media_query="""
    CREATE TABLE IF NOT EXISTS movies(
        id BIGSERIAL PRIMARY KEY,
        post_id INT NOT NULL,
        file_at VARCHAR(200) NOT NULL,
        caption TEXT,
        created_at TIMESTAMP DEFAULT now()
        
     
     )
     """



    cur.execute(query)
    cur.execute(channel_query)
    cur.execute(media_query)
    conn.commit()

