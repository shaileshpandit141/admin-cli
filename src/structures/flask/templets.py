from ..code_formatter import CodeFormatter


class FlaskTemplets:
    def __init__(self) -> None:
        pass

    def routes_py(self)-> str:
        return CodeFormatter.format("""
        from flask import Flask, render_template

        app = Flask(__name__)


        @app.route('/')
        def home():
            return render_template("pages/home.html")
        """)

    def run_py(self) -> str:
        return CodeFormatter.format("""
        from src import app

        if __name__ == '__main__':
            app.run(debug=True)
        """)
    
    def base_document(self) -> str:
        return CodeFormatter.format("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            {% block head %}{% endblock head %}
            <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/base.css') }}">
            <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/global.css') }}">
        </head>
        <body>
            {% block body %}{% endblock body %}
            <script type="module" src="{{ url_for('static', filename='js/index.js') }}"></script>
        </body>
        </html>
        """)

    def base_style(self) -> str:
        return CodeFormatter.format("""
        /* Reset default styles. */
        * {
            box-sizing: border-box;
            padding: 0;
            margin: 0;
        }

        /* Setting scroll-behavior. */
        html {
            scroll-behavior: smooth;
        }

        body {
            display: grid;
            font-family: Arial, Helvetica, sans-serif;
            height: fit-content;
            width: 100%;
            position: relative;
            overflow: hidden;
            overflow-y: auto;
        }

        /* Apply font on input and button tags. */
        input,
        input::placeholder,
        button {
            font-family: Arial, Helvetica, sans-serif;
        }
        """)
    
    def global_style(self) ->str:
        return CodeFormatter.format("""
        /* Body styles */
        body {
            grid-template-columns: repeat(12, 1fr);
        }


        /* Protect Link OverFlow during Click.  */
        .protect--link--overflow {
            display: flex;
            overflow: hidden;
            width: fit-content;
        }


        .main-layout {
            grid-column: 2/-2;
        }
        """)

    def index_script(self) -> str:
        return CodeFormatter.format("""
        // Default html, css, and js code for test 
        const default_test_code = (
            `<!-- App test code, injected by JavaScript using src/index.js file. -->
            <style>
            .test {
                grid-column: 2/-2;
                font-family: Arial, Helvetica, sans-serif;
                height: fit-content;
                min-height: 100vh;
                width: 100%;
                user-select: none;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }

            h1 {
                font-size: 28px;
                text-align: center;
                letter-spacing: 0.03em;
                line-height: 24px;
            }
            
            p {
                margin-block: 16px;
                font-size: 14px;
                letter-spacing: 0.03em;
                line-height: 1.5;
                text-align: center;
                width: 100%;
                min-width: 0;
                max-width: 450px;
            }

            span {
                text-wrap: nowrap;
                letter-spacing: 0.03em;
                color: #7f02ad;
            }

            .counter {
                font-size: 16px;
                letter-spacing: 0.03em;
                font-weight: 600;
                padding: 8px 16px;
                border-radius: 999rem;
                margin-bottom: 8px;
            }

            button {
            font-size: 16px;
            letter-spacing: 0.03em;
            font-weight: 600;
            border: none;
            padding: 8px 16px;
            border-radius: 999rem;
            background-color: #e7e7e7;
            transition: background-color 0.3s ease-in-out. outline 0.3s ease-in-out;
            }

            button:hover {
                background-color: #dadada;
                outline: 3.5px solid #7f02ad57;
            }
        </style>
        <section class="test">
            <h1>Welcome to <span>Admin-CLI</span></h1>
            <p>
                Now that the App is running with flask-server, if you want to change
                the document, please update your flask web app
                to update the document.
            </p>
            <h1 class="counter"><span class="counter-js">00</span></h1>
            <button id='test-btn-js' type="button">Increment</button>
        </section>
        `
        )

        document.querySelector(".home-content").insertAdjacentHTML('beforeend', default_test_code)

        const counter = document.querySelector(".counter-js")
        const testBtn = document.getElementById('test-btn-js')
        let defaultCounterState = 1

        testBtn.addEventListener('click', () => {
            if (defaultCounterState < 10) {
                let temp = `0${defaultCounterState}`
                counter.innerHTML = temp
                defaultCounterState += 1
            } else {
                counter.innerHTML = defaultCounterState
                defaultCounterState += 1
            }
        })
        """)
    
    def header_document(self) -> str:
        return CodeFormatter.format("""
        <header>
            <!--Header links-->
        </header>
        """)
    
    def footer_document(self) -> str:
        return CodeFormatter.format("""
        <footer>
            <!--Header links-->
        </footer>
        """)
    
    def main_layout_document(self) -> str:
        return CodeFormatter.format("""
        {% extends "base.html" %} 

        {% block body %}
        <div class="main-layout">
        {% block content %}{% endblock content %}
        </div>
        {% endblock body %}
        """)
    
    def home_document(self) -> str:
        return CodeFormatter.format("""
        {% extends "layouts/main-layout.html" %} 

        {% block head %}
        <title>Flask-App: Created by Admin-CLI</title>
        {% endblock head %}

        {% block content %}
        <section class="home-content">
            <!--Our Home Content-->
        </section>
        {% endblock content %}
        """)

