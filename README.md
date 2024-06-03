# Flashcard Generator

This project creates a Flashcard Generator using various technologies such as Google Gemini, Google Service Account, Langchain, YouTube transcripts, React.js, FastAPI, and Vertex AI. The project is part of the challenges provided by Radical AI, where contributions have been made to implement certain steps.

## Description

The Flashcard Generator is designed to generate flashcards based on whatever youtube video the user would like. It utilizes machine learning models for text embeddings and leverages Google's Gemini and Vertex AI API for processing the YouTube transcript into a series of flashcards. The project also incorporates React.js for the user interface to make it interactive and easy to use.

## Usage

To run the Quiz Builder:

1. Enter the backend directory and install the necessary dependencies listed in `backend/requirements.txt`. 
You can do that with the following command, while in the backend directory, `pip install -r requirements.txt`.
2. Run the frontend by executing `npm run dev`, in the src directory, `cd frontend/dynamocards/src`.
3. Run the backend by executing `uvicorn main:app --reload`, in the backend directory, `cd backend`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project is based on [mission-dynamoCards-v2](https://github.com/radicalxdev/mission-dynamoCards-v2), developed by [radicalxdev]. We thank them for providing the foundation for this project.

- [Radical AI](https://www.radicalai.org/) - For providing the challenges and inspiration for this project.
- [React.js](https://react.dev/) - For the user-friendly interface development.
- [Google Cloud Platform](https://cloud.google.com/) - For the various APIs and services used in this project.
- [Langchain](https://langchain.com/) - For providing text embeddings technology.
