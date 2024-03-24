# Default Configuration for app.
default_config_script = (
    '''// Configure meta data object.
const config = {
    title: 'JS-App',
}

// Setting the default document title.
document.title = config.title

'''
)


# Default Styles for document.
default_config_styles = (
    '''/* Reset default styles. */
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
button {
    font-family: Arial, Helvetica, sans-serif;
}
'''
)


# Default Configuration for Document Boilerplate.
default_document = (
    '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Linked favicon. -->
    <link rel="shortcut icon" href="./assets/icons/favicon.svg" type="image/x-icon">

    <!-- Default document title. -->
    <title>Document</title>

    <!-- Linked config style file. -->
    <link rel="stylesheet" href="./meta/config_styles.css">

    <!-- Linked stylesheet files. -->
    <link rel="stylesheet" href="./styles/styles.css">
</head>

<body>
    <!-- ----------------------------------------- -->
    <!-- Edit here to update document. -->
    <!-- ----------------------------------------- -->

    <!-- Linked config JavaScript file. -->
    <script type="module" src="./meta/config_script.js"></script>

    <!-- Linked JavaScript files. -->
    <script type="module" src="./src/index.js"></script>
</body>

</html>
''')


# Default Styles for user.
default_styles = (
    '''/* CSS Font Size Variables. */
:root {
    
    /* For Display Text  */
    --display: 4rem;
    --display-height: 44px;

    /* For Heading Text  */
    --heading: 2.813rem;
    --heading-height: 36px;

    /* For Title Text  */
    --title: 1.5rem;
    --title-height: 24px;
    --title-spacing: 0.15px;

    /* For Label Text  */
    --label: 1.125rem;
    --label-height: 16px;
    --label-spacing: 0.5px;

    /* For body Text  */
    --body-m: 0.875rem;
    --body-m-height: 20px;
    --body-m-spacing: 0.25px;

    /* Define Color variables */
    --background-color: #fff;
    --text-color: #09090b;
    --header-background: unset;
    --sidebar-background: unset;
    --footer-background: unset;
    --hover-color: unset;
}

/* Body styles. */
body {
    display: grid;
    background-color: var(--background-color);
    grid-template-columns: repeat(12, 1fr);
    height: fit-content;
    width: 100%;
    position: relative;
    overflow: hidden;
    overflow-y: auto;
}

/* Protect Link OverFlow during Click.  */
.protect--link--overflow {
    display: flex;
    overflow: hidden;
    width: fit-content;
}

/* Write your style here.-------------- */
''')


# Default js-app test script.
default_script = (
    '''// Default html, css, and js code for test 
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
    <h1>Welcome to <span>JS-CLI</span></h1>
    <p>
        Now that the App is running with live-server, if you want to change
        the document, please edit the index.html or src/index.js
        file to update the document.
    </p>
    <h1 class="counter"><span class="counter-js">00</span></h1>
    <button id='test-btn-js' type="button">Increment</button>
</section>
`
)

document.body.insertAdjacentHTML('beforeend', default_test_code)

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
''')


# Default js-app favicon.
default_app_favicon = (
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 630 630">
<rect width="630" height="630" fill="#f7df1e"/>
<path d="m423.2 492.19c12.69 20.72 29.2 35.95 58.4 35.95 24.53 0 40.2-12.26 40.2-29.2 0-20.3-16.1-27.49-43.1-39.3l-14.8-6.35c-42.72-18.2-71.1-41-71.1-89.2 0-44.4 33.83-78.2 86.7-78.2 37.64 0 64.7 13.1 84.2 47.4l-46.1 29.6c-10.15-18.2-21.1-25.37-38.1-25.37-17.34 0-28.33 11-28.33 25.37 0 17.76 11 24.95 36.4 35.95l14.8 6.34c50.3 21.57 78.7 43.56 78.7 93 0 53.3-41.87 82.5-98.1 82.5-54.98 0-90.5-26.2-107.88-60.54zm-209.13 5.13c9.3 16.5 17.76 30.45 38.1 30.45 19.45 0 31.72-7.61 31.72-37.2v-201.3h59.2v202.1c0 61.3-35.94 89.2-88.4 89.2-47.4 0-74.85-24.53-88.81-54.075z"/>
</svg>
'''
)
