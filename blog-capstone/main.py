from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

main_title = 'The Kohelet'
footer = 'Refined in a furnace, purified seven times by the LORD.'

blog_url = 'https://api.npoint.io/c523ddd127f93831aaf4'

@app.route('/')
def home():
    r = requests.get(blog_url)
    all_posts = r.json()
    return render_template('index.html', posts=all_posts, main_title=main_title, footer=footer)


@app.route('/blog/id=<blog_id>')
def blog(blog_id):
    print(blog_id)
    blog_id = int(blog_id)
    r = requests.get(blog_url)
    all_posts = r.json()
    return render_template('post.html', posts=all_posts, blog_id=blog_id, main_title=main_title, footer=footer)


def random_yes():
    yes_list = ['Absolutely!', 'Yep!', 'You got it!', 'Of course!', 'Right-O!', 'Heck yeah!', 'No doubt!']
    yes = random.choice(yes_list)
    return yes

app.jinja_env.globals.update(random_yes=random_yes)

if __name__ == '__main__':
    app.run(debug=True)
