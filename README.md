# Example of a Formative Assessment

This repository provides a simple example of what a formative assessment for the Software Engineering course at Northeastern University London Apprenticeships could look like.

## Background

Historically, learners have submitted Streamlit applications for this course. These applications were rarely deployed and lost marks, so I explored how difficult deployment actually is. It turns out that deploying Streamlit apps is very straightforward and can be done for free on [Streamlit Community Cloud](https://share.streamlit.io/), without the need for professional Python hosting services such as [Render.com](https://render.com/). So, if you decide to use Streamlit, know you can deploy it easily but the course teaches JavaScript which is a great technology to know, so your app - your technology choice.

## User Documentation

### Purpose

This application prompts the user for their name and displays a personalised greeting.

### How to Use

- Visit the [deployed app](https://se-seminar-1-bcbebxtfed4j85fge8rstv.streamlit.app/)
- Type your name into the text box shown on the screen.
- The application will display: Hello name surrounded by flower emojis.

## Technical Documentation

### Running the App Locally

Follow the steps below to run the Streamlit application on your machine.

1.Clone the repository

```bash
git clone https://github.com/EDGENortheastern/se-seminar-1.git
```

2.Create and activate a virtual environment

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

3.Install project dependencies

```bash
pip install -r requirements.txt
```

4.Run

```bash
streamlit run app.py
```