# DS 4003 Final Project: CO2 Emissions Per Capita Data from Different Countries Over the Years

Praggnya Kanungo - DS 4003, Spring 2024 Final Project: CO2 Emissions Per Capita Data from Different Countries Over the Years 

This is the final project for DS 4003. This project uses a dataset with the CO2 emissions per capita measurements of different countries in different years. I explored and cleaned this data before applying it to this dashboard. The original data set can be found on Gapminder. Here is the source URL: http://gapm.io/dco2_consumption_historic.

This dashboard uses Dash, Plotly, HTML, and Python. The live dashboard is linked here:
https://co2-emissions-per-capita-dashboard.onrender.com/


## Overview
This interactive dashboard’s purpose is to visualize and analyze CO2 emissions per capita across various countries over time. Through this dashboard, users are enabled to explore global trends, country-specific data, year-specific data, and comparisons among multiple countries through the four modes provided in the dashboard. The purpose of this interactive dashboard is to provide insights into the impact of carbon emissions on climate change, allowing users to understand and visualize this data-driven information interactively. It doesn’t matter what your background or purpose for visiting this dashboard is; once you visit, you will see the terrible increase in CO2 emissions per capita data for any given country, including yours, over the years. This dashboard is a call for change and action; it aims to allow users to explore the recorded data themselves, putting them face to face with the terrible truth of climate change and how countries around the world constantly aid in worsening this condition with high CO2 emissions. 

## Building Process
The dashboard was built using the Dash framework with Bootstrap Minty styling for a modern and responsive design. The core technologies and libraries used in this project include the following:
- Dash for building the interactive user interface
- Plotly Express for creating dynamic and customizable graphs
- Bootstrap for consistent styling and responsive design elements
- Pandas for data manipulation and analysis

Creating this project was done in a properly organized way, in a series of sprints. In the first sprint, I only started with a vague conceptual design for what I wanted this dashboard to be and I created user profiles to understand who my audience is and how I can tailor my dashboard properly towards them. The next sprint required actually finding and properly cleaning the dataset to be used. In this sprint, I was able to explore my data properly and understood what can and can not be done with the information and data I have. Once I cleaned and understood my dataset, in the next sprint, I went on and made a layout for the UI|UX elements to be featured on my dashboard. In the fourth sprint, I made part of my functioning dashboard (implementing only one of the modes). Doing this sprint helped me understand how I can make my final product more functioning and appealing to the audience. Finally, with the implementation of the remaining modes and final touches, the final project was ready. Through the building process, I always did my initial work on a Jupyter Notebook, and then later integrated the code into my GitHub as a .py file. Doing the work initially on a Jupyter Notebook helped me make very quick and accessible changes to my code. In conclusion, the building process, which includes the sprints and the use of tools like the Jupyter Notebook, helped me achieve my final result in a seamless way since I was able to seek feedback when needed at each stage. All sprints are in the sprints folder in this repository.

## Data Science Concepts
During the development of this dashboard, I depended on and used various data science concepts:
- **Data Exploration**: This project required me to understand the structure and content of the dataset I used, identify relevant columns, and explore the relationships between data points in order to understand what sort of a dashboard I can put forward with it.
- **Data Cleaning**: I bettered my data handling skills by depending on Pandas for all sorts of things that include but are not limited to the following: handling missing or inconsistent data, ensuring proper data types, removing duplicates to ensure data integrity, applying filters, melting my data, and analyzing the data for insights.
- **Data Visualization**: In this project, I created meaningful visualizations to communicate insights and used Ploty Express to do so. I created line graphs, histograms, box plots, violin plots, and bar graphs to represent different aspects of the data and ensure proper visualization.
- **Interactivity**: Interactivity was the key in the dashboard, and I implemented interactivity by using Dash. Implementing interactivity in the dashboard included using callbacks, allowing users to select modes, countries, and year ranges, and updating graphs in real time. I also used Dash elements such as range sliders, dropdowns, and radio buttons.

In this dashboard, I hoped to give users a simplified but meaningful experience in using the dashboard, creating a huge focus on UX design for my purpose. To abide by my focus, I focused on creating a clear, logical, non-clustered order of things to provide a smooth user experience. Interactive development is important to data science and the entire class utilized these methods and improved the dashboards in cycles, and I did the same. I received constant feedback to improve the dashboard’s design, layout, and functionality. Another concept in data science is proper documentation and I utilized with concept by ensuring clear code documentation and sharing the project on GitHub.

## Strengths
Through this dashboard, I’ve demonstrated several key strengths:
- **Ability to Create an User-Friendly Interface**: Through using external stylesheets and UI design principles, I created a properly, clear implementation of the visual interface elements of this dashboard.
- **Understanding and Implementing Interactivity**: By using Dash and implementing interactive elements, such as sliders, dropdowns, and radio buttons, I was able to enhance user engagement and allow for dynamic data exploration.
- **Being Able to Create and Curate Comprehensive Visualizations**: The variety of visualizations used in the dashboard provides a thorough overview of CO2 emissions trends and patterns. I implemented these Visualizations through Plotly Express.

## Learning Experiences
Developing this dashboard provided a multitude of valuable learning experiences:
- **Working with Data**: This project entirely depended on working with data and learning how to manipulate, clean, and visualize data using Pandas and Plotly was a big learning experience. With this experience, I learned how important it is to make sure to first explore your data properly and in depth before doing any sort of handling. This is a very valuable thing to learn and keep in mind for me, and I am grateful this project has allowed me to learn this. Along with that, I learned a lot about Pandas and how incredibly powerful this is as a tool for data manipulation and handling. I hope to keep using and learning even more about Pandas in the future.
- **Dashboard Development**: With this project, I gained an understanding of the structure and workflow of a Dash application, including the use of callbacks to update content dynamically. This was a completely new thing for me, but my Dashboard almost depended entirely on proper callbacks, making this a huge learning experience for me, allowing me to gain skills in Dash.
- **Improving Data Visualization Skills**: With this project, I gained experience in creating effective visualizations to communicate complex data in a clear and accessible manner. I had big takeaways from this, and the biggest takeaway was that it matters what type of graph you use! Different graphs will communicate the same data in different ways, so as a data scientist I must always properly consider the purpose of communicating this data before I choose a mode of visualization.

## Conclusion
In conclusion, the CO2 Emissions Per Capita Dashboard serves as a tool to explore and analyze CO2 emissions data and helps provide valuable insights into global trends and country-specific information. My intention with this was to raise awareness about climate change and encourage action towards a more sustainable future. 
