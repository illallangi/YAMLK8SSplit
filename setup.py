import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="yaml-k8s-split-illallangi",
  version="0.0.1",
  author="Andrew Cole",
  author_email="andrew.cole@illallangi.com",
  description="Splits Kubernetes YAML resources into seperate files based on .kind, .metadata.namespace and .metadata.name.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/illallangi/YAMLK8SSplit",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  entry_points = {
    'console_scripts': ['yamlk8ssplit=yaml_k8s_split.__cli__:main'],
  },
  install_requires=[]
)