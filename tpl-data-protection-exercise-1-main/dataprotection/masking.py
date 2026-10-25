import pandas as pd

def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    df = pd.DataFrame(people)
    
    df["email"] = df["email"].str.split("@").str[1].str.split(".").str[0]
    df['phone'] = df['phone'].str.slice_replace(stop=-2, repl='*' * 8)

    return people