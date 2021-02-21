# Homeworks-Lawyer-online
Contains the results of homework.

![1.png](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/1.png)

# Project name: 
Lawyer-online </br>
Web application: https://cryptic-sierra-19326.herokuapp.com/#
    
# Description: 
The project aims to automate legal advice. Because the project there is a limited time - 8 weeks - at the moment, the program will not work perfectly. According to the description of the situation, several probable articles will be selected that could be suitable for this situation, for the sake of specificity later the program will ask additional questions that it will need for the final decision. Information on sources can be found [here](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/wiki). More information on the motivation for choosing such topics can be found behind this [link](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%960).

Legal decisions are often subjective, as they use human resources that are somehow interested in one of the parties. Automation of legal processes should make these processes less subjective and fairer over time. Obviously, the work on this project should take much longer. However, for this period of time you can definitely function this programs to simplify the work in the field of jurisprudence, namely the classification of criminal situations, and then improve.

Input: situation from the user </br>
Weekend: a selection of articles of the Criminal Code of Ukraine

# Structure:
* docs(all the text files that were necessary to perform dz):

    * adt - description of ATD used in homework
    * analysis - analysis of the results obtained during the cycle of homework
    * api - functionality Natural Language API
    * data - a description of the data obtained to achieve the result and a plan for working on them
    * get_data_capacity - description of the data obtained after completing the cycle of homework
    * modules - capabilities of moguls to be used for data analysis
    * posts - reviews of 3 posts related to the topic of homework and the section of computer science involved in it
    * proposition - a description of what can be done with Natural Language API
    * questions - answers to questions to choose a topic
    * requirements - functional and non-functional system requirements
    
* examples(examples for working with modules for data processing):

    * kku.csv - file with the contents of the Criminal Code of Ukraine, which was used for reading
    * modules_for_data.py - module with examples of the use of libraries for data processing
    
* images(contains images used for formatting wiki and README):

    * 0.png
    * 1.png
    * ...
    
* modules(a folder with modules for the implementation of the planned homework cycle):

    * kku(folder for working with the content file of the Criminal Code of Ukraine):
    
        * trans - folder with the contents of the translator's implementation
        * article-adt_sample.py - module-example of use Article ADT
        * articls_with_punkts.xlsx - the result of processing the Criminal Code
        * chocing_relevant_information_in_articles.py - module with implementation Article ADT as a class Article(more about the work of              methods can be read in docs.adt), this module also selects important words and synonyms for each gender using a method in                this class
        * creating_file_for_articles_with_punkts.py - module with implementation KKU ADT as a class KKU, similarly as above, you can                  read more about the methods in the specified file, this module actually creates a file-result of processing the criminal                code articles_with_punkts.xlsx.
        * kku.csv - file with the contents of the Criminal Code
        * kku_adt_sample.py - module-example of use KKU ADT
        
    * pytextrank - folder with the content of the implementation of the selection of important words from the sentence
    * samples_reading(folder with modules for reading situations-examples):
    
        * 1.csv - file with the contents of the collection of problems in criminal law
        * 2.csv - file with the contents of the collection of problems in criminal law
        * sample_adt_sample.py - module-example of use Sample ADT
        * samples.py - module for implementation Sample ADT as a class Sample, You can read more about the methods of this class in the              file, described above, this mogul creates files-results of processing of collections
        * samles.xlsx - the result of processing the collection of problems in criminal law 1
        * samles_2.xlsx - the result of processing the collection of problems in criminal law 2
        
    * web_application(a folder containing everything you need to create a web application and process custom input):
        * my_app(application folder):
        
            * reading_users_situation(folder to save everything related to the processing of user situations):
            
                * persons(folder for saving modules for processing actors in a situation):
                    person.py - module for class implementation Person
                * read_save_input.py - module for implementation UsersSituaion ADT as a class UsersSituation, used to read and process                       user data (more about the methods in the file described above)
                
            * static(folder to save all the files needed to design a web application)
            * template(folder for saving html files for web application):
            * articles_with_punkts.xlsx - file with articles, paragraphs and important words for each article
            * result.xlsx - file for recording user data
            * run.py - module to run the application
            * users_history.xlsx - file to save user history
            
* samples(folder with examples of using ATD):

    * 2.csv - data file for Samples ADT 
    * articles_adt_sample.py - module-example of use Articles ADT
    * articles_with_punkts.xlsx - data file for use Articles ADT
    * kku.csv - data file for use KKU ADT
    * kku_adt_sample.py - module-example of use KKU ADT
    * sample_adt_sample.py - module example of use Sample ADT
    

# Table of Contents: 
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contribution)
4. [Credits](#credits)
5. [License](#license)

# Installation:

Simple enough to use
<pre>
git clone https://github.com/lianaonyshkiv/Homeworks-Lawyer-online
</pre>

Then run run.py, that in my_app, та перейти за посиланням у терміналі
![8.png](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/8.png)

# Usage:

After going to the site you will see the following display
![9.png](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/9.png)
Flipping down will be
![10.png](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/10.png)
![11.png](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/11.png)
![12.png](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/12.png)
The last image shows that it is possible to enter your situation in a special place.
Enter it and get the result.
Works only in Ukrainian.
It is not necessary to fill in all fields.

For example, after entering "Шахрайство"(discription can de also longer) the result will look like this
![14.jpg](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/14.png)
![15.jpg](https://github.com/lianaonyshkiv/Homeworks-Lawyer-online/blob/master/images/15.png)

# Contribution:

Please follow the style when loading versions. In general, "fork-and-pull" Git workflow.

1) Fork the repo on GitHub
2) Clone the project to your own machine
3) Commit changes to your own branch
4) Push your work back up to your fork
5) Submit a Pull request so that we can review your changes

# Credits:

You can be here!

# License:
[MIT](https://choosealicense.com/licenses/mit/)
