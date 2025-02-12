# Multimodal AI System for Custom Output Generation

# Overview

This project integrates Vision AI (YOLOv8) and Language Models (LLMs) to create a seamless multimodal AI application. The system analyzes uploaded images, extracts relevant details using YOLOv8, and dynamically generates user-defined outputs through an LLM. Outputs can range from concise summaries to creative descriptions or detailed analytical reports, customized to the user's needs.

# Features

✅ AI-Powered Image Analysis → Uses YOLOv8 to detect objects in images

✅ Dynamic Prompt Generation → Generates smart prompts for LLM based on detected objects

✅ Custom Output Modes → Choose between a concise summary, creative description, or detailed report

✅ Region-Specific Naming → Adjusts object names based on user location (e.g., “Truck” → “Lorry” in UK)

✅ Multilingual Support → Translates generated text into any selected language

✅ Easy API Integration → Works with OpenAI's GPT-4 or GPT-3.5


# Architecture

1. Image Upload & Preprocessing:

   Users upload an image for analysis.

   The system preprocesses the image for object detection.

2. Vision AI Analysis:

   YOLOv8 detects objects and extracts descriptive details (e.g., labels, bounding boxes).

3. Dynamic Prompt Creation:

   Extracted details are converted into prompts tailored to the user's desired output type.

4. LLM Integration:

   The LLM generates user-specific outputs based on the dynamically created prompts.

5. Output Customization:

   Users can define the format, tone, and language of the output.


# Installation

1. clone the repository

       git clone https://github.com/yourusername/multimodal-ai-system.git
       cd multimodal-ai-system

2. Install Dependencies:

Create a virtual environment:
         
         python -m venv venv
         source venv/bin/activate 

3. Download YOLOv8 Weights:

Download the YOLOv8 model weights from Ultralytics and place them in the models directory.

4. Set Up API Keys:

Add your OpenAI API key and any other required keys to a .env file:

        pip install -r requirements.txt
