def calc_f1_score(tp, fp, fn):
    # Validate input types
    if not all(isinstance(x, int) for x in [tp, fp, fn]):
        print("tp, fp, and fn must be integers")
        return

    # Validate input values
    if any(x <= 0 for x in [tp, fp, fn]):
        print("tp, fp, and fn must be greater than 0")
        return

    try:
        # Calculate Precision
        precision = tp / (tp + fp)

        # Calculate Recall
        recall = tp / (tp + fn)

        # Calculate F1-Score
        f1_score = 2 * precision * recall / (precision + recall)

        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1_score:.4f}")
    except ZeroDivisionError:
        print("Error in calculation due to division by zero")


# Example usage:
calc_f1_score(10, 5, 3)
