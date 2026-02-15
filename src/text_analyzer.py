# ============================================================
# Program      : Text Analyzer (Advanced)
# Description  : Cleans text, removes stopwords, ranks words,
#                generates a word cloud visualization, and
#                saves the top-frequency list to a file.
# Author       : M. Salimudin
# Date         : 14 February 2026
# Language     : Python 3
# ============================================================

from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple

from wordcloud import WordCloud
import matplotlib.pyplot as plt


DEFAULT_STOPWORDS = {
    # Indonesian (basic)
    "dan", "yang", "di", "ke", "dari", "untuk", "pada", "dengan", "atau", "ini", "itu", "adalah",
    # English (basic)
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "with", "is", "are", "was", "were",
}


@dataclass(frozen=True)
class AnalysisResult:
    char_count: int
    word_count: int
    top_n: int
    most_common: List[Tuple[str, int]]
    frequencies: Counter


def tokenize(text: str) -> List[str]:
    """Lowercase and extract alphanumeric tokens (plus apostrophes)."""
    return re.findall(r"[a-zA-Z0-9']+", text.lower())


def remove_stopwords(tokens: Iterable[str], stopwords: set[str] = DEFAULT_STOPWORDS, min_len: int = 3) -> List[str]:
    """Remove stopwords and very short tokens."""
    return [t for t in tokens if t not in stopwords and len(t) >= min_len]


def analyze_text(text: str, top_n: int = 15, stopwords: set[str] = DEFAULT_STOPWORDS) -> AnalysisResult:
    char_count = len(text)
    tokens = tokenize(text)
    filtered = remove_stopwords(tokens, stopwords=stopwords, min_len=3)
    word_count = len(filtered)

    freq_counter: Counter = Counter(filtered)
    most_common = freq_counter.most_common(top_n)

    return AnalysisResult(
        char_count=char_count,
        word_count=word_count,
        top_n=top_n,
        most_common=most_common,
        frequencies=freq_counter,
    )


def save_ranking(most_common: List[Tuple[str, int]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.write("Top Word Frequencies\n")
        f.write("====================\n")
        for word, count in most_common:
            f.write(f"{word}\t{count}\n")


def show_wordcloud(frequencies: Counter) -> None:
    wordcloud = WordCloud(width=1000, height=600, background_color="white").generate_from_frequencies(frequencies)
    plt.figure(figsize=(12, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud")
    plt.show()


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Analyze text: tokenize, remove stopwords, rank top words, save ranking, and show word cloud."
    )
    p.add_argument(
        "--file",
        type=str,
        default=None,
        help="Optional: path to a text file as input (if omitted, program will ask for input in terminal).",
    )
    p.add_argument(
        "--top",
        type=int,
        default=15,
        help="Number of most frequent words to display/save (default: 15).",
    )
    p.add_argument(
        "--no-viz",
        action="store_true",
        help="Disable word cloud visualization window.",
    )
    p.add_argument(
        "--output",
        type=str,
        default="outputs/word_frequency_top.txt",
        help="Output file for top-frequency list (default: outputs/word_frequency_top.txt).",
    )
    return p


def main() -> None:
    args = build_arg_parser().parse_args()

    if args.file:
        input_path = Path(args.file)
        text = input_path.read_text(encoding="utf-8")
    else:
        text = input("Enter a text: ")

    result = analyze_text(text, top_n=args.top)

    print("\n=== RESULTS ===")
    print(f"Characters (including spaces): {result.char_count}")
    print(f"Words (after cleaning & stopwords removal): {result.word_count}")
    print(f"\nTop {result.top_n} Most Frequent Words:")
    for word, count in result.most_common:
        print(f"{word:<15} {count}")

    output_path = Path(args.output)
    save_ranking(result.most_common, output_path)
    print(f"\nSaved ranking to: {output_path.as_posix()}")

    if not args.no_viz:
        show_wordcloud(result.frequencies)


if __name__ == "__main__":
    main()
