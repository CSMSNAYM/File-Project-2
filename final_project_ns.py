while True:
    print(f"\nChoose any of the options below:"
        "\nA:-Database"
        "\nB:-Question Regarding the Database"
        "\nC:-Quit/Exit")
    user_input= input("\n:").capitalize()
    if user_input=='C':
        print(f"\nUser exit.Thank You!")
        break
    elif user_input=='A':
        import pandas as pd
        data = pd.read_csv("data.csv")
        print(data)

        break
    elif user_input=='B':
        print(f"\nChoose any of the question below:"
              
              "\nQ(A) What is the change in inflation rate throughout years?"
              "\nQ(B) What is the monthly inflation rate change of Vegetable?"
              "\nQ(C) What is the monthly inflation rate change of fruits?"
              "\nQ(D) Which Vegetable was the most and least effected over the years?"
              "\nQ(E) Which Fruit was most and least effected over the year?"
              "\nQ(F) At what year was the most significant change in inflation?")
       
        user_question= input("\nQ:").capitalize()

        import pandas as pd 
        import matplotlib.pyplot as plt

        while True:
            if user_question=='A':
                print(f"\nInflation:"
                  "\n Inflation is an increase in the general price level of goods and services in an economy. When the general price level rises, each unit of currency buys fewer goods and services;consequently, inflation corresponds to a reduction in the purchasing power of money.")
                data = pd.read_csv("data.csv")
                #Converting date data dtype
                data['date']=pd.to_datetime(data['date'])
                #set date as index
                df=data.set_index('date')
                df=df.sort_index()
               
           
                #grouping data and dividing yearly
                aggregation_functions={'price':'mean'}
                df_yearly_average_price=df.groupby(['category','item','variety','unit']).resample("Y",origin='2017-11-03').aggregate(aggregation_functions).reset_index().rename(columns={'price': 'yearly_average_price'})
                df_yearly_average_price['yearly_price_pct_change']=df_yearly_average_price['yearly_average_price'].pct_change(axis=0)*100
                print(df_yearly_average_price)

                #Diagram
                df_yearly_average_price['yearly_price_pct_change'] = df_yearly_average_price['yearly_price_pct_change'].fillna(0)
                df_yearly_average_price['yearly_average_price']=df_yearly_average_price['yearly_average_price'].fillna(0)
                df_yearly_categoric_average_price=df_yearly_average_price.groupby(['date','category','unit'])['yearly_price_pct_change'].mean().reset_index()
                df_yearly_categoric_average_price['yearly_price_pct_change']=df_yearly_categoric_average_price['yearly_price_pct_change'].round(1)
                df_yearly_categoric_average_price['yearly_price_pct_change']=df_yearly_categoric_average_price['yearly_price_pct_change'].astype(str) + '%'
                fig = plt.sunburst(df_yearly_categoric_average_price, path=['date','category','unit','yearly_price_pct_change'],width=750, height=750)
                fig.show()
                break
               
            elif user_question=='B':
                def calculate_inflation_in_vegetable():
                    data= pd.read_csv("data.csv")
                    df_vegetable= data[(data['category']=='vegetable')]
                    weekly_prices=df_vegetable.groupby(['date','item']).mean('price')
                    weekly_prices=weekly_prices.sort_index()
                    inflation = weekly_prices.pct_change()
                    print(inflation*100)
                    print(type(inflation.index))
                   
                    plt.plot(inflation.index,100*inflation.price)
                    plt.xlabel('data')
                    plt.ylabel('inflation(percentage)')
                calculate_inflation_in_vegetable()

            elif user_question=='C':
                def calculate_inflation_in_fruit():
                    data= pd.read_csv("data.csv")
                    df_fruit= data[(data['category']=='fruit')]
                    weekly_prices=df_fruit.groupby(['date','item']).mean('price')
                    weekly_prices=weekly_prices.sort_index()
                    inflation = weekly_prices.pct_change()
                    print(inflation*100)
                    print(type(inflation.index))

                #Diagram
                    plt.plot(inflation.index,100*inflation.price)
                    plt.xlabel('data')
                    plt.ylabel('inflation(percentage)')
                calculate_inflation_in_fruit

            elif user_question=='d':
                def calculate_inflation_in_vegetable():
                    df= pd.read_csv('data.csv')
                    df_vegetable= df[(df['category']=='vegetable')]
                    weekly_prices=df_vegetable.groupby(['date','item']).mean('price')
                    weekly_prices=weekly_prices.pct_change()
                    weekly_prices=[]
               
                for row in calculate_inflation_in_vegetable:
                    data=float(row[2])
                    weekly_prices.append(data)
                    weekly_prices_min=min(weekly_prices)
                    weekly_prices_max=max(weekly_prices)
                print(f"The Vegetable that was least effected by inflation:{weekly_prices_min}")
                print(f"The Vegetable that was most effected by inflation:{weekly_prices_max}")

            elif user_question=='e':
                def calculate_inflation_in_fruit():
                    df= pd.read_csv('data.csv')
                    df_fruit= df[(df['category']=='fruit')]
                    weekly_prices=df_fruit.groupby(['date','item']).mean('price')
                    weekly_prices=weekly_prices.pct_change()
                    weekly_prices=[]
               
                for row in calculate_inflation_in_fruit:
                    data=float(row[2])
                    weekly_prices.append(data)
                    weekly_prices_min=min(weekly_prices)
                    weekly_prices_max=max(weekly_prices)
                print(f"The Fruit that was least effected by inflation:{weekly_prices_min}")
                print(f"The Fruit that was most effected by inflation:{weekly_prices_max}")
       
   
    else:
        print(f"Try Again(Error)")


    break