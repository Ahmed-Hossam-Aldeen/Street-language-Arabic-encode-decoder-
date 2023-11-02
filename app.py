import streamlit as st

arabic_dict = {
    'ا': 'ازازة',
    'ب': 'بيت',
    'ت': 'تفاح',
    'ث': 'ثعبان',
    'ج': 'جزمة',
    'ح': 'حصان',
    'خ': 'خضار',
    'د': 'درس',
    'ذ': 'ذئب',
    'ر': 'رياضة',
    'ز': 'زهرة',
    'س': 'سمكة',
    'ش': 'شمس',
    'ص': 'صقر',
    'ض': 'ضفدعة',
    'ط': 'طيارة',
    'ظ': 'ظرف',
    'ع': 'عصير',
    'غ': 'غابة',
    'ف': 'فراشة',
    'ق': 'قلم',
    'ك': 'كتاب',
    'ل': 'لوحة',
    'م': 'مدينة',
    'ن': 'نجمة',
    'ه': 'هرم',
    'و': 'وردة',
    'ي': 'يوم'
    # You can add more letters and corresponding words as needed
}
def encode(sentence):
    words = sentence.split()
    modified_words = []
    
    for i in words:
           if i.startswith('ال'):
              modified_words.append('الس'+i[3:])
              modified_words.append(arabic_dict[i[2]])
           else: 
              modified_words.append('س'+i[1::])
              modified_words.append(arabic_dict[i[0]])
    
    modified_sentence = ' '.join(modified_words)
    return modified_sentence


# Function to decode the sentence
def decode(sentence):
    words = sentence.split()
    modified_words = []
    
    for i in range(len(words)):
        if i % 2 == 0:  # Odd words
           if words[i].startswith('ال'):
              modified_words.append('ال'+words[i+1][0]+words[i][3:])
           else: 
              modified_words.append(words[i+1][0] + words[i][1:])
        
    
    modified_sentence = ' '.join(modified_words)
    return modified_sentence

# Streamlit app
def main():
    st.title(" السغة لمون Encoder/Decoder")

    # User input for encoding/decoding
    input_sentence = st.text_input("Enter a sentence:")

    # Encode button
    if st.button("Encode"):
        encoded_sentence = encode(input_sentence)
        st.write("Encoded Sentence:/n" + encoded_sentence)

    # Decode button
    if st.button("Decode"):
        decoded_sentence = decode(input_sentence)
        st.write("Decoded Sentence:/n" + decoded_sentence)

# Run the app
if __name__ == "__main__":
    main()
