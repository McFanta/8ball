# A simple fun program based on the magic 8 ball and a remake of Javipepe's 8ball plugin for the nimbus slackbot

def ball8():
    import random

    possible_answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely',
                        'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes'                                                                        'Sign point to yes',
                        'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                        'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no'
                        'Outlook not so good', 'Very doubtful']

    example_question = 'Is Linux better than Windows?'
    #                                ^ obviously yes.
    raw_input("Ask Me a question")
    print(random.choice(possible_answers))

ball8()