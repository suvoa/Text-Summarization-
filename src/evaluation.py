from rouge_score import rouge_scorer

def evaluate_summary(reference, generated):
    """
    Evaluate generated summary against reference using ROUGE scores.
    
    Args:
        reference (str): Reference summary
        generated (str): Generated summary
        
    Returns:
        dict: Dictionary containing ROUGE scores
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, generated)
    
    return {
        'rouge1': scores['rouge1'].fmeasure,
        'rouge2': scores['rouge2'].fmeasure,
        'rougeL': scores['rougeL'].fmeasure
    }

def print_evaluation_results(scores, model_name=""):
    """Print evaluation results in a formatted way."""
    print(f"\n🔹 {model_name} ROUGE Scores:")
    print(f"  ROUGE-1: {scores['rouge1']:.4f}")
    print(f"  ROUGE-2: {scores['rouge2']:.4f}")
    print(f"  ROUGE-L: {scores['rougeL']:.4f}")
