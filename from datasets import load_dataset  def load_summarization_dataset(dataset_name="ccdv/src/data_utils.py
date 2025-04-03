from datasets import load_dataset

def load_summarization_dataset(dataset_name="ccdv/govreport-summarization", split="train"):
    """
    Load the summarization dataset.
    
    Args:
        dataset_name (str): Name of the dataset
        split (str): Dataset split to use (train, validation, test)
        
    Returns:
        dataset: HuggingFace dataset
    """
    return load_dataset(dataset_name, split=split)

def get_sample(dataset, idx=0):
    """
    Get a sample from the dataset.
    
    Args:
        dataset: HuggingFace dataset
        idx (int): Index of the sample
        
    Returns:
        tuple: (text, summary)
    """
    sample = dataset[idx]
    return sample["report"], sample["summary"]

def print_sample_info(text, summary, generated=None, max_chars=300):
    """Print information about a sample in a formatted way."""
    print(f"\n🔹 Original Text (first {max_chars} chars):")
    print(f" {text[:max_chars]}...\n")
    
    if generated:
        print(f"\n🔹 Generated Summary:")
        print(f" {generated}\n")
    
    print(f"\n🔹 Reference Summary:")
    print(f" {summary}")
