def software_developer_madlib():
    adj1 = input("Enter an adjective: ")
    software_type = input("Enter a type of software: ")
    programming_language = input("Enter a programming language: ")
    number = input("Enter a number: ")
    bug_type = input("Enter a type of bug: ")
    adj2 = input("Enter another adjective: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    plural_noun = input("Enter a plural noun: ")
    famous_company = input("Enter a famous software company: ")
    silly_word = input("Enter a silly word: ")
    past_verb = input("Enter a past tense verb: ")
    famous_person = input("Enter a famous person: ")
    adj3 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    adj4 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    
    story = f"""
    Once upon a time, in a {adj1} world of software development, there was a {software_type} that was written in {programming_language}.
    The developers had only {number} days to get rid of the {bug_type} that kept popping up. It was a {adj2} task, but by {verb_ing} their {plural_noun}, 
    they managed to catch the attention of {famous_company}.
    \"Wow, this code is so {silly_word}!\" exclaimed the CEO of {famous_company}. They {past_verb} to hire the team on the spot. 
    {famous_person} even called them {adj3} and gave them a {noun1} as a token of appreciation.
    
    In the end, the developers learned to always {verb1} before they {verb2}. It was a {adj4} lesson that they would carry with them 
    to their next project, along with their trusty {noun2}.
    """
    
    print(story)

software_developer_madlib()
