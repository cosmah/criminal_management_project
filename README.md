# Criminal Management Project

## Overview

The Criminal Management Project is a web-based application designed to assist law enforcement agencies in managing and tracking criminal records. This system provides a centralized platform for storing, retrieving, and analyzing information related to criminal activities and suspects.

## Features

- **Criminal Record Management**: Create, update, and delete criminal records.
- **Image-based Search**: Search for criminal records using facial recognition technology.
- **Location Tracking**: Track and display the current location of the user/officer.
- **User Authentication**: Secure login system for authorized personnel.
- **Responsive Design**: Mobile-friendly interface for easy access on various devices.

## Technology Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default), compatible with PostgreSQL for production
- **APIs**: Google Maps Geocoding API for location services

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/cosmah/criminal_management_project.git
   cd criminal_management_project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000`

## Usage

1. Login with your superuser credentials.
2. Navigate through the dashboard to access different features.
3. Use the search functionality to find criminal records.
4. Add new records or update existing ones as needed.

## API Reference

The application uses the Google Maps Geocoding API for location services. Ensure you have a valid API key and enable billing on your Google Cloud account to use this feature.

## Contributing

Contributions to the Criminal Management Project are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any queries or support, please contact:
- Cosmah Seekirya
- Tel: +256708153467, +256760877809
- Email: cosmahke@gmail.com
- GitHub: [@cosmah](https://github.com/cosmah)

## Acknowledgements

- Django Documentation
- Google Maps API Documentation
- Contributors and supporters of the project

---

**Note**: This project is for educational purposes only. Ensure compliance with local laws and regulations regarding the management of sensitive information.
