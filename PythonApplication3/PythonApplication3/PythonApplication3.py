import yfinance as yf
import datetime
from datetime import date
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error

def download_data(stock,start_Date,end_date):
    data=yf.download(stock,start=start_Date,end=end_date)
    
    return data
def my_model(model,num):
    df=data[['Close','Volume']]
    df['preds']=df.Close.shift(-1) # �rnek 12 nisan 2024 tarihindeki veriye 13 nisan 2024 a��l�� fiyat�n� yazar
    #print(df)
    X=df.drop(['preds','Volume'],axis=1).values
    X=scaler.fit_transform(X) 
    X=X[:-1]
    X_forecast=X[-num:]
    
    y=df.preds.values
    y=y[:-1]
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    model.fit(X_train,y_train)
    preds=model.predict(X_test)
    
    print(f'predict with the accuracy of: {r2_score(y_test,preds)}')
    forecasted_pred=model.predict(X_forecast)
    
    day=num
    today=datetime.date.today()
    for i in forecasted_pred:
        tahmingunu=today+datetime.timedelta(days=day-1)
        print(f'predicted closing price for day {tahmingunu} is {i}')
        day=day-1
        

stock="btc-usd" #yfinance'dan iste�imiz hissnin kodunu buraya yaz�yoruz
today=datetime.date.today()
duration=50 # 50 i�lem g�n�ndeki verileri �ekmeye yarar de�i�tirilebilir
before=today-datetime.timedelta(days=duration)
start_date=before
end_date=today

data=download_data(stock,start_date,end_date)
print(data)

num=1 # ka� g�nl�k tahmin edilece�ini belirler
scaler=StandardScaler()
classify=LinearRegression()
my_model(classify,num)


