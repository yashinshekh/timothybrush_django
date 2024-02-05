# Project Brief: Django Web Registration

## Project Overview: 

Develop a Django, HTMX, and Alpine web application featuring a multi-stage registration form for a classic car show by a small car club. The registration form would capture the individual's name, email, address, phone, details of their car (year, make, model), whether they will attend any sub-events, any pre-ordered merchandise (tshirts, ball caps, and toques), and a final review of their registration before being directed to PayPal for payment.  Integration with PayPal (for payments) and social authentication using Google.

### Multi-Stage Registration Form:

- Stage 1 - User Details: First and Last Name, Email (2 fields that must match to validate), Street Address, City, Province/State, Postal/Zip Code
- Stage 2 - Vehicle Details: Year, Make, Model
- Stage 3 - Sub-event (cruise night, afternoon tour, street dance)
- Stage 4 - Pre-Order Merchandise: Event T-shirts (men's and women's, multiple sizes, 2-3 colours), baseball caps (2 colours), and toques (4-5 colours)
- Stage 5 - Order review with total and PayPal button.

## Key Features:

###  1. User Profile & Authentication:

* Link extended profile information to user authentication
* Allow users to sign up/link their social media accounts seamlessly (Google)
* Ensure a secure authentication process with proper error handling and user feedback.

### 2. Payment Gateway Integration (PayPal):

* Integrate PayPal payment gateway to facilitate secure and convenient transactions.
* Implement a payment flow that allows users to make payments for services using their PayPal accounts or credit/debit cards.
* Allow users to return to/complete a pending transaction from their profile page

### 3. HTMX Integration:

* Leverage htmx to enhance user experience through seamless and dynamic updates.
* Ensure a responsive and smooth user interface with htmx features like AJAX requests and DOM manipulation.

### 4. Alpine Integration:

* Modal for Release and Waiver of Liability (ex. Registering includes your approval to use photos of your car or yourself from any organized events in any North Island Car Club publication, media package, web site, or other marketing material without remuneration.)
* Modal for Assumption of Risk and Indemnity Agreement (ex. unsanctioned burnouts will not be tolerated and vehicle owner assumes full responsibility)

### 5. User Dashboard:
    
* Provide users with a personalized dashboard to update their information, account settings, and complete any pending or failed transaction.
* Include features such as order history, profile settings, and notifications.

### 6. Responsive Design:

* Develop a responsive and user-friendly design that works well on various devices and screen sizes.
* Prefer Bootstrap 5 and usage of crispy forms 

## Required:
- django 4.2
    - django-allauth
    - django-paypal
    - django-crispy-forms
    - django-htmx
    - django-dotenv

## Deliverables:

* Fully functional Django web application with HTMX integration.
* Codebase with proper documentation.
* Integration of social authentication (Google) and PayPal
* User-friendly interface with a focus on responsiveness and usability.

### Timeline:

* Define a realistic timeline based on the complexity of the project and potential milestones.

### Budget:

* Negotiate a budget that considers the complexity of the project and the skills required.

### Additional Notes:

* Discuss any specific requirements or preferences not covered in the brief.
* Maintain clear communication channels throughout the project.
