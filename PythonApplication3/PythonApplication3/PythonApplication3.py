import yfinance as yf
import datetime
import pyodbc
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import uuid  

# G�khan Erol 210401112 
def download_data(stock,start_Date,end_date):
    data=yf.download(stock,start=start_Date,end=end_date)
    
    return data
def my_model(model,num):
    df=data[['Close','Volume']]
    df['preds']=df.Close.shift(-1) 
    X=df.drop(['preds'],axis=1).values
    X=scaler.fit_transform(X) 
    X=X[:-1]
    X_forecast=X[-num:]
    
    y=df.preds.values
    y=y[:-1]
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    model.fit(X_train,y_train)
    preds=model.predict(X_test)
    
    print(f'predict with the accuracy of: {r2_score(y_test,preds)}')
    #R�=SS(res)/SS(tot) ile hesaplanmaktad�r
    #( SS(res) art�k kareler toplam� (Residual Sum of Squares),
    # modelin tahmin etti�i de�erlerle ger�ek de�erler aras�ndaki 
    # farklar�n karelerinin toplam�d�r. SS(tot) toplam kareler toplam� 
    # (Total Sum of Squares), ger�ek de�erlerin ortalamadan 
    # sapmalar�n�n karelerinin toplam�d�r.) 
    #print(f'predict with the accuracy of 2 : {mean_squared_error(y_test,preds)}')
    forecasted_pred=model.predict(X_forecast)
    
    InsertPreds(forecasted_pred,num)

def WhichStocks(Stock):
    conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=(localdb)\\MSSQLLocalDB;"
        "DATABASE=Stock;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT ID from Stockss where Stockcode='{Stock}'")
    row = cursor.fetchone()
    
    conn.commit()
    # Ba�lant�y� kapatma
    cursor.close()
    conn.close()    
    return row[0]

def InsertValues(data):
    DeleteValues()
    conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=(localdb)\\MSSQLLocalDB;"
        "DATABASE=Stock;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    data.reset_index(inplace=True)
    
    for index, row in data.iterrows():
        id=uuid.uuid4()
        dates = row['Date'].strftime('%Y-%m-%d')
        closing_price = row['Close']
        volume = row['Volume']
        cursor.execute("insert into StocksPricess"
        f"(ID,Dates,ClosingPrice,Volumes,StocksID) values ('{id}','{dates}','{closing_price}','{volume}','{WhichStocks(stock)}')")
    
    
    
    conn.commit()
    # Ba�lant�y� kapatma
    cursor.close()
    conn.close()
def DeleteValues():
    conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=(localdb)\\MSSQLLocalDB;"
        "DATABASE=Stock;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(f"delete from StocksPricess where StocksID='{WhichStocks(stock)}'")
    
    conn.commit()
    # Ba�lant�y� kapatma
    cursor.close()
    conn.close()
    

def InsertPreds(preds,num):
    DeletePreds()
    conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=(localdb)\\MSSQLLocalDB;"
        "DATABASE=Stock;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    today = datetime.date.today() + datetime.timedelta(days=num-1)
    
    for i in preds:
       id = str(uuid.uuid4())
       cursor.execute("insert into Predictionss"
        f"(ID,Dates,PredictionPrices,StocksID) values ('{id}','{today}','{i}','{WhichStocks(stock)}')")
       today -= datetime.timedelta(days=1)
       
    
    conn.commit()
    # Ba�lant�y� kapatma
    cursor.close()
    conn.close() 
def DeletePreds():
    conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=(localdb)\\MSSQLLocalDB;"
        "DATABASE=Stock;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(f"delete from Predictionss where StocksID='{WhichStocks(stock)}'")

    conn.commit()
    # Ba�lant�y� kapatma
    cursor.close()
    conn.close() 
    
stock="dot-usd" #yfinance'dan iste�imiz hissenin kodunu buraya yaz�yoruz
today=datetime.date.today()
duration=100 # 100 i�lem g�n�ndeki verileri �ekmeye yarar de�i�tirilebilir
before=today-datetime.timedelta(days=duration)
start_date=before
end_date=today

data=download_data(stock,start_date,end_date)
num=30 # ka� g�nl�k tahmin edilece�ini belirler
scaler=StandardScaler()
classify=LinearRegression()
my_model(classify,num)
#WhichStocks(stock)
InsertValues(data)


