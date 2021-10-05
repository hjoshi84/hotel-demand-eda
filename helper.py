import numpy as np

def overall_stats(user_options,df):
    if(user_options != 'Overall') :
        df = df[df['arrival_date_year'] == int(user_options)]
        booked = np.ceil((df['is_canceled'].value_counts(normalize=True) * 100)[0])
        hotel_type_city = np.ceil(df[df['is_canceled'] == 0]['hotel'].value_counts(normalize=True) * 100)[0]
        hotel_type_resort =np.ceil(df[df['is_canceled'] == 0]['hotel'].value_counts(normalize=True) * 100)[1]
        max_booked = \
        df.groupby(['country_name'])['booked'].sum().sort_values().reset_index()[-1:]['country_name'].to_list()[0]

    else:
        booked = np.ceil((df['is_canceled'].value_counts(normalize=True) * 100)[0])
        hotel_type_city = np.ceil(df[df['is_canceled'] == 0]['hotel'].value_counts(normalize=True) * 100)[0]
        hotel_type_resort = np.ceil(df[df['is_canceled'] == 0]['hotel'].value_counts(normalize=True) * 100)[1]
        max_booked = \
        df.groupby(['country_name'])['booked'].sum().sort_values().reset_index()[-1:]['country_name'].to_list()[0]

    return booked,hotel_type_city,hotel_type_resort,max_booked

def custom_df(user_options,df):
        if (user_options != 'Overall'):
            df = df[df['arrival_date_year'] == int(user_options)]

        else:
            df = df

        return df
