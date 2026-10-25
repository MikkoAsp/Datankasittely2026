from datetime import datetime
import pandas as pd
def anonymize(people):
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """
    df = pd.DataFrame(people)
    df = df.drop("name", axis=1)
    
    df["birthdate"] = df["birthdate"].str.split("-").str[0]
    df["city"] = df["city"].str[0]
    
    df = df.rename(columns={'birthdate': 'birth_year', 'city': 'city_initial'})
    df['birth_year'] = df['birth_year'].astype(int)
    df = df[['birth_year', 'city_initial']]

    return df.to_dict(orient='records') 