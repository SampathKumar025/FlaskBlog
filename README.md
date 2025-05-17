# FlaskBlog

Welcome to FlaskBlog, a simple and customizable blog website built with Flask.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

FlaskBlog is a web application that allows users to create, read, update, and delete blog posts. It's designed to be easy to use and can serve as a starting point for building your own blogging platform. This README provides essential information on how to get started with FlaskBlog.

## Features

- User authentication and registration
- Create, edit, and delete blog posts
- User-friendly web interface
- Customizable with Flask extensions
- Secure and well-documented codebase

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Pip (Python package manager)
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SampathKumar025/FlaskBlog.git
   cd FlaskBlog

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Set up the database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade

5. Start the Flask development server:

    ```bash
    flask run  # or
    py run.py


## Usage

1. Open your web browser and navigate to 'http://localhost:5000'.
2. Register for an account or log in if you already have one.
3. Explore and use the FlaskBlog features to create, edit, and manage your blog posts.
