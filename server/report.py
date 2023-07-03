import pandas as pd

def read_data():
    # Example dataframe
    dataset = pd.read_csv("data.csv")
    df = pd.DataFrame(dataset)
    df[['Day','Month','Year']] = df.Dates.str.split("-", expand = True)
    df['Year'] = df['Year'].str.replace(' 00:00', '')
    df.drop(['Dates'], axis=1)
    return df

def get_month_usage_details(state,month,year) : 
    df = read_data()
    filtered_data = df[(df['States'] == state) & (df['Month'] == month) & (df['Year'] == year)]
    highest_usage = filtered_data['Usage'].max()
    lowest_usage = filtered_data['Usage'].min()
    sum_usage = filtered_data['Usage'].sum()
    usage_details = {'max':highest_usage,'min':lowest_usage,'total':sum_usage}
    return usage_details



def get_monthwise_report(desired_state,desired_year):
    df = read_data()
    # Specify the desired state and year
    # desired_state = 'Karnataka'
    # desired_year = '2019'

    # Filter the dataframe based on state and year
    filtered_df = df[(df['States'] == desired_state) & (df['Year'] == desired_year)]

    # Group by month and calculate the sum of usage
    grouped_df = filtered_df.groupby('Month')['Usage'].sum().reset_index()

    json_data = grouped_df.to_json(orient='records')
    return json_data

if __name__ == '__main__':
    # print(get_monthwise_report('Karnataka','2020'))
    print(get_month_usage_details('Kerala','04','2020'))


