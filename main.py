import argparse

import pandas as pd
from thefuzz import fuzz, process

df = pd.read_csv("books.csv")


def fuzzysearch(q: str, limit: int = 10):
    """Fuzzy seach book title"""

    choices = df["title"].unique().tolist()
    matches = process.extract(q, choices, scorer=fuzz.partial_token_set_ratio, limit=limit)
    return matches


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seach book by titles")
    required_arguments = parser.add_argument_group("required arguments")
    required_arguments.add_argument(
        "-q", "--query", required=True, help="searching query"
    )
    args = parser.parse_args()
    matches = fuzzysearch(args.query)
    print(f'{"Score":<10} Result')
    for book_title, score in matches:
        print(f"{score:<10} {book_title}")
