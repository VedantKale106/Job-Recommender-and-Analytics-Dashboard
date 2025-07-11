# Job Recommender and Analytics Dashboard

## Project Overview

This project provides a comprehensive solution for job recommendations based on individual skills and offers an analytical dashboard to visualize key insights from job market data. The core of this project involves data transformation, exploratory data analysis (EDA), and a web application for interactive job recommendations, complemented by a Power BI dashboard for deeper insights.

-----

## Table of Contents

  - [Project Overview](https://www.google.com/search?q=%23project-overview)
  - [Features](https://www.google.com/search?q=%23features)
  - [Project Structure](https://www.google.com/search?q=%23project-structure)
  - [Setup and Installation](https://www.google.com/search?q=%23setup-and-installation)
  - [Usage](https://www.google.com/search?q=%23usage)
  - [Power BI Dashboard](https://www.google.com/search?q=%23power-bi-dashboard)
  - [Data Source](https://www.google.com/search?q=%23data-source)
  - [Contributing](https://www.google.com/search?q=%23contributing)
  - [License](https://www.google.com/search?q=%23license)

-----

## Features

  * **Skill-Based Job Recommendation:** Input your skills and get a ranked list of job titles with a match percentage, highlighting matched and missing skills.
  * **Top Skills Identification:** Visualize the most in-demand skills from the dataset.
  * **Job Description Word Cloud:** Understand common keywords and themes in job descriptions.
  * **Interactive Web Application:** A user-friendly Flask application for real-time job recommendations and skill suggestions.
  * **Power BI Analytics Dashboard:** A rich, interactive dashboard for exploring job market trends, skills, and certifications.

-----

## Project Structure

```
.
├── Data Transformation.py
├── Dataset.csv
├── EDA.ipynb
├── PowerBi Report.pbix
├── job_certs.csv
├── job_main.csv
├── job_skills.csv
└── Website/
    ├── app.py
    └── templates/
        ├── index.html
        └── result.html
```

  * **`Dataset.csv`**: The raw input dataset containing job titles, descriptions, skills, and certifications.
  * **`Data Transformation.py`**: A Python script to preprocess the `Dataset.csv`, splitting skills and certifications into separate, normalized CSVs (`job_skills.csv`, `job_certs.csv`) suitable for analysis and Power BI. It also exports the main job data as `job_main.csv`.
  * **`EDA.ipynb`**: A Jupyter Notebook (converted to `.py` for this README) performing Exploratory Data Analysis. It includes:
      * Loading and inspecting the dataset.
      * Transforming skill and certification strings into lists.
      * Identifying and visualizing the top 20 most in-demand skills.
      * Generating a word cloud from job descriptions.
      * Contains the `recommend_jobs` function, which is also used in the web application.
  * **`PowerBi Report.pbix`**: The Power BI desktop file containing the interactive dashboard for deeper data insights.
  * **`job_skills.csv`**: Transformed data showing each job title mapped to individual skills.
  * **`job_certs.csv`**: Transformed data showing each job title mapped to individual certifications.
  * **`job_main.csv`**: The main job dataset, cleaned and ready for use.
  * **`Website/`**:
      * **`app.py`**: The Flask web application for the job recommender. It loads the dataset, processes user input, and serves job recommendations.
      * **`templates/`**: Contains HTML templates (`index.html`, `result.html`) for the web application's user interface.

-----

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**

    ```bash
    pip install pandas matplotlib seaborn scikit-learn flask wordcloud
    ```

4.  **Ensure you have the `Dataset.csv` file in the root directory.**

-----

## Usage

### 1\. Data Transformation

Run the `Data Transformation.py` script to prepare the data. This will create `job_skills.csv`, `job_certs.csv`, and `job_main.csv`.

```bash
python "Data Transformation.py"
```

### 2\. Exploratory Data Analysis (EDA)

The `EDA.ipynb` notebook demonstrates the data understanding and visualization steps. You can open it with Jupyter Notebook or JupyterLab:

```bash
jupyter notebook EDA.ipynb
```

Execute the cells in the notebook to see the data insights, including top skills and the job description word cloud.

### 3\. Web Application

Navigate to the `Website` directory and run `app.py`:

```bash
cd Website
python app.py
```

Open your web browser and go to `http://127.0.0.1:5000/` (or the address provided in your terminal) to access the job recommender. Enter your skills (comma-separated) to get job recommendations.

-----

## Power BI Dashboard

The `PowerBi Report.pbix` file contains the interactive Power BI dashboard. To explore it:

1.  **Download and install Power BI Desktop** if you haven't already.
2.  **Open `PowerBi Report.pbix`** with Power BI Desktop.

The dashboard allows you to:

  * Analyze job market trends.
  * Identify popular skills and certifications.
  * Filter jobs by various criteria.

-----

## Data Source

The project utilizes `Dataset.csv`, which contains job postings with titles, descriptions, associated skills, and certifications.

-----

## Contributing

Contributions are welcome\! If you have suggestions for improvements or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

-----
