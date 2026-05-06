import pandas as pd

#Functions


def fileLoader(file_path):
    return pd.read_csv(file_path)

def duplicateCheck(df):
    return df.drop_duplicates()

def remove_missing_data(df):
    return df.dropna()

def remove_invalid_customers(books, customers):
    return books[books["Customer ID"].isin(customers["Customer ID"])]



def clean_dates(df):
    df["Book checkout"] = df["Book checkout"].astype(str).str.replace('"', '')
    df["Book Returned"] = df["Book Returned"].astype(str).str.replace('"', '')

    df["Book checkout"] = pd.to_datetime(books["Book checkout"],dayfirst=True, errors="coerce")

    df["Book Returned"] = pd.to_datetime(books["Book Returned"],dayfirst=True,errors="coerce")
    return df


def calculate_days_borrowed(df):
    df["Days Borrowed"] = (df["Book Returned"] - df["Book checkout"]).dt.days
    return df


def flag_overdue_books(df):
    df["Overdue"] = df["Days Borrowed"] > 14
    return df


def flag_date_errors(df):
    df["Date Error"] = df["Days Borrowed"] < 0
    return df


# Main File

customers = fileLoader("c:/Users/Admin/.ssh/2026-05-05-Module5/03_Library SystemCustomers.csv")
books = fileLoader("c:/Users/Admin/.ssh/2026-05-05-Module5/03_Library Systembook.csv")

customers = duplicateCheck(customers)
books = duplicateCheck(books)

customers = remove_missing_data(customers)
books = remove_missing_data(books)

books = remove_invalid_customers(books, customers)

books = clean_dates(books)

books = calculate_days_borrowed(books)
books = flag_overdue_books(books)
books = flag_date_errors(books)


customers.to_csv("clean_customers.csv", index=False)
books.to_csv("clean_books.csv", index=False)


print("Customer records:", len(customers))
print("Book records:", len(books))
print("Overdue books:", books["Overdue"].sum())
print("Date errors:", books["Date Error"].sum())

print("Cleaning complete")