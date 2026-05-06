import unittest
import pandas as pd

from library_solution import remove_missing_data, calculate_days_borrowed, flag_overdue_books


class TestLibrarySolution(unittest.TestCase):

    def test_naCheck_removes_missing_rows(self):
        df = pd.DataFrame({
            "Customer ID": [1, 2, None],
            "Customer Name": ["Jane", "John", None]
        })

        cleaned_df = remove_missing_data(df)

        self.assertEqual(len(cleaned_df), 2, "NaN rows were not removed")


    def test_dataEnrich_calculates_days_borrowed(self):
        df = pd.DataFrame({
            "Book checkout": pd.to_datetime(["01/01/2023"], dayfirst=True),
            "Book Returned": pd.to_datetime(["10/01/2023"], dayfirst=True)
        })

        enriched_df = calculate_days_borrowed (df)

        self.assertEqual(enriched_df["Days Borrowed"][0], 9, "Days Borrowed was not calculated correctly")


    def test_dataEnrich_flags_overdue(self):
        df = pd.DataFrame({
            "Book checkout": pd.to_datetime(["01/01/2023"], dayfirst=True),
            "Book Returned": pd.to_datetime(["20/01/2023"], dayfirst=True)
        })

        enriched_df = flag_overdue_books(df)

        self.assertEqual(enriched_df["Overdue"][0], True, "Overdue flag was not created correctly")


if __name__ == "__main__":
    unittest.main()