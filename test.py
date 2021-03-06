# -*- coding: utf-8 -*-
"""
    Flask-BS - Another flask extension that provides Bootstrap CSS, JS and HTML5 boilerplate.

    Author: Bill Schumacher <bill@servernet.co>
    License: LGPLv3
    Copyright: 2016 Bill Schumacher, Cerebral Power
** GNU Lesser General Public License Usage
** This file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
"""
from flask import Flask

from flask_bs import Bootstrap, render_content_with_bootstrap

app = Flask(__name__)
app.config['BOOTSTRAP_EXCLUDE_JQUERY'] = False
bs = Bootstrap(app)


@app.route("/")
def hello():
    return render_content_with_bootstrap()


if __name__ == "__main__":
    app.run()
