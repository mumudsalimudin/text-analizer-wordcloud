from src.text_analyzer import tokenize, remove_stopwords, analyze_text

def test_tokenize_basic():
    assert tokenize("Hello, World!") == ["hello", "world"]

def test_remove_stopwords_basic():
    tokens = ["ini", "adalah", "contoh", "teks"]
    filtered = remove_stopwords(tokens)
    assert "contoh" in filtered and "teks" in filtered
    assert "ini" not in filtered and "adalah" not in filtered

def test_analyze_text_top_n():
    res = analyze_text("kata kata kata lain", top_n=1)
    assert res.most_common[0][0] == "kata"
