# Job Recommender and Analytics Dashboard

## Project Overview

This project provides a comprehensive solution for job recommendations based on individual skills and offers an analytical dashboard to visualize key insights from job market data. The core of this project involves data transformation, exploratory data analysis (EDA), and a web application for interactive job recommendations, complemented by a Power BI dashboard for deeper insights.

-----

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Power BI Dashboard](#power-bi-dashboard)
- [Data Source](#data-source)
- [Contributing](#contributing)

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

## Screenshots

<img width="1167" height="651" alt="Image" src="https://github.com/user-attachments/assets/2551024f-cf8a-49d9-8076-9c23eadf9c69" />

<img width="1163" height="649" alt="Image" src="https://github.com/user-attachments/assets/891169ec-5ddc-48b5-95ee-d2b3fd3c9e82" />

<img width="1162" height="656" alt="Image" src="https://github.com/user-attachments/assets/b95fc98d-f0f6-431e-b78a-b6eb30a29723" />

<img width="1885" height="912" alt="Image" src="https://github.com/user-attachments/assets/1d826977-f1e0-4738-b97e-cd3fa10dd3a2" />

<img width="1888" height="912" alt="Image" src="https://github.com/user-attachments/assets/b9c0facd-1034-4e70-8bc7-3bab17525a33" />

<img width="1884" height="917" alt="Image" src="https://github.com/user-attachments/assets/31fb9732-affa-4e73-9c2c-db870a8d2871" />

<img width="1883" height="921" alt="Image" src="https://github.com/user-attachments/assets/4f5ed201-50e2-434f-975d-f7b161881fbe" />

<img width="1879" height="919" alt="Image" src="https://github.com/user-attachments/assets/e13a5d08-c796-47b3-906b-e8a66a50feea" />



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
