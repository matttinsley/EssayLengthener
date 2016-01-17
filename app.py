from flask import Flask, render_template
import redis
import ast

app = Flask(__name__)
app.debug = True


@app.route("/word/<word>")
def thesaurus_lookup(word):
    r_server = redis.Redis("localhost")
    synonyms = r_server.get(word)
    print "synonyms:", synonyms
    if synonyms:
        synonyms = ast.literal_eval(synonyms)
    else:
        synonyms = ["No synonyms"]
    return render_template('home.html', word=word, synonyms=synonyms)


if __name__ == "__main__":
    app.run()

