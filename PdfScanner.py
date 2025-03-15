import fitz  
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def summarize_text(text, num_sentences=5):
    """Summarize the extracted text using LSA (Latent Semantic Analysis)."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return "\n".join(str(sentence) for sentence in summary)

def summarize_pdf(pdf_path, num_sentences=5):
    """Extract and summarize text from a PDF file."""
    text = extract_text_from_pdf(pdf_path)
    return summarize_text(text, num_sentences)

if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Change this to your PDF file path
    num_sentences = 5  # Adjust the number of summary sentences
    summary = summarize_pdf(pdf_path, num_sentences)
    print("\nSummary:\n", summary)
