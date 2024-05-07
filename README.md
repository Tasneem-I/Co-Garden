# Co-Gardens
# Team
1. **Suchitra M** 
   - Worked on developing Figma prototype of planner page
   - Worked on frontend of the main website using Bootstrap
2. **Tasneem I**
   - Worked on flask and database integration for main website
   - Worked on model training and vector embedding
   - Developed chatbot and its UI using Langchain and Streamlit
3. **Thejuswini R**
   - Worked on frontend development of main website using Bootstrap
   - Helped in data collection and cleaning
4. **Trisheta S**
   - Worked on frontend development of main website using Bootstrap
   - Helped in data collection and cleaning
  
   
# How to Use
1. Clone the repository onto local machine
2. Set environment variable keys for PINECONE_API_KEY and OPENAI_API_KEY.
3. Run app.py
4. Run chat1.py using the command streamlit run chat1.py

# Inspiration
We were inspired to work on Co Gardens by a deep-rooted passion for environmental stewardship and holistic wellness. Witnessing the growing need for sustainable solutions in urban environments, we saw an opportunity to merge our love for gardening with our desire to make a positive impact on the world.
The recognition of the disconnect between people and their food sources further fueled our motivation. We were driven by the belief that reconnecting individuals with the process of growing their own food could not only promote healthier lifestyles but also foster a deeper appreciation for the environment.

Moreover, the alarming rise in food-related health issues and environmental degradation propelled us to take action. We saw Co Gardens as a way to address these pressing concerns by offering a platform for communities to come together, cultivate nutritious produce, and contribute to a more sustainable future.

## What it does
Co-Gardens is an innovative web app focused on promoting sustainability, health and mental well being.  Its primary objective is to assist users in fostering a deeper connection with nature by cultivating their own food even within limited urban spaces.  The app offers a planner feature designed to aid urban gardeners in planning and monitoring their container gardens effectively. It provides customizable templates for users to tailor to their needs, as well as pre-existing templates for commonly grown plants, complete with detailed information on their specific requirements.

Moreover, the app boasts a chatbot feature that is trained on verified gardening data, particularly regarding a plant's growth and nutritional needs, in addition to leveraging ChatGPT's 3.5 Turbo Model. This integration enables users to receive more accurate and prompt suggestions for their gardening queries and challenges. 



## How we built it
We first divided our entire project into three modules : Main Website, Chatbot and Planner.
 The home page, their current location, is built using Bootstrap for frontend development, SQLite3 for backend storage, and Flask for dynamic connectivity and loading. It provides details about the app's purpose, why users should use it, and how to navigate different sections. 

The planner feature offers an interface for users to organize and track their plants, prototyped using figma. It supports two templates: custom and existing. Custom templates allow users to personalize their entries, while existing templates serve as a knowledge base provided by the app, particularly useful for beginners, with additional tips and care instructions. Both templates include a link to the chatbot.

The chatbot is trained on verified and accurate data collected from multiple sources, leveraging the GPT-3.5-Turbo model with the assistance of Langchain. The data is embedded using a sentence transformer (all-MiniLM-L6-v2) into a vector database called Pinecone. When a user queries the chatbot, it refines the input using GPT-3.5-Turbo and converts it to vectors, enabling a similarity search in the database. The content from the database and GPT-3.5-Turbo is combined to provide an accurate response to the user's query. Finally the chat UI is built using Streamlit.

## What we learned
Since we're novices, we've strengthened our knowledge of web construction and natural language processing, which allows us to set up Flask backends with user authentication, build databases for chatbot data, and integrate GPT-3.5 for advanced language processing with ease. Technologies like Pinecone, Streamlit, and Langchain are part of our expanding toolkit and enhance our expertise in collaborative workflows and version control with GitHub. Our expert usage of HTML, CSS, and Bootstrap for front-end integration guarantees a smooth and responsive user experience. By utilizing Figma for UI/UX design, we are able to better grasp the critical impact that interface design plays in how users perceive us and how to improve user happiness through visually appealing and intuitive navigation. Furthermore, we understand how critical it is to get models ready in order to visualize website operation.

## What's next for Co-Gardens
In our Co Gardens project, the integration of innovative technologies holds promising future implications. Implementing a water reminder system ensures efficient and sustainable use of resources, promoting responsible gardening practices. The integration of e-commerce functionalities facilitates a seamless exchange of gardening supplies, fostering community engagement and supporting local businesses. Additionally, incorporating a digital journal feature allows participants to document their experiences, share insights, and contribute to a collective knowledge base, enhancing the collaborative and educational aspects of our gardening initiative. Together, these advancements not only elevate the gardening experience but also pave the way for a more connected and environmentally conscious community.
