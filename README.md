# Text Summarization with Transformer Models

This repository implements and evaluates several transformer-based models for text summarization on government report data.

## Models Implemented
- PEGASUS (google/pegasus-cnn_dailymail)
- FLAN-T5 (google/flan-t5-large)
- mT5 (csebuetnlp/mT5_multilingual_XLSum)

## Dataset
The project uses the "govreport-summarization" dataset, which contains long government reports paired with human-written summaries.

## Key Features
- Evaluation of multiple transformer models for text summarization
- ROUGE score calculation for summary quality assessment
- Comparison of summarization strategies on long-form text

## Getting Started
```bash
# Clone the repository
git clone https://github.com/yourusername/text-summarization-project.git
cd text-summarization-project

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook notebooks/tsummarization.ipynb
