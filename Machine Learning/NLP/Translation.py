from textblob import TextBlob

user_input = "Hello World, My name is suvo and im a student of computer science currently in my 3rd year of engineering at SRM Institute of Science and Technology"

pt = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife!"

# url = "http://translate.google.com/translate_a/t?client=te&format=html&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&kc=1"

blob =  TextBlob(user_input)
ans =  blob.translate(to="de") # hindi - hi , bn , mr
print(ans)


quote1 = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."""

quote2 = """Darcy, as well as Elizabeth, really loved them; and they were both ever sensible of the warmest gratitude towards the persons who, by bringing her into Derbyshire, had been the means of uniting them."""

sentiment1 = TextBlob(quote1).sentiment
sentiment2 = TextBlob(quote2).sentiment

print(quote1 + " has a sentiment of " + str(sentiment1))
print(quote2 + " has a sentiment of " + str(sentiment2))
