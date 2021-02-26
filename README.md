# PyFlink-DS
Python Flink (DataStream)
## Team members names  
* Rohitha Reddy Meda  
* Sowmya Thogiti
* Vigneshwar Reddy Lenkala

![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Group/big%20data%20project.png)

## Sowmya Thogiti
### Demonstration skill: 
To read a collection of numbers from 0 to 9, filter the even numbers and multiply them by 10 and finally store them in another collection using PyFlink DataStream.

### Prerequisites:
* Apache Flink Installed (2.12 or 2.11) 
* IntelliJ IDE installed from [source](https://www.jetbrains.com/idea/download/#section=windows)
* PIP installed
* Python 3.7 version installed and set in path of environment variables
* pyflink installed [source](https://pypi.org/project/pyflink/)

### Introduction to DataStream API:  
* Apache Flink offers a DataStream API for building robust, stateful streaming applications.
* It provides fine-grained control over state and time, which allows for the implementation of advanced event-driven systems
* Flink is considered as the next-gen stream processing system.
* Flink offers substantially higher processing speeds to spark and hadoop.
* Flink provides low latency and high throughput

### How to download Flink:
* Check the versions of pip and python in terminal of IntelliJ IDE using:
    * pip --version
    * python --version
* Once the python is of version 3.7.0, use below command to run in terminal opened in IntelliJ IDE using:
    * pip install apache-flink
* Install pyflink using below command in terminal:
  pip install pyflink

### How to setup pyflink:
* open IntelliJ IDE and open the installed path of pyflink from file select.
* Build project from build menu.
* Run whole project and wait for all the dependencies installed into your local machine.
* Start working on pyflink projects.

### Flink set-up using python:
* Create a new file using File\New\Python file
* Provide a new name for the file such as task1.py
* In order to configure python interpreter, we need to select File\Project Structure
* in Project structure, under project settings - project SDK list - select Add sdk list - select python SDK.
* Under Add python SDk Interpreter - select Virtualenv Environment - Base interpreter--select the path of python 3.7(python.exe).
* Click OK
* Click apply and then OK again.
* After applying SDK changes, venv folder is created by default which stores all respective libraries and scripts.  
![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Sowmya/sdk%20setup.png)   

### Source code of above topic:
![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Sowmya/code.JPG)   

### Output:   
![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Sowmya/output.JPG)   

### References:  
* [DataStream API](https://ci.apache.org/projects/flink/flink-docs-stable/dev/python/datastream_tutorial.html)
* [Sample codes](https://ci.apache.org/projects/flink/flink-docs-master/api/python/_modules/pyflink/datastream/data_stream.html)
* [Documentation part](https://ci.apache.org/projects/flink/flink-docs-release-1.9/api/python/pyflink.datastream.html)
* [stackoverflow sol1](https://stackoverflow.com/questions/62820531/python-flink-instalation-failed-to-find-the-file-flink-1-12-snapshot-bin-flink)
* [stackoverflow sol2](https://stackoverflow.com/questions/62232422/flink-cluster-not-starting-due-to-could-not-find-or-load-main-class-error)

### Demonstration video link: 
[Sowmya Demo video](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Sowmya/Sowmya-pyflink-ds.mp4)

## Vigneshwar Reddy Lenkala
### Demonstration skill: 
To read a collection of words, calculate the length of each and return a file with each line containing the word and its length using PyFlink DataStream.

### Prerequisites:
* Apache Flink Installed (2.12 or 2.11)
* PIP installed
* IntelliJ IDE installed
* Python 3.7 version installed 

### Introduction to DataStream API
* Apache Flink is an Open source stream processing framework for distributed, high performance data streaming application.
* Apache Flink offers a DataStream API for building robust, stateful streaming applications.
* It provides fine-grained control over state and time, which allows for the implementation of advanced event-driven systems.
* Flink also provides batch processing, graph processing, Itearative proccessing for Machine learning applications.
* Flink is considered as the next-gen stream processing system.
* Flink offers substantially higher processing speeds to spark and hadoop.
* Flink provides low latency and high throughput

### Installation steps of PyFlink
*  Python version (3.5, 3.6, 3.7 or 3.8) is required for PyFlink. Please run the following command to make sure that it meets the requirements:
-   $ python --version
* Check the version of pip using command:
-   $ pip --version
* Use the below command to install apache-flink 1.12.0
-  $ python -m pip install apache-flink 1.12.0

### Code snippet:

![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Vignesh/Collection%20of%20words%20code%20snippet.png)

### Output snippet:
![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Vignesh/Output.png)

### Demonstration video link: 
[Vignesh Demo Video](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Vignesh/Vignesh-pyflink.mp4)

### References:
* [https://ci.apache.org/projects/flink/flink-docs-stable/dev/python/datastream_tutorial.html](https://ci.apache.org/projects/flink/flink-docs-stable/dev/python/datastream_tutorial.html)
* [https://ci.apache.org/projects/flink/flink-docs-master/api/python/_modules/pyflink/datastream/data_stream.html](https://ci.apache.org/projects/flink/flink-docs-master/api/python/_modules/pyflink/datastream/data_stream.html)
* [https://flink.apache.org/downloads.html#flink](https://flink.apache.org/downloads.html#flink)
* [https://ci.apache.org/projects/flink/flink-docs-release-1.9/api/python/pyflink.datastream.html](https://ci.apache.org/projects/flink/flink-docs-release-1.9/api/python/pyflink.datastream.html)

## Rohitha Reddy Meda
### Demonstration skill:
To read a file containing sentences in each line, filter lines containing a certain word and write them to a new file

### Prerequisites:
* Apache Flink Installed (2.12 or 2.11)
* PIP installed
* IntelliJ IDE installed
* Python 3.7 version installed and set in path of environment variables

### Introduction to DataStream API:
* To develop stable, stateful streaming applications, Apache Flink offers a DataStream API.
* It provides fine-grained state and time control that enables advanced event-driven systems to be introduced.
* Flink is known as the delivery system for next-gen streams.
* For spark and hadoop, Flink provides significantly higher processing speeds.
* Flink provides low latency and high throughput.


### Flink set-up using python:
* Create a new file using File\New\Python file
* Provide a new name for the file such as project1.py
* We must pick File\Project Structure to configure the python interpreter.
* Under Project Structure, under Project Settings - Project SDK List - choice Add SDK List - choose Python SDK.
* Under Add python SDk Interpreter - choose Virtualenv Environment - Base Interpreter—choose python 3.7 road (python.exe).
* Click OK
* Click apply and then OK again.
* The env folder is generated by default after applying SDK changes, which stores all the respective libraries and scripts.

### Code for my topic
![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Rohitha/Code.jpeg)

### Input and Output snip
![](https://github.com/sowmyathogiti/PyFlink-DS/blob/main/images/Rohitha/Input%20and%20output.jpeg)

### Demonstration video link:
* [https://use.vg/MfZg7a](https://use.vg/MfZg7a)

### References:
* [https://ci.apache.org/projects/flink/flink-docs-release-1.9/getting-started/tutorials/local_setup.html](https://ci.apache.org/projects/flink/flink-docs-release-1.9/getting-started/tutorials/local_setup.html)
* [https://data-flair.training/blogs/apache-flink-installation-on-windows/](https://data-flair.training/blogs/apache-flink-installation-on-windows/)
* [https://ci.apache.org/projects/flink/flink-docs-master/api/python/_modules/pyflink/datastream/data_stream.html](https://ci.apache.org/projects/flink/flink-docs-master/api/python/_modules/pyflink/datastream/data_stream.html)
