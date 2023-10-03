import setuptools

with open("README.md", 'r', encoding= "utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "end-to-end-mlops-data-science-project"
AUTHOR_USER_NAME = "ny-essien"
SRC_REPO = "machine_learning_project"
AUTHOR_EMAIL = "nsikan4001@gmail.com"

setuptools.setup(

    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "my first package for machine learning application",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {

        "bug_tracker" : f"https//github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src"), 
)