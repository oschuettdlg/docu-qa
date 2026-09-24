import argparse
import glob
import os

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def load_chunks(folder, size=400, overlap=80):
    chunks = []
    for path in glob.glob(os.path.join(folder, "**", "*.md"), recursive=True):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        step = max(1, size - overlap)
        for i in range(0, max(1, len(text) - overlap), step):
            chunks.append({"src": path, "text": text[i:i + size]})
    return chunks


class MiniRAG:
    def __init__(self, folder):
        self.chunks = load_chunks(folder)
        if not self.chunks:
            raise SystemExit("no .md files found under %s" % folder)
        self.vec = TfidfVectorizer(stop_words="english")
        self.mat = self.vec.fit_transform([c["text"] for c in self.chunks])

    def search(self, query, k=4):
        q = self.vec.transform([query])
        scores = (self.mat @ q.T).toarray().ravel()
        top = np.argsort(-scores)[:k]
        return [(self.chunks[i], float(scores[i]))
                for i in top if scores[i] > 0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("question")
    args = ap.parse_args()
    rag = MiniRAG(args.folder)
    hits = rag.search(args.question)
    if not hits:
        print("no relevant chunks found")
        return
    for hit, score in hits:
        print("--- %s (%.3f)" % (hit["src"], score))
        print(hit["text"].strip()[:300])


if __name__ == "__main__":
    main()
