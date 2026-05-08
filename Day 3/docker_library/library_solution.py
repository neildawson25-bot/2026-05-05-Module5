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

def count_removed_rows(before_count, after_count):
    return before_count - after_count


def count_overdue_books(df):
    return df["Overdue"].sum()


def count_date_errors(df):
    return df["Date Error"].sum()


def export_pipeline_metrics(metrics, file_path):
    metrics.to_csv(file_path, index=False)


# Main File
# Main File

customers = fileLoader("03_Library SystemCustomers.csv")
books = fileLoader("03_Library Systembook.csv")

original_customer_records = len(customers)
original_book_records = len(books)


# Remove duplicate rows

customers_before_duplicates = len(customers)
books_before_duplicates = len(books)

customers = duplicateCheck(customers)
books = duplicateCheck(books)

customer_duplicates_removed = count_removed_rows(customers_before_duplicates, len(customers))
book_duplicates_removed = count_removed_rows(books_before_duplicates, len(books))


# Remove missing data

customers_before_missing = len(customers)
books_before_missing = len(books)

customers = remove_missing_data(customers)
books = remove_missing_data(books)

customer_missing_removed = count_removed_rows(customers_before_missing, len(customers))
book_missing_removed = count_removed_rows(books_before_missing, len(books))


# Remove books linked to invalid customers

books_before_invalid_customers = len(books)

books = remove_invalid_customers(books, customers)

invalid_customer_rows_removed = count_removed_rows(books_before_invalid_customers, len(books))


# Clean and enrich book data

books = clean_dates(books)
books = calculate_days_borrowed(books)
books = flag_overdue_books(books)
books = flag_date_errors(books)


# Final metrics

customer_records = len(customers)
book_records = len(books)
overdue_books = count_overdue_books(books)
date_errors = count_date_errors(books)


# Export cleaned files

customers.to_csv("/outputfiles/clean_customers.csv", index=False)
books.to_csv("/outputfiles/clean_books.csv", index=False)


# Export pipeline metrics

metrics = pd.DataFrame({
    "Metric": [
        "Original Customer Records",
        "Original Book Records",
        "Final Customer Records",
        "Final Book Records",
        "Customer Duplicate Rows Removed",
        "Book Duplicate Rows Removed",
        "Customer Missing Rows Removed",
        "Book Missing Rows Removed",
        "Invalid Customer Rows Removed",
        "Overdue Books",
        "Date Errors"
    ],
    "Value": [
        original_customer_records,
        original_book_records,
        customer_records,
        book_records,
        customer_duplicates_removed,
        book_duplicates_removed,
        customer_missing_removed,
        book_missing_removed,
        invalid_customer_rows_removed,
        overdue_books,
        date_errors
    ]
})

export_pipeline_metrics(metrics, "/outputfiles/pipeline_metrics.csv")


# Print summary

print("Customer records:", customer_records)
print("Book records:", book_records)
print("Overdue books:", overdue_books)
print("Date errors:", date_errors)
print("Pipeline metrics exported")
print("Cleaning complete")