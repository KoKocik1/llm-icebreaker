# Ice Breaker

A smart application that helps you break the ice with people by analyzing their LinkedIn profiles and generating personalized conversation starters, interesting facts, and topics of interest.

## Features

- 🔍 LinkedIn Profile Analysis
  - Automated LinkedIn profile scraping
  - Profile picture extraction
  - Professional background analysis
- 💡 Smart Ice Breakers
  - AI-generated conversation starters based on profile data
  - Personalized topics of interest
  - Interesting facts about the person
- 🎯 Topic Suggestions
  - AI-curated topics that might interest the person
  - Based on their professional background and activities
- 🚀 Fast and Efficient
  - Caching system for LinkedIn profiles
  - MongoDB integration for data persistence
  - Optimized API calls

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI/ML**: LangChain, OpenAI GPT-3.5
- **Database**: MongoDB
- **APIs**: LinkedIn, Tavily
- **Web Scraping**: Selenium, LinkedIn Scraper

## Prerequisites

- Python 3.8+
- MongoDB installed and running locally on port 27017
- Chrome browser (for LinkedIn scraping)
- OpenAI API key
- Tavily API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ice_breaker.git
   cd ice_breaker
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install and start MongoDB locally:

   ```bash
   # On macOS with Homebrew
   brew install mongodb-community
   brew services start mongodb-community

   # On Ubuntu
   sudo apt install mongodb
   sudo systemctl start mongodb

   # On Windows
   # Download and install MongoDB Community Server from mongodb.com
   # Start MongoDB service from Services
   ```

5. Set up environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   LINKEDIN_EMAIL=your_linkedin_email
   LINKEDIN_PASSWORD=your_linkedin_password
   MONGODB_URI=mongodb://localhost:27017/ice_breaker
   ```

## Usage

1. Ensure MongoDB is running locally:

   ```bash
   # Check MongoDB status
   mongosh
   ```

2. Start the Flask application:

   ```bash
   python app.py
   ```

3. Open your browser and navigate to:

   ```
   http://localhost:5001
   ```

4. Enter a person's name in the input field and click "Do Your Magic"

5. The application will:
   - Find their LinkedIn profile
   - Analyze their profile data
   - Generate personalized ice breakers
   - Display their profile picture
   - Show interesting facts and topics of interest

## Project Structure
