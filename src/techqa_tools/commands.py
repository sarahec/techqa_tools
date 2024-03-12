from pathlib import Path
from spacy import Language

from .tools import label_corpus, read_corpus_entries, read_corpus_segments, tokenize_corpus


def tokenize(language: Language, input_path: Path, batch_size: int = 1024, processes: int = 1, segment_size: int = 64):
    inputs = read_corpus_entries(
        input_path) if segment_size is None else read_corpus_segments(input_path, segment_size)
    yield from tokenize_corpus(inputs, language, batch_size, processes)


def label_text(language, input_path, batch_size, processes, segment_size):
    inputs = read_corpus_entries(
        input_path) if segment_size is None else read_corpus_segments(input_path, segment_size)
    yield from label_corpus(inputs, language, batch_size, processes)
