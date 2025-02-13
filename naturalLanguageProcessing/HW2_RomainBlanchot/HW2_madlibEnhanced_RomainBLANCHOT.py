import random
import nltk
from nltk.corpus import wordnet

def get_synonym(word, pos=None, allow_multiword=False):
    # Check if word is empty or None
    if not word:
        # print(f"DEBUG: Word is empty or None")
        return word
        
    try:
        # Download required NLTK resources
        nltk.download('wordnet', quiet=True)
        nltk.download('omw-1.4', quiet=True)
        
        # print(f"\nDEBUG: Searching synonyms for '{word}'")
        
        # Clean the word and handle multi-word inputs
        word = word.lower().strip()
        if ' ' in word and not allow_multiword:  # Skip multi-word phrases unless allowed
            # print(f"DEBUG: Skipping multi-word phrase: {word}")
            return word
            
        # Get synsets based on part of speech
        if pos == 'verb':
            synsets = wordnet.synsets(word, pos=wordnet.VERB)
        elif pos == 'adj':
            synsets = wordnet.synsets(word, pos=wordnet.ADJ)
        elif pos == 'noun':
            synsets = wordnet.synsets(word, pos=wordnet.NOUN)
        else:
            synsets = wordnet.synsets(word)
        
        # print(f"DEBUG: Found {len(synsets)} synsets")
        
        if synsets:
            # Collect all unique lemmas
            lemmas = []
            for synset in synsets:
                # Get lemma names and their usage counts
                for lemma in synset.lemmas():
                    name = lemma.name()
                    count = lemma.count() or 0  # Get usage frequency, default to 0 if None
                    
                    # Handle multi-word synonyms based on allow_multiword parameter
                    if '_' in name and not allow_multiword:
                        # print(f"DEBUG: Skipping multi-word synonym: {name}")
                        continue
                        
                    if name.lower() != word and name not in [l[0] for l in lemmas]:
                        lemmas.append((name, count))
                        # print(f"DEBUG: Found synonym: {name} (frequency: {count})")
            
            # Sort by usage frequency and get the most common synonym
            if lemmas:
                lemmas.sort(key=lambda x: x[1], reverse=True)
                result = lemmas[0][0].replace('_', ' ')
                # print(f"DEBUG: Returning most frequent synonym: {result}")
                return result
            
            # print(f"DEBUG: No suitable synonyms found, returning original word: {word}")
            return word
                    
        # print(f"DEBUG: No synonyms found, returning original word: {word}")
        return word
        
    except Exception as e:
        print(f"Error finding synonym for '{word}': {str(e)}")
        return word

def software_developer_madlib(use_test_inputs=False):
    print("Welcome to the NLP-Enhanced Mad Lib Game!\n")
    
    if use_test_inputs:
        # Use test inputs
        test_inputs = [
            "futuristic",            # 1. Adjective
            "AI assistant",         # 2. Type of software
            "Python",               # 3. Programming language
            "48",                   # 4. Number
            "memory leak",          # 5. Type of bug
            "challenging",          # 6. Adjective
            "debugging",            # 7. Verb ending in -ing
            "logs",                 # 8. Noun (plural)
            "Google",               # 9. Famous software company
            "blorp",                # 10. Silly word
            "decided",              # 11. Verb (past tense)
            "Elon Musk",            # 12. Famous person
            "brilliant",            # 13. Adjective
            "trophy",               # 14. Noun
            "test",                 # 15. Verb
            "deploy",               # 16. Verb
            "invaluable",           # 17. Adjective
            "laptop"                # 18. Noun
        ]
        mock_inputs = mock_input_generator(test_inputs)
        input_func = lambda prompt: next(mock_inputs)
    else:
        input_func = input
        
    # Collect user input
    adj1 = input_func("Enter an adjective: ")
    software_type = input_func("Enter a type of software: ")
    programming_language = input_func("Enter a programming language: ")
    number = input_func("Enter a number: ")
    bug_type = input_func("Enter a type of bug: ")
    adj2 = input_func("Enter another adjective: ")
    verb_ing = input_func("Enter a verb ending in -ing: ")
    plural_noun = input_func("Enter a plural noun: ")
    famous_company = input_func("Enter a famous software company: ")
    silly_word = input_func("Enter a silly word: ")
    past_verb = input_func("Enter a past tense verb: ")
    famous_person = input_func("Enter a famous person: ")
    adj3 = input_func("Enter another adjective: ")
    noun1 = input_func("Enter a noun: ")
    verb1 = input_func("Enter a verb: ")
    verb2 = input_func("Enter another verb: ")
    adj4 = input_func("Enter another adjective: ")
    noun2 = input_func("Enter another noun: ")
    
    # Get synonyms with appropriate part of speech for all inputs
    adj1 = get_synonym(adj1, 'adj')
    software_type = get_synonym(software_type, 'noun', allow_multiword=True)
    programming_language = get_synonym(programming_language, 'noun')
    bug_type = get_synonym(bug_type, 'noun', allow_multiword=True)
    adj2 = get_synonym(adj2, 'adj')
    verb_ing = get_synonym(verb_ing, 'verb')
    plural_noun = get_synonym(plural_noun, 'noun')
    famous_company = get_synonym(famous_company, 'noun')
    silly_word = get_synonym(silly_word, 'adj')  # Treat silly words as adjectives
    past_verb = get_synonym(past_verb, 'verb')
    famous_person = get_synonym(famous_person, 'noun', allow_multiword=True)
    adj3 = get_synonym(adj3, 'adj')
    noun1 = get_synonym(noun1, 'noun')
    verb1 = get_synonym(verb1, 'verb')
    verb2 = get_synonym(verb2, 'verb')
    adj4 = get_synonym(adj4, 'adj')
    noun2 = get_synonym(noun2, 'noun')
    
    story_templates = [
        f"Once upon a time, in a {adj1} world of software development, there was a {software_type} that was written in {programming_language}.\n"
        f"The developers had only {number} days to get rid of the {bug_type} that kept popping up. It was a {adj2} task, but by {verb_ing} their {plural_noun},\n"
        f"they managed to catch the attention of {famous_company}.\n"
        f"\"Wow, this code is so {silly_word}!\" exclaimed the CEO of {famous_company}. They {past_verb} to hire the team on the spot.\n"
        f"{famous_person} even called them {adj3} and gave them a {noun1} as a token of appreciation.\n"
        f"In the end, the developers learned to always {verb1} before they {verb2}. It was a {adj4} lesson that they would carry with them\n"
        f"to their next project, along with their trusty {noun2}.\n",
        
        f"Deep in the {adj1} corridors of {famous_company}, an elite team of developers was racing against time.\n"
        f"They had to patch a {software_type} bug in {programming_language}, and only {number} days remained before launch!\n"
        f"The {bug_type} issue was a nightmare, but they kept {verb_ing} with their {plural_noun}, hoping for a miracle.\n"
        f"One day, {famous_person} stumbled upon their work and called it {adj3}.\n"
        f"Impressed, they awarded the team a {noun1} and declared their efforts {silly_word}.\n"
        f"From that moment, they knew they must always {verb1} before they {verb2}, carrying their {noun2} as a lucky charm.\n"
    ]
    
    print(random.choice(story_templates))

def mock_input_generator(inputs):
    for item in inputs:
        yield item

# Main execution
print("Choose input mode:")
print("1. Manual input")
print("2. Test inputs")
choice = input("Enter your choice (1 or 2): ")

if choice == "2":
    software_developer_madlib(use_test_inputs=True)
else:
    software_developer_madlib(use_test_inputs=False)
