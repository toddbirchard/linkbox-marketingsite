from flask import request, render_template, flash, url_for, redirect, Blueprint
from flask import current_app as app
import requests
import json
from .forms import URLForm


landing_bp = Blueprint('landing_bp', __name__)


@landing_bp.route('/', methods=['GET', 'POST'])
def homepage():
    """Serve homepage."""
    form = URLForm(request.form)
    if request.method == 'POST':
        if form.validate():
            url = request.form.get('url')
            if 'http' not in url:
                url = 'http://' + url
            print('-----------', url)
            params = {'url': url}
            req = requests.get('https://us-east1-hackersandslackers-204807.cloudfunctions.net/linkbox-api', params=params)
            response = json.loads(req.text)
            response = json.dumps(response, indent=2)
            return render_template('index.html',
                                   form=form,
                                   response=response,
                                   template="home")
        flash('Please enter a URL!')
        return redirect(url_for('landing_bp.homepage'))
    return render_template('index.html',
                           form=form,
                           template="home")
