def process_text(text, reverse=False, *args, **kwargs):
    if reverse:
        text = text[::-1]
    additional_text = ' '.join(args)
    separator = kwargs.get('separator', '')  
    additional_processing = kwargs.get('additional_processing', lambda x: x) 
    text = additional_processing(text)
    result = text + separator + additional_text
    return result
original_text = "Hello, world!"
additional_text = "This is additional text."
reversed_text = process_text(original_text, reverse=True)
combined_text = process_text(original_text, additional_text, separator=' | ')
print(reversed_text)  
print(combined_text) 