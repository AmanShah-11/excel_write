import pandas as pd


def test(src, dest):

    # Put the src file in the param here
    file = pd.read_excel('excel_stuff/Chart of Accounts Takeon v3 (1).xlsx')

    # Put the dest file in the param here instead of hard encoding
    file.to_csv('excel_stuff/Chart of Accounts Takeon v3 (1).txt', sep="\t", index=False)

    # Do exception handling and whatnot and return success/fail


if __name__ == "__main__":
    test("dummy var", "dummy var2")
